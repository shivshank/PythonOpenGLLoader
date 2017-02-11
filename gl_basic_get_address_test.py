# first attempt to understand how to go about things
# kept around for history's sake
import sys
import ctypes
from ctypes import c_int, c_float, c_char_p, c_void_p, WINFUNCTYPE

_gl = ctypes.WinDLL("opengl32")
_gl.glClearColor.argtypes = [c_float, c_float, c_float, c_float]

getProcAddress = _gl.wglGetProcAddress
getProcAddress.argtypes = [c_char_p]
getProcAddress.restype = c_void_p

class NativeFunctionWrapper:
    def __init__(self, f):
        self.f = f
        self.calls = 0
    def __call__(self, *args, argtypes=None, restype=c_int):
        if type(self.f) is int:
            # lazy loader!
            if argtypes is None:
                argtypes = []
            # create a function pointer object from the address
            self.f = WINFUNCTYPE(restype, *argtypes)(self.f)
        else:
            # allow user to specify argtypes/restype (optional)
            if argtypes is not None:
                self.f.argtypes = argtypes
        self.calls += 1
        return self.f(*args)

class GL:
    # from the XML spec (ARB enums for GL 1.0/1.1)
    # https://cvs.khronos.org/svn/repos/ogl/trunk/doc/registry/public/api/gl.xml
    # alternatively, generate a header using glad or the official scripts
    GL_COLOR_BUFFER_BIT = 0x00004000
    GL_PROJECTION = 0x1701
    GL_MODELVIEW = 0x1700
    GL_TRIANGLES = 0x0004
    GL_ARRAY_BUFFER = 0x8892
    GL_STATIC_DRAW = 0x88E4
    GL_FLOAT = 0x1406
    """def glClear(self, *args):
        return _gl.glClear(*args)
    def glClearColor(self, *args):
        return _gl.glClearColor(*args)"""

    def __getattr__(self, attr):
        try:
            return NativeFunctionWrapper(getattr(_gl, attr))
        except AttributeError:
            print(attr)
            cfunc_addr = getProcAddress(attr.encode('ascii'))
            wrapper = NativeFunctionWrapper(cfunc_addr)
            # store it so we don't have to repeat this
            setattr(self, attr, wrapper)
            return wrapper

print(getProcAddress(b'glDrawArrays'))

sys.modules[__name__] = GL()
