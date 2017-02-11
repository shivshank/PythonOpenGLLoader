from . import parser
from . import python

features = [parser.import_api('gl', i) for i in (
    'GL_VERSION_1_0', 'GL_VERSION_1_1', 'GL_VERSION_1_2', 'GL_VERSION_1_3',
    'GL_VERSION_1_4', 'GL_VERSION_1_5',
    'GL_VERSION_2_0', 'GL_VERSION_2_1'
)]

header = '# Generated Windows-Only OpenGL-Python module\n'

with open('gl_generated_example.py', mode='w') as file:
    file.write(header)
    python.writeFeatures(file, features)
