import re
import xml.etree.ElementTree as ET
from . import model
import io
import requests

print('Fetching gl.xml from khronos...')
r = requests.get('https://cvs.khronos.org/svn/repos/ogl/trunk/doc/registry/public/api/gl.xml')
print('Done.')
tree = ET.parse(io.StringIO(r.text))
# TODO: Make this not global... I really don't remember doing it this way...
root = tree.getroot()

enumCache = None
commandCache = None

def import_api(api, version):
    return require_api(find_api(api, version))

def require_api(api):
    feature = model.Feature(api.get('api'), api.get('name'))
    for require in api.findall('require'):
        for element in require.iter():
            if element is require:
                continue
            if element.tag == 'enum':
                feature.enums.append(require_enum(element.get('name')))
            elif element.tag == 'command':
                feature.commands.append(require_command(element.get('name')))
            elif element.tag == 'type':
                # I have no idea what we're supposed to do with these :(
                pass
            else:
                # TODO: Should log when this happens
                pass
    return feature

def find_api(api, version):
    candidates = [i for i in root.findall('feature')
        if i.get('api') == api and i.get('name') == version]
    return candidates[0]

def require_command(name):
    cacheCommands()
    c = commandCache[name]
    proto = c.find('proto')
    # the slice at the end removes the function name
    cPrototype = ''.join(proto.itertext())[:-len(name)].strip()
    resultType, resIndirection = parseCType(cPrototype)
    params = []
    for param in c.findall('param'):
        paramName = param.find('name').text
        # the slice at the end removes the paramater name
        ptype = ''.join(param.itertext())[:-len(paramName)].strip()
        paramType, paramIndirection = parseCType(ptype)
        params.append(model.CommandParam(paramName,
            model.GLType(paramType, paramIndirection)))
    return model.Command(name, model.GLType(resultType, resIndirection), params)

def require_enum(name):
    cacheEnums()
    e = enumCache[name]
    return model.Enum(name, e.get('value'))

def cacheEnums():
    global enumCache
    if enumCache:
        return
    enumCache = {}
    enums = root.findall('enums')
    for enumBlock in enums:
        for enum in enumBlock.findall('enum'):
            enumCache[enum.get('name')] = enum

def cacheCommands():
    global commandCache
    if commandCache:
        return
    commandCache = {}
    commands = root.findall('commands')
    for commandBlock in commands:
        for command in commandBlock.findall('command'):
            name = command.find('proto').find('name').text
            commandCache[name] = command

cIdentifier = re.compile(r'([_a-zA-Z][_a-zA-Z0-9]+)$')

def parseCType(t):
    # remove const... that is meaningless for our purposes
    t = t.replace('const', '').strip()
    indirection = t.count('*')
    t = t.replace('*', '').strip()
    t = (t, indirection)
    return t
