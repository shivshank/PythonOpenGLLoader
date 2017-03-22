import itertools
import re

glTypes = {
    'void': 'None',
    'GLenum': 'c_uint',
    'GLboolean': 'c_bool',
    'GLbitfield': 'c_uint',
    'GLbyte': 'c_byte',
    'GLshort': 'c_short',
    'GLint': 'c_int',
    'GLint64': 'c_int64',
    'GLclampx': 'c_int',
    'GLubyte': 'c_ubyte',
    'GLushort': 'c_ushort',
    'GLuint': 'c_uint',
    'GLuint64': 'c_uint64',
    'GLsizei': 'c_int',
    'GLfloat': 'c_float',
    'GLclampf': 'c_float',
    'GLdouble': 'c_double',
    'GLclampd': 'c_double',
    'GLchar': 'c_char',
    'GLsizeiptr': 'ptrdiff_t',
    'GLintptr': 'ptrdiff_t',
    'GLsync': 'c_void_p'
}

setupCode = """import re
from ctypes import WinDLL, WINFUNCTYPE, sizeof, cast, \\
    POINTER, c_void_p, c_char_p, c_int32, c_int64, {0}

if sizeof(c_void_p) == 4:
    ptrdiff_t = c_int32
elif sizeof(c_void_p) == 8:
    ptrdiff_t = c_int64

# _gl will be None if the library is not loaded by ctypes
_gl = None
_nglGetProcAddress = None

# to be set when OpenGL is loaded (by any means through this library)
glVersion = {{
    "major": None,
    "minor": None
}}

def _loadGLLibrary():
    global _gl, _nglGetProcAddress
    _gl = WinDLL("opengl32")
    _nglGetProcAddress = _gl.wglGetProcAddress
    _nglGetProcAddress.argtypes = [c_char_p]
    _nglGetProcAddress.restype = c_void_p

def _getProcAddress(func):
    if _gl is None or _nglGetProcAddress is None:
        raise ValueError("_getProcAddress can only be called when ctypes loads "
            "OpenGL library")
    try:
        return getattr(_gl, func)
    except AttributeError:
        return _nglGetProcAddress(func.encode('ascii'))

def _makeFunction(address, restype, *argtypes):
    \"\"\"addresses returned by glGetProcAddress => python callable\"\"\"
    if address is None or address == 0:
        raise RuntimeError('Function not available', func)
    # functions exported directly by the shared library will already be callable
    if type(address) is int:
        func_type = WINFUNCTYPE(restype, *argtypes)
        return func_type(address)
    f = address
    f.restype = restype
    f.argtypes = argtypes
    return f
"""
setupCode = setupCode.replace('    ', '\t')

loaders = """def loadGL(loader=_getProcAddress):
    if loader is _getProcAddress:
        _loadGLLibrary()
    # OpenGL 1.0 will export this... let's just make our own temp reference
    _tempGlgs = _makeFunction(loader("glGetString"), POINTER(c_ubyte), c_uint)
    versionStr = cast(_tempGlgs(GL_VERSION), c_char_p)
    match = re.search(rb'(\d+).(\d+)', versionStr.value)
    majorBStr, minorBStr = match.group(1, 2)
    glVersion["major"] = int(majorBStr)
    glVersion["minor"] = int(minorBStr)"""
loaders = loaders.replace('    ', '\t')

def writeSetup(buffer):
    skip_types = set(
        'None, c_void_p, c_char_p, c_int32, c_int64, ptrdiff_t'.split(', '))
    buffer.write(setupCode.format(
        ', '.join(i for i in glTypes.values() if i not in skip_types)))

def writeFeatures(buffer, features):
    enums = itertools.chain(*(f.enums for f in features))
    writeSetup(buffer)
    buffer.write('\n')
    for e in enums:
        writeEnum(buffer, e)
    buffer.write('\n')
    calls = []
    for f in features:
        call = writeCommands(buffer, f)
        calls.append(call)
        buffer.write('\n')
    writeLoader(buffer, calls)

def writeLoader(buffer, calls):
    buffer.write(loaders.rstrip() + '\n')
    for c in calls:
        buffer.write('\t' + c.strip() + '\n')

def writeCommands(buffer, feature, loaderName='loader'):
    buffer.write('def __load_{}(loader):\n'.format(feature.version))
    call = "__load_{}({})".format(feature.version, loaderName)
    match = re.search(r'(\d+)_(\d+)', feature.version)
    featMaj, featMin = match.group(1, 2)
    buffer.write("\tif glVersion['major'] < {0} or (glVersion['major'] == {0}\n"
        "\t\t\tand glVersion['minor'] < {1}):\n"
        "\t\treturn\n".format(featMaj, featMin))
    for command in feature.commands:
        try:
            # loaderName refers to the loader variable name in the enclosing
            # scope; loaderStr passed to commandToPython refers to it in local
            # scope; see def of the function this outputs
            buffer.write(commandToPython(command, 'loader'))
        except KeyError as e:
            # TODO: this should be logged
            print(command.name)
            raise e
    return call

def writeEnum(buffer, enum):
    buffer.write('{} = {}\n'.format(enum.name, enum.value))

funcTemplate = "\tglobal {exportName}\n" + \
    "\t{exportName} = _makeFunction({loader}('{glName}'), {resAndParams})\n"

def commandToPython(command, loaderStr):
    params = ', '.join(glTypeToPython(i.type) for i in command.params)
    signature = glTypeToPython(command.resType)
    if params:
        signature += ', ' + params
    formatted = funcTemplate.format(glName=command.name,
        exportName=command.name,
        resAndParams=signature,
        loader=loaderStr)
    return formatted

def glTypeToPython(t):
    pyType = glTypes[t.name]
    if t.indirection > 0:
        try:
            special = {
                'None': 'c_void_p',
                'c_char': 'c_char_p'
            }[pyType]
            if t.indirection == 1:
                return special
            indirection = t.indirection - 1
            pyType = special
        except KeyError:
            indirection = t.indirection
        return 'POINTER(' * indirection + pyType + ')' * indirection
    return pyType
