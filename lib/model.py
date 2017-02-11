class Feature:
    def __init__(self, api, version):
        self.api = api
        self.version = version
        self.groups = []
        self.enums = []
        self.commands = []
        self.types = []

class Type:
    def __init__(self):
        pass

class Group:
    def __init__(self, name):
        self.enums = []
    def addEnum(self, enum):
        self.enums.append(enum)

class Enum:
    def __init__(self, name, value):
        self.name = name
        self.value = value

class Command:
    def __init__(self, name, resType, params):
        self.name = name
        self.resType = resType
        self.params = params

class CommandParam:
    def __init__(self, parameter, ptype):
        self.name = parameter
        self.type = ptype

class GLType:
    def __init__(self, name, indirection=0, length=None, group=None):
        self.name = name
        self.indirection = indirection
        self.length = length
        self.group = group
