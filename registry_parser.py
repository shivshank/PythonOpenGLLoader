import xml.etree.ElementTree as ET
from io import StringIO

tree = ET.parse('khronos/gl.xml')
root = tree.getroot()

def allText(element):
    """
        subtree => text without tags and extra whitespace stripped
        ^ bad wording, sorry
        REFACTOR: Not sure if there's another method that already does this
    """
    return ' '.join(i.strip() for i in element.itertext() if i.strip())

# get the standard enums

def parseEnums(root, out):
    enumDefinitions = (i for i in root.findall('enums'))
    for enumGroup in enumDefinitions:
        for enum in enumGroup.iter(tag='enum'):
            out.write("{} = {}\n".format(enum.get("name"), enum.get("value")))

class UnresolvedType:
    cache = {}
    def __init__(self, glType, group=None):
        """
            glType is whatever **** the spec shoots at us

            It should be whatever the c type is
        """
        self.name = glType
        self.group = group

def parseType(specText, group=None):
    specText = specText.strip()
    types = UnresolvedType.cache.get(specText, None)
    if types is None:
         t = UnresolvedType(specText, group)
         UnresolvedType.cache[specText] = [t]
    else:
        for candidate in types:
            if candidate.group == group:
                t = candidate
                break
        else:
            t = UnresolvedType(specText, group)
            UnresolvedType.cache[specText].append(t)
    return t

class Parameter:
    def __init__(self, name, _type, group=None, length=None):
        self.name = name
        self.type = _type
        # used for GLenums and GLbooleans
        self.group = group
        # used on array/pointer types... maybe useful
        self.length = length

class Function:
    def __init__(self, name, returnType, params):
        self.name = name
        self.returnType = returnType
        self.params = params

def parseCommands(root):
    commands = root.find('commands')
    output = {}
    for func in commands.iter(tag='command'):
        proto = func.find('proto')
        name = proto.find('name').text
        returnType = allText(proto).rsplit(name, 1)[0]
        returnType = parseType(returnType, group=proto.get('group'))
        params = []
        for p in func.iter(tag='param'):
            # construct a C-style definition... then we'll extract
            # ElementTree... why no text nodes?
            cDef = allText(p)
            param_name = p.find('name').text
            param_type = cDef.rsplit(param_name, 1)[0]
            params.append(Parameter(param_name,
                parseType(param_type, group=p.get('group')),
                length=p.get('len')))
        result = Function(name, returnType, tuple(params))
        output[result.name] = result
    return output

glda = parseCommands(root)["glDrawArrays"]

for k, v in UnresolvedType.cache.items():
    print(k, v)
