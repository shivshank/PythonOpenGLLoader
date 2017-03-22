# Generated Windows-Only OpenGL-Python module
import re
from ctypes import WinDLL, WINFUNCTYPE, sizeof, cast, \
	POINTER, c_void_p, c_char_p, c_int32, c_int64, c_uint, c_bool, c_uint, c_byte, c_short, c_int, c_int, c_ubyte, c_ushort, c_uint, c_uint64, c_int, c_float, c_float, c_double, c_double, c_char

if sizeof(c_void_p) == 4:
	ptrdiff_t = c_int32
elif sizeof(c_void_p) == 8:
	ptrdiff_t = c_int64

# _gl will be None if the library is not loaded by ctypes
_gl = None
_nglGetProcAddress = None

# to be set when OpenGL is loaded (by any means through this library)
glVersion = {
	"major": None,
	"minor": None
}

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
	"""addresses returned by glGetProcAddress => python callable"""
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

GL_DEPTH_BUFFER_BIT = 0x00000100
GL_STENCIL_BUFFER_BIT = 0x00000400
GL_COLOR_BUFFER_BIT = 0x00004000
GL_FALSE = 0
GL_TRUE = 1
GL_POINTS = 0x0000
GL_LINES = 0x0001
GL_LINE_LOOP = 0x0002
GL_LINE_STRIP = 0x0003
GL_TRIANGLES = 0x0004
GL_TRIANGLE_STRIP = 0x0005
GL_TRIANGLE_FAN = 0x0006
GL_QUADS = 0x0007
GL_NEVER = 0x0200
GL_LESS = 0x0201
GL_EQUAL = 0x0202
GL_LEQUAL = 0x0203
GL_GREATER = 0x0204
GL_NOTEQUAL = 0x0205
GL_GEQUAL = 0x0206
GL_ALWAYS = 0x0207
GL_ZERO = 0
GL_ONE = 1
GL_SRC_COLOR = 0x0300
GL_ONE_MINUS_SRC_COLOR = 0x0301
GL_SRC_ALPHA = 0x0302
GL_ONE_MINUS_SRC_ALPHA = 0x0303
GL_DST_ALPHA = 0x0304
GL_ONE_MINUS_DST_ALPHA = 0x0305
GL_DST_COLOR = 0x0306
GL_ONE_MINUS_DST_COLOR = 0x0307
GL_SRC_ALPHA_SATURATE = 0x0308
GL_NONE = 0
GL_FRONT_LEFT = 0x0400
GL_FRONT_RIGHT = 0x0401
GL_BACK_LEFT = 0x0402
GL_BACK_RIGHT = 0x0403
GL_FRONT = 0x0404
GL_BACK = 0x0405
GL_LEFT = 0x0406
GL_RIGHT = 0x0407
GL_FRONT_AND_BACK = 0x0408
GL_NO_ERROR = 0
GL_INVALID_ENUM = 0x0500
GL_INVALID_VALUE = 0x0501
GL_INVALID_OPERATION = 0x0502
GL_OUT_OF_MEMORY = 0x0505
GL_CW = 0x0900
GL_CCW = 0x0901
GL_POINT_SIZE = 0x0B11
GL_POINT_SIZE_RANGE = 0x0B12
GL_POINT_SIZE_GRANULARITY = 0x0B13
GL_LINE_SMOOTH = 0x0B20
GL_LINE_WIDTH = 0x0B21
GL_LINE_WIDTH_RANGE = 0x0B22
GL_LINE_WIDTH_GRANULARITY = 0x0B23
GL_POLYGON_MODE = 0x0B40
GL_POLYGON_SMOOTH = 0x0B41
GL_CULL_FACE = 0x0B44
GL_CULL_FACE_MODE = 0x0B45
GL_FRONT_FACE = 0x0B46
GL_DEPTH_RANGE = 0x0B70
GL_DEPTH_TEST = 0x0B71
GL_DEPTH_WRITEMASK = 0x0B72
GL_DEPTH_CLEAR_VALUE = 0x0B73
GL_DEPTH_FUNC = 0x0B74
GL_STENCIL_TEST = 0x0B90
GL_STENCIL_CLEAR_VALUE = 0x0B91
GL_STENCIL_FUNC = 0x0B92
GL_STENCIL_VALUE_MASK = 0x0B93
GL_STENCIL_FAIL = 0x0B94
GL_STENCIL_PASS_DEPTH_FAIL = 0x0B95
GL_STENCIL_PASS_DEPTH_PASS = 0x0B96
GL_STENCIL_REF = 0x0B97
GL_STENCIL_WRITEMASK = 0x0B98
GL_VIEWPORT = 0x0BA2
GL_DITHER = 0x0BD0
GL_BLEND_DST = 0x0BE0
GL_BLEND_SRC = 0x0BE1
GL_BLEND = 0x0BE2
GL_LOGIC_OP_MODE = 0x0BF0
GL_COLOR_LOGIC_OP = 0x0BF2
GL_DRAW_BUFFER = 0x0C01
GL_READ_BUFFER = 0x0C02
GL_SCISSOR_BOX = 0x0C10
GL_SCISSOR_TEST = 0x0C11
GL_COLOR_CLEAR_VALUE = 0x0C22
GL_COLOR_WRITEMASK = 0x0C23
GL_DOUBLEBUFFER = 0x0C32
GL_STEREO = 0x0C33
GL_LINE_SMOOTH_HINT = 0x0C52
GL_POLYGON_SMOOTH_HINT = 0x0C53
GL_UNPACK_SWAP_BYTES = 0x0CF0
GL_UNPACK_LSB_FIRST = 0x0CF1
GL_UNPACK_ROW_LENGTH = 0x0CF2
GL_UNPACK_SKIP_ROWS = 0x0CF3
GL_UNPACK_SKIP_PIXELS = 0x0CF4
GL_UNPACK_ALIGNMENT = 0x0CF5
GL_PACK_SWAP_BYTES = 0x0D00
GL_PACK_LSB_FIRST = 0x0D01
GL_PACK_ROW_LENGTH = 0x0D02
GL_PACK_SKIP_ROWS = 0x0D03
GL_PACK_SKIP_PIXELS = 0x0D04
GL_PACK_ALIGNMENT = 0x0D05
GL_MAX_TEXTURE_SIZE = 0x0D33
GL_MAX_VIEWPORT_DIMS = 0x0D3A
GL_SUBPIXEL_BITS = 0x0D50
GL_TEXTURE_1D = 0x0DE0
GL_TEXTURE_2D = 0x0DE1
GL_POLYGON_OFFSET_UNITS = 0x2A00
GL_POLYGON_OFFSET_POINT = 0x2A01
GL_POLYGON_OFFSET_LINE = 0x2A02
GL_POLYGON_OFFSET_FILL = 0x8037
GL_POLYGON_OFFSET_FACTOR = 0x8038
GL_TEXTURE_BINDING_1D = 0x8068
GL_TEXTURE_BINDING_2D = 0x8069
GL_TEXTURE_WIDTH = 0x1000
GL_TEXTURE_HEIGHT = 0x1001
GL_TEXTURE_INTERNAL_FORMAT = 0x1003
GL_TEXTURE_BORDER_COLOR = 0x1004
GL_TEXTURE_RED_SIZE = 0x805C
GL_TEXTURE_GREEN_SIZE = 0x805D
GL_TEXTURE_BLUE_SIZE = 0x805E
GL_TEXTURE_ALPHA_SIZE = 0x805F
GL_DONT_CARE = 0x1100
GL_FASTEST = 0x1101
GL_NICEST = 0x1102
GL_BYTE = 0x1400
GL_UNSIGNED_BYTE = 0x1401
GL_SHORT = 0x1402
GL_UNSIGNED_SHORT = 0x1403
GL_INT = 0x1404
GL_UNSIGNED_INT = 0x1405
GL_FLOAT = 0x1406
GL_DOUBLE = 0x140A
GL_STACK_OVERFLOW = 0x0503
GL_STACK_UNDERFLOW = 0x0504
GL_CLEAR = 0x1500
GL_AND = 0x1501
GL_AND_REVERSE = 0x1502
GL_COPY = 0x1503
GL_AND_INVERTED = 0x1504
GL_NOOP = 0x1505
GL_XOR = 0x1506
GL_OR = 0x1507
GL_NOR = 0x1508
GL_EQUIV = 0x1509
GL_INVERT = 0x150A
GL_OR_REVERSE = 0x150B
GL_COPY_INVERTED = 0x150C
GL_OR_INVERTED = 0x150D
GL_NAND = 0x150E
GL_SET = 0x150F
GL_TEXTURE = 0x1702
GL_COLOR = 0x1800
GL_DEPTH = 0x1801
GL_STENCIL = 0x1802
GL_STENCIL_INDEX = 0x1901
GL_DEPTH_COMPONENT = 0x1902
GL_RED = 0x1903
GL_GREEN = 0x1904
GL_BLUE = 0x1905
GL_ALPHA = 0x1906
GL_RGB = 0x1907
GL_RGBA = 0x1908
GL_POINT = 0x1B00
GL_LINE = 0x1B01
GL_FILL = 0x1B02
GL_KEEP = 0x1E00
GL_REPLACE = 0x1E01
GL_INCR = 0x1E02
GL_DECR = 0x1E03
GL_VENDOR = 0x1F00
GL_RENDERER = 0x1F01
GL_VERSION = 0x1F02
GL_EXTENSIONS = 0x1F03
GL_NEAREST = 0x2600
GL_LINEAR = 0x2601
GL_NEAREST_MIPMAP_NEAREST = 0x2700
GL_LINEAR_MIPMAP_NEAREST = 0x2701
GL_NEAREST_MIPMAP_LINEAR = 0x2702
GL_LINEAR_MIPMAP_LINEAR = 0x2703
GL_TEXTURE_MAG_FILTER = 0x2800
GL_TEXTURE_MIN_FILTER = 0x2801
GL_TEXTURE_WRAP_S = 0x2802
GL_TEXTURE_WRAP_T = 0x2803
GL_PROXY_TEXTURE_1D = 0x8063
GL_PROXY_TEXTURE_2D = 0x8064
GL_REPEAT = 0x2901
GL_R3_G3_B2 = 0x2A10
GL_RGB4 = 0x804F
GL_RGB5 = 0x8050
GL_RGB8 = 0x8051
GL_RGB10 = 0x8052
GL_RGB12 = 0x8053
GL_RGB16 = 0x8054
GL_RGBA2 = 0x8055
GL_RGBA4 = 0x8056
GL_RGB5_A1 = 0x8057
GL_RGBA8 = 0x8058
GL_RGB10_A2 = 0x8059
GL_RGBA12 = 0x805A
GL_RGBA16 = 0x805B
GL_CURRENT_BIT = 0x00000001
GL_POINT_BIT = 0x00000002
GL_LINE_BIT = 0x00000004
GL_POLYGON_BIT = 0x00000008
GL_POLYGON_STIPPLE_BIT = 0x00000010
GL_PIXEL_MODE_BIT = 0x00000020
GL_LIGHTING_BIT = 0x00000040
GL_FOG_BIT = 0x00000080
GL_ACCUM_BUFFER_BIT = 0x00000200
GL_VIEWPORT_BIT = 0x00000800
GL_TRANSFORM_BIT = 0x00001000
GL_ENABLE_BIT = 0x00002000
GL_HINT_BIT = 0x00008000
GL_EVAL_BIT = 0x00010000
GL_LIST_BIT = 0x00020000
GL_TEXTURE_BIT = 0x00040000
GL_SCISSOR_BIT = 0x00080000
GL_ALL_ATTRIB_BITS = 0xFFFFFFFF
GL_CLIENT_PIXEL_STORE_BIT = 0x00000001
GL_CLIENT_VERTEX_ARRAY_BIT = 0x00000002
GL_CLIENT_ALL_ATTRIB_BITS = 0xFFFFFFFF
GL_QUAD_STRIP = 0x0008
GL_POLYGON = 0x0009
GL_ACCUM = 0x0100
GL_LOAD = 0x0101
GL_RETURN = 0x0102
GL_MULT = 0x0103
GL_ADD = 0x0104
GL_AUX0 = 0x0409
GL_AUX1 = 0x040A
GL_AUX2 = 0x040B
GL_AUX3 = 0x040C
GL_2D = 0x0600
GL_3D = 0x0601
GL_3D_COLOR = 0x0602
GL_3D_COLOR_TEXTURE = 0x0603
GL_4D_COLOR_TEXTURE = 0x0604
GL_PASS_THROUGH_TOKEN = 0x0700
GL_POINT_TOKEN = 0x0701
GL_LINE_TOKEN = 0x0702
GL_POLYGON_TOKEN = 0x0703
GL_BITMAP_TOKEN = 0x0704
GL_DRAW_PIXEL_TOKEN = 0x0705
GL_COPY_PIXEL_TOKEN = 0x0706
GL_LINE_RESET_TOKEN = 0x0707
GL_EXP = 0x0800
GL_EXP2 = 0x0801
GL_COEFF = 0x0A00
GL_ORDER = 0x0A01
GL_DOMAIN = 0x0A02
GL_PIXEL_MAP_I_TO_I = 0x0C70
GL_PIXEL_MAP_S_TO_S = 0x0C71
GL_PIXEL_MAP_I_TO_R = 0x0C72
GL_PIXEL_MAP_I_TO_G = 0x0C73
GL_PIXEL_MAP_I_TO_B = 0x0C74
GL_PIXEL_MAP_I_TO_A = 0x0C75
GL_PIXEL_MAP_R_TO_R = 0x0C76
GL_PIXEL_MAP_G_TO_G = 0x0C77
GL_PIXEL_MAP_B_TO_B = 0x0C78
GL_PIXEL_MAP_A_TO_A = 0x0C79
GL_VERTEX_ARRAY_POINTER = 0x808E
GL_NORMAL_ARRAY_POINTER = 0x808F
GL_COLOR_ARRAY_POINTER = 0x8090
GL_INDEX_ARRAY_POINTER = 0x8091
GL_TEXTURE_COORD_ARRAY_POINTER = 0x8092
GL_EDGE_FLAG_ARRAY_POINTER = 0x8093
GL_FEEDBACK_BUFFER_POINTER = 0x0DF0
GL_SELECTION_BUFFER_POINTER = 0x0DF3
GL_CURRENT_COLOR = 0x0B00
GL_CURRENT_INDEX = 0x0B01
GL_CURRENT_NORMAL = 0x0B02
GL_CURRENT_TEXTURE_COORDS = 0x0B03
GL_CURRENT_RASTER_COLOR = 0x0B04
GL_CURRENT_RASTER_INDEX = 0x0B05
GL_CURRENT_RASTER_TEXTURE_COORDS = 0x0B06
GL_CURRENT_RASTER_POSITION = 0x0B07
GL_CURRENT_RASTER_POSITION_VALID = 0x0B08
GL_CURRENT_RASTER_DISTANCE = 0x0B09
GL_POINT_SMOOTH = 0x0B10
GL_LINE_STIPPLE = 0x0B24
GL_LINE_STIPPLE_PATTERN = 0x0B25
GL_LINE_STIPPLE_REPEAT = 0x0B26
GL_LIST_MODE = 0x0B30
GL_MAX_LIST_NESTING = 0x0B31
GL_LIST_BASE = 0x0B32
GL_LIST_INDEX = 0x0B33
GL_POLYGON_STIPPLE = 0x0B42
GL_EDGE_FLAG = 0x0B43
GL_LIGHTING = 0x0B50
GL_LIGHT_MODEL_LOCAL_VIEWER = 0x0B51
GL_LIGHT_MODEL_TWO_SIDE = 0x0B52
GL_LIGHT_MODEL_AMBIENT = 0x0B53
GL_SHADE_MODEL = 0x0B54
GL_COLOR_MATERIAL_FACE = 0x0B55
GL_COLOR_MATERIAL_PARAMETER = 0x0B56
GL_COLOR_MATERIAL = 0x0B57
GL_FOG = 0x0B60
GL_FOG_INDEX = 0x0B61
GL_FOG_DENSITY = 0x0B62
GL_FOG_START = 0x0B63
GL_FOG_END = 0x0B64
GL_FOG_MODE = 0x0B65
GL_FOG_COLOR = 0x0B66
GL_ACCUM_CLEAR_VALUE = 0x0B80
GL_MATRIX_MODE = 0x0BA0
GL_NORMALIZE = 0x0BA1
GL_MODELVIEW_STACK_DEPTH = 0x0BA3
GL_PROJECTION_STACK_DEPTH = 0x0BA4
GL_TEXTURE_STACK_DEPTH = 0x0BA5
GL_MODELVIEW_MATRIX = 0x0BA6
GL_PROJECTION_MATRIX = 0x0BA7
GL_TEXTURE_MATRIX = 0x0BA8
GL_ATTRIB_STACK_DEPTH = 0x0BB0
GL_CLIENT_ATTRIB_STACK_DEPTH = 0x0BB1
GL_ALPHA_TEST = 0x0BC0
GL_ALPHA_TEST_FUNC = 0x0BC1
GL_ALPHA_TEST_REF = 0x0BC2
GL_INDEX_LOGIC_OP = 0x0BF1
GL_LOGIC_OP = 0x0BF1
GL_AUX_BUFFERS = 0x0C00
GL_INDEX_CLEAR_VALUE = 0x0C20
GL_INDEX_WRITEMASK = 0x0C21
GL_INDEX_MODE = 0x0C30
GL_RGBA_MODE = 0x0C31
GL_RENDER_MODE = 0x0C40
GL_PERSPECTIVE_CORRECTION_HINT = 0x0C50
GL_POINT_SMOOTH_HINT = 0x0C51
GL_FOG_HINT = 0x0C54
GL_TEXTURE_GEN_S = 0x0C60
GL_TEXTURE_GEN_T = 0x0C61
GL_TEXTURE_GEN_R = 0x0C62
GL_TEXTURE_GEN_Q = 0x0C63
GL_PIXEL_MAP_I_TO_I_SIZE = 0x0CB0
GL_PIXEL_MAP_S_TO_S_SIZE = 0x0CB1
GL_PIXEL_MAP_I_TO_R_SIZE = 0x0CB2
GL_PIXEL_MAP_I_TO_G_SIZE = 0x0CB3
GL_PIXEL_MAP_I_TO_B_SIZE = 0x0CB4
GL_PIXEL_MAP_I_TO_A_SIZE = 0x0CB5
GL_PIXEL_MAP_R_TO_R_SIZE = 0x0CB6
GL_PIXEL_MAP_G_TO_G_SIZE = 0x0CB7
GL_PIXEL_MAP_B_TO_B_SIZE = 0x0CB8
GL_PIXEL_MAP_A_TO_A_SIZE = 0x0CB9
GL_MAP_COLOR = 0x0D10
GL_MAP_STENCIL = 0x0D11
GL_INDEX_SHIFT = 0x0D12
GL_INDEX_OFFSET = 0x0D13
GL_RED_SCALE = 0x0D14
GL_RED_BIAS = 0x0D15
GL_ZOOM_X = 0x0D16
GL_ZOOM_Y = 0x0D17
GL_GREEN_SCALE = 0x0D18
GL_GREEN_BIAS = 0x0D19
GL_BLUE_SCALE = 0x0D1A
GL_BLUE_BIAS = 0x0D1B
GL_ALPHA_SCALE = 0x0D1C
GL_ALPHA_BIAS = 0x0D1D
GL_DEPTH_SCALE = 0x0D1E
GL_DEPTH_BIAS = 0x0D1F
GL_MAX_EVAL_ORDER = 0x0D30
GL_MAX_LIGHTS = 0x0D31
GL_MAX_CLIP_PLANES = 0x0D32
GL_MAX_PIXEL_MAP_TABLE = 0x0D34
GL_MAX_ATTRIB_STACK_DEPTH = 0x0D35
GL_MAX_MODELVIEW_STACK_DEPTH = 0x0D36
GL_MAX_NAME_STACK_DEPTH = 0x0D37
GL_MAX_PROJECTION_STACK_DEPTH = 0x0D38
GL_MAX_TEXTURE_STACK_DEPTH = 0x0D39
GL_MAX_CLIENT_ATTRIB_STACK_DEPTH = 0x0D3B
GL_INDEX_BITS = 0x0D51
GL_RED_BITS = 0x0D52
GL_GREEN_BITS = 0x0D53
GL_BLUE_BITS = 0x0D54
GL_ALPHA_BITS = 0x0D55
GL_DEPTH_BITS = 0x0D56
GL_STENCIL_BITS = 0x0D57
GL_ACCUM_RED_BITS = 0x0D58
GL_ACCUM_GREEN_BITS = 0x0D59
GL_ACCUM_BLUE_BITS = 0x0D5A
GL_ACCUM_ALPHA_BITS = 0x0D5B
GL_NAME_STACK_DEPTH = 0x0D70
GL_AUTO_NORMAL = 0x0D80
GL_MAP1_COLOR_4 = 0x0D90
GL_MAP1_INDEX = 0x0D91
GL_MAP1_NORMAL = 0x0D92
GL_MAP1_TEXTURE_COORD_1 = 0x0D93
GL_MAP1_TEXTURE_COORD_2 = 0x0D94
GL_MAP1_TEXTURE_COORD_3 = 0x0D95
GL_MAP1_TEXTURE_COORD_4 = 0x0D96
GL_MAP1_VERTEX_3 = 0x0D97
GL_MAP1_VERTEX_4 = 0x0D98
GL_MAP2_COLOR_4 = 0x0DB0
GL_MAP2_INDEX = 0x0DB1
GL_MAP2_NORMAL = 0x0DB2
GL_MAP2_TEXTURE_COORD_1 = 0x0DB3
GL_MAP2_TEXTURE_COORD_2 = 0x0DB4
GL_MAP2_TEXTURE_COORD_3 = 0x0DB5
GL_MAP2_TEXTURE_COORD_4 = 0x0DB6
GL_MAP2_VERTEX_3 = 0x0DB7
GL_MAP2_VERTEX_4 = 0x0DB8
GL_MAP1_GRID_DOMAIN = 0x0DD0
GL_MAP1_GRID_SEGMENTS = 0x0DD1
GL_MAP2_GRID_DOMAIN = 0x0DD2
GL_MAP2_GRID_SEGMENTS = 0x0DD3
GL_FEEDBACK_BUFFER_SIZE = 0x0DF1
GL_FEEDBACK_BUFFER_TYPE = 0x0DF2
GL_SELECTION_BUFFER_SIZE = 0x0DF4
GL_VERTEX_ARRAY = 0x8074
GL_NORMAL_ARRAY = 0x8075
GL_COLOR_ARRAY = 0x8076
GL_INDEX_ARRAY = 0x8077
GL_TEXTURE_COORD_ARRAY = 0x8078
GL_EDGE_FLAG_ARRAY = 0x8079
GL_VERTEX_ARRAY_SIZE = 0x807A
GL_VERTEX_ARRAY_TYPE = 0x807B
GL_VERTEX_ARRAY_STRIDE = 0x807C
GL_NORMAL_ARRAY_TYPE = 0x807E
GL_NORMAL_ARRAY_STRIDE = 0x807F
GL_COLOR_ARRAY_SIZE = 0x8081
GL_COLOR_ARRAY_TYPE = 0x8082
GL_COLOR_ARRAY_STRIDE = 0x8083
GL_INDEX_ARRAY_TYPE = 0x8085
GL_INDEX_ARRAY_STRIDE = 0x8086
GL_TEXTURE_COORD_ARRAY_SIZE = 0x8088
GL_TEXTURE_COORD_ARRAY_TYPE = 0x8089
GL_TEXTURE_COORD_ARRAY_STRIDE = 0x808A
GL_EDGE_FLAG_ARRAY_STRIDE = 0x808C
GL_TEXTURE_COMPONENTS = 0x1003
GL_TEXTURE_BORDER = 0x1005
GL_TEXTURE_LUMINANCE_SIZE = 0x8060
GL_TEXTURE_INTENSITY_SIZE = 0x8061
GL_TEXTURE_PRIORITY = 0x8066
GL_TEXTURE_RESIDENT = 0x8067
GL_AMBIENT = 0x1200
GL_DIFFUSE = 0x1201
GL_SPECULAR = 0x1202
GL_POSITION = 0x1203
GL_SPOT_DIRECTION = 0x1204
GL_SPOT_EXPONENT = 0x1205
GL_SPOT_CUTOFF = 0x1206
GL_CONSTANT_ATTENUATION = 0x1207
GL_LINEAR_ATTENUATION = 0x1208
GL_QUADRATIC_ATTENUATION = 0x1209
GL_COMPILE = 0x1300
GL_COMPILE_AND_EXECUTE = 0x1301
GL_2_BYTES = 0x1407
GL_3_BYTES = 0x1408
GL_4_BYTES = 0x1409
GL_EMISSION = 0x1600
GL_SHININESS = 0x1601
GL_AMBIENT_AND_DIFFUSE = 0x1602
GL_COLOR_INDEXES = 0x1603
GL_MODELVIEW = 0x1700
GL_PROJECTION = 0x1701
GL_COLOR_INDEX = 0x1900
GL_LUMINANCE = 0x1909
GL_LUMINANCE_ALPHA = 0x190A
GL_BITMAP = 0x1A00
GL_RENDER = 0x1C00
GL_FEEDBACK = 0x1C01
GL_SELECT = 0x1C02
GL_FLAT = 0x1D00
GL_SMOOTH = 0x1D01
GL_S = 0x2000
GL_T = 0x2001
GL_R = 0x2002
GL_Q = 0x2003
GL_MODULATE = 0x2100
GL_DECAL = 0x2101
GL_TEXTURE_ENV_MODE = 0x2200
GL_TEXTURE_ENV_COLOR = 0x2201
GL_TEXTURE_ENV = 0x2300
GL_EYE_LINEAR = 0x2400
GL_OBJECT_LINEAR = 0x2401
GL_SPHERE_MAP = 0x2402
GL_TEXTURE_GEN_MODE = 0x2500
GL_OBJECT_PLANE = 0x2501
GL_EYE_PLANE = 0x2502
GL_CLAMP = 0x2900
GL_ALPHA4 = 0x803B
GL_ALPHA8 = 0x803C
GL_ALPHA12 = 0x803D
GL_ALPHA16 = 0x803E
GL_LUMINANCE4 = 0x803F
GL_LUMINANCE8 = 0x8040
GL_LUMINANCE12 = 0x8041
GL_LUMINANCE16 = 0x8042
GL_LUMINANCE4_ALPHA4 = 0x8043
GL_LUMINANCE6_ALPHA2 = 0x8044
GL_LUMINANCE8_ALPHA8 = 0x8045
GL_LUMINANCE12_ALPHA4 = 0x8046
GL_LUMINANCE12_ALPHA12 = 0x8047
GL_LUMINANCE16_ALPHA16 = 0x8048
GL_INTENSITY = 0x8049
GL_INTENSITY4 = 0x804A
GL_INTENSITY8 = 0x804B
GL_INTENSITY12 = 0x804C
GL_INTENSITY16 = 0x804D
GL_V2F = 0x2A20
GL_V3F = 0x2A21
GL_C4UB_V2F = 0x2A22
GL_C4UB_V3F = 0x2A23
GL_C3F_V3F = 0x2A24
GL_N3F_V3F = 0x2A25
GL_C4F_N3F_V3F = 0x2A26
GL_T2F_V3F = 0x2A27
GL_T4F_V4F = 0x2A28
GL_T2F_C4UB_V3F = 0x2A29
GL_T2F_C3F_V3F = 0x2A2A
GL_T2F_N3F_V3F = 0x2A2B
GL_T2F_C4F_N3F_V3F = 0x2A2C
GL_T4F_C4F_N3F_V4F = 0x2A2D
GL_CLIP_PLANE0 = 0x3000
GL_CLIP_PLANE1 = 0x3001
GL_CLIP_PLANE2 = 0x3002
GL_CLIP_PLANE3 = 0x3003
GL_CLIP_PLANE4 = 0x3004
GL_CLIP_PLANE5 = 0x3005
GL_LIGHT0 = 0x4000
GL_LIGHT1 = 0x4001
GL_LIGHT2 = 0x4002
GL_LIGHT3 = 0x4003
GL_LIGHT4 = 0x4004
GL_LIGHT5 = 0x4005
GL_LIGHT6 = 0x4006
GL_LIGHT7 = 0x4007
GL_UNSIGNED_BYTE_3_3_2 = 0x8032
GL_UNSIGNED_SHORT_4_4_4_4 = 0x8033
GL_UNSIGNED_SHORT_5_5_5_1 = 0x8034
GL_UNSIGNED_INT_8_8_8_8 = 0x8035
GL_UNSIGNED_INT_10_10_10_2 = 0x8036
GL_TEXTURE_BINDING_3D = 0x806A
GL_PACK_SKIP_IMAGES = 0x806B
GL_PACK_IMAGE_HEIGHT = 0x806C
GL_UNPACK_SKIP_IMAGES = 0x806D
GL_UNPACK_IMAGE_HEIGHT = 0x806E
GL_TEXTURE_3D = 0x806F
GL_PROXY_TEXTURE_3D = 0x8070
GL_TEXTURE_DEPTH = 0x8071
GL_TEXTURE_WRAP_R = 0x8072
GL_MAX_3D_TEXTURE_SIZE = 0x8073
GL_UNSIGNED_BYTE_2_3_3_REV = 0x8362
GL_UNSIGNED_SHORT_5_6_5 = 0x8363
GL_UNSIGNED_SHORT_5_6_5_REV = 0x8364
GL_UNSIGNED_SHORT_4_4_4_4_REV = 0x8365
GL_UNSIGNED_SHORT_1_5_5_5_REV = 0x8366
GL_UNSIGNED_INT_8_8_8_8_REV = 0x8367
GL_UNSIGNED_INT_2_10_10_10_REV = 0x8368
GL_BGR = 0x80E0
GL_BGRA = 0x80E1
GL_MAX_ELEMENTS_VERTICES = 0x80E8
GL_MAX_ELEMENTS_INDICES = 0x80E9
GL_CLAMP_TO_EDGE = 0x812F
GL_TEXTURE_MIN_LOD = 0x813A
GL_TEXTURE_MAX_LOD = 0x813B
GL_TEXTURE_BASE_LEVEL = 0x813C
GL_TEXTURE_MAX_LEVEL = 0x813D
GL_SMOOTH_POINT_SIZE_RANGE = 0x0B12
GL_SMOOTH_POINT_SIZE_GRANULARITY = 0x0B13
GL_SMOOTH_LINE_WIDTH_RANGE = 0x0B22
GL_SMOOTH_LINE_WIDTH_GRANULARITY = 0x0B23
GL_ALIASED_LINE_WIDTH_RANGE = 0x846E
GL_RESCALE_NORMAL = 0x803A
GL_LIGHT_MODEL_COLOR_CONTROL = 0x81F8
GL_SINGLE_COLOR = 0x81F9
GL_SEPARATE_SPECULAR_COLOR = 0x81FA
GL_ALIASED_POINT_SIZE_RANGE = 0x846D
GL_TEXTURE0 = 0x84C0
GL_TEXTURE1 = 0x84C1
GL_TEXTURE2 = 0x84C2
GL_TEXTURE3 = 0x84C3
GL_TEXTURE4 = 0x84C4
GL_TEXTURE5 = 0x84C5
GL_TEXTURE6 = 0x84C6
GL_TEXTURE7 = 0x84C7
GL_TEXTURE8 = 0x84C8
GL_TEXTURE9 = 0x84C9
GL_TEXTURE10 = 0x84CA
GL_TEXTURE11 = 0x84CB
GL_TEXTURE12 = 0x84CC
GL_TEXTURE13 = 0x84CD
GL_TEXTURE14 = 0x84CE
GL_TEXTURE15 = 0x84CF
GL_TEXTURE16 = 0x84D0
GL_TEXTURE17 = 0x84D1
GL_TEXTURE18 = 0x84D2
GL_TEXTURE19 = 0x84D3
GL_TEXTURE20 = 0x84D4
GL_TEXTURE21 = 0x84D5
GL_TEXTURE22 = 0x84D6
GL_TEXTURE23 = 0x84D7
GL_TEXTURE24 = 0x84D8
GL_TEXTURE25 = 0x84D9
GL_TEXTURE26 = 0x84DA
GL_TEXTURE27 = 0x84DB
GL_TEXTURE28 = 0x84DC
GL_TEXTURE29 = 0x84DD
GL_TEXTURE30 = 0x84DE
GL_TEXTURE31 = 0x84DF
GL_ACTIVE_TEXTURE = 0x84E0
GL_MULTISAMPLE = 0x809D
GL_SAMPLE_ALPHA_TO_COVERAGE = 0x809E
GL_SAMPLE_ALPHA_TO_ONE = 0x809F
GL_SAMPLE_COVERAGE = 0x80A0
GL_SAMPLE_BUFFERS = 0x80A8
GL_SAMPLES = 0x80A9
GL_SAMPLE_COVERAGE_VALUE = 0x80AA
GL_SAMPLE_COVERAGE_INVERT = 0x80AB
GL_TEXTURE_CUBE_MAP = 0x8513
GL_TEXTURE_BINDING_CUBE_MAP = 0x8514
GL_TEXTURE_CUBE_MAP_POSITIVE_X = 0x8515
GL_TEXTURE_CUBE_MAP_NEGATIVE_X = 0x8516
GL_TEXTURE_CUBE_MAP_POSITIVE_Y = 0x8517
GL_TEXTURE_CUBE_MAP_NEGATIVE_Y = 0x8518
GL_TEXTURE_CUBE_MAP_POSITIVE_Z = 0x8519
GL_TEXTURE_CUBE_MAP_NEGATIVE_Z = 0x851A
GL_PROXY_TEXTURE_CUBE_MAP = 0x851B
GL_MAX_CUBE_MAP_TEXTURE_SIZE = 0x851C
GL_COMPRESSED_RGB = 0x84ED
GL_COMPRESSED_RGBA = 0x84EE
GL_TEXTURE_COMPRESSION_HINT = 0x84EF
GL_TEXTURE_COMPRESSED_IMAGE_SIZE = 0x86A0
GL_TEXTURE_COMPRESSED = 0x86A1
GL_NUM_COMPRESSED_TEXTURE_FORMATS = 0x86A2
GL_COMPRESSED_TEXTURE_FORMATS = 0x86A3
GL_CLAMP_TO_BORDER = 0x812D
GL_CLIENT_ACTIVE_TEXTURE = 0x84E1
GL_MAX_TEXTURE_UNITS = 0x84E2
GL_TRANSPOSE_MODELVIEW_MATRIX = 0x84E3
GL_TRANSPOSE_PROJECTION_MATRIX = 0x84E4
GL_TRANSPOSE_TEXTURE_MATRIX = 0x84E5
GL_TRANSPOSE_COLOR_MATRIX = 0x84E6
GL_MULTISAMPLE_BIT = 0x20000000
GL_NORMAL_MAP = 0x8511
GL_REFLECTION_MAP = 0x8512
GL_COMPRESSED_ALPHA = 0x84E9
GL_COMPRESSED_LUMINANCE = 0x84EA
GL_COMPRESSED_LUMINANCE_ALPHA = 0x84EB
GL_COMPRESSED_INTENSITY = 0x84EC
GL_COMBINE = 0x8570
GL_COMBINE_RGB = 0x8571
GL_COMBINE_ALPHA = 0x8572
GL_SOURCE0_RGB = 0x8580
GL_SOURCE1_RGB = 0x8581
GL_SOURCE2_RGB = 0x8582
GL_SOURCE0_ALPHA = 0x8588
GL_SOURCE1_ALPHA = 0x8589
GL_SOURCE2_ALPHA = 0x858A
GL_OPERAND0_RGB = 0x8590
GL_OPERAND1_RGB = 0x8591
GL_OPERAND2_RGB = 0x8592
GL_OPERAND0_ALPHA = 0x8598
GL_OPERAND1_ALPHA = 0x8599
GL_OPERAND2_ALPHA = 0x859A
GL_RGB_SCALE = 0x8573
GL_ADD_SIGNED = 0x8574
GL_INTERPOLATE = 0x8575
GL_SUBTRACT = 0x84E7
GL_CONSTANT = 0x8576
GL_PRIMARY_COLOR = 0x8577
GL_PREVIOUS = 0x8578
GL_DOT3_RGB = 0x86AE
GL_DOT3_RGBA = 0x86AF
GL_BLEND_DST_RGB = 0x80C8
GL_BLEND_SRC_RGB = 0x80C9
GL_BLEND_DST_ALPHA = 0x80CA
GL_BLEND_SRC_ALPHA = 0x80CB
GL_POINT_FADE_THRESHOLD_SIZE = 0x8128
GL_DEPTH_COMPONENT16 = 0x81A5
GL_DEPTH_COMPONENT24 = 0x81A6
GL_DEPTH_COMPONENT32 = 0x81A7
GL_MIRRORED_REPEAT = 0x8370
GL_MAX_TEXTURE_LOD_BIAS = 0x84FD
GL_TEXTURE_LOD_BIAS = 0x8501
GL_INCR_WRAP = 0x8507
GL_DECR_WRAP = 0x8508
GL_TEXTURE_DEPTH_SIZE = 0x884A
GL_TEXTURE_COMPARE_MODE = 0x884C
GL_TEXTURE_COMPARE_FUNC = 0x884D
GL_POINT_SIZE_MIN = 0x8126
GL_POINT_SIZE_MAX = 0x8127
GL_POINT_DISTANCE_ATTENUATION = 0x8129
GL_GENERATE_MIPMAP = 0x8191
GL_GENERATE_MIPMAP_HINT = 0x8192
GL_FOG_COORDINATE_SOURCE = 0x8450
GL_FOG_COORDINATE = 0x8451
GL_FRAGMENT_DEPTH = 0x8452
GL_CURRENT_FOG_COORDINATE = 0x8453
GL_FOG_COORDINATE_ARRAY_TYPE = 0x8454
GL_FOG_COORDINATE_ARRAY_STRIDE = 0x8455
GL_FOG_COORDINATE_ARRAY_POINTER = 0x8456
GL_FOG_COORDINATE_ARRAY = 0x8457
GL_COLOR_SUM = 0x8458
GL_CURRENT_SECONDARY_COLOR = 0x8459
GL_SECONDARY_COLOR_ARRAY_SIZE = 0x845A
GL_SECONDARY_COLOR_ARRAY_TYPE = 0x845B
GL_SECONDARY_COLOR_ARRAY_STRIDE = 0x845C
GL_SECONDARY_COLOR_ARRAY_POINTER = 0x845D
GL_SECONDARY_COLOR_ARRAY = 0x845E
GL_TEXTURE_FILTER_CONTROL = 0x8500
GL_DEPTH_TEXTURE_MODE = 0x884B
GL_COMPARE_R_TO_TEXTURE = 0x884E
GL_FUNC_ADD = 0x8006
GL_FUNC_SUBTRACT = 0x800A
GL_FUNC_REVERSE_SUBTRACT = 0x800B
GL_MIN = 0x8007
GL_MAX = 0x8008
GL_CONSTANT_COLOR = 0x8001
GL_ONE_MINUS_CONSTANT_COLOR = 0x8002
GL_CONSTANT_ALPHA = 0x8003
GL_ONE_MINUS_CONSTANT_ALPHA = 0x8004
GL_BUFFER_SIZE = 0x8764
GL_BUFFER_USAGE = 0x8765
GL_QUERY_COUNTER_BITS = 0x8864
GL_CURRENT_QUERY = 0x8865
GL_QUERY_RESULT = 0x8866
GL_QUERY_RESULT_AVAILABLE = 0x8867
GL_ARRAY_BUFFER = 0x8892
GL_ELEMENT_ARRAY_BUFFER = 0x8893
GL_ARRAY_BUFFER_BINDING = 0x8894
GL_ELEMENT_ARRAY_BUFFER_BINDING = 0x8895
GL_VERTEX_ATTRIB_ARRAY_BUFFER_BINDING = 0x889F
GL_READ_ONLY = 0x88B8
GL_WRITE_ONLY = 0x88B9
GL_READ_WRITE = 0x88BA
GL_BUFFER_ACCESS = 0x88BB
GL_BUFFER_MAPPED = 0x88BC
GL_BUFFER_MAP_POINTER = 0x88BD
GL_STREAM_DRAW = 0x88E0
GL_STREAM_READ = 0x88E1
GL_STREAM_COPY = 0x88E2
GL_STATIC_DRAW = 0x88E4
GL_STATIC_READ = 0x88E5
GL_STATIC_COPY = 0x88E6
GL_DYNAMIC_DRAW = 0x88E8
GL_DYNAMIC_READ = 0x88E9
GL_DYNAMIC_COPY = 0x88EA
GL_SAMPLES_PASSED = 0x8914
GL_SRC1_ALPHA = 0x8589
GL_VERTEX_ARRAY_BUFFER_BINDING = 0x8896
GL_NORMAL_ARRAY_BUFFER_BINDING = 0x8897
GL_COLOR_ARRAY_BUFFER_BINDING = 0x8898
GL_INDEX_ARRAY_BUFFER_BINDING = 0x8899
GL_TEXTURE_COORD_ARRAY_BUFFER_BINDING = 0x889A
GL_EDGE_FLAG_ARRAY_BUFFER_BINDING = 0x889B
GL_SECONDARY_COLOR_ARRAY_BUFFER_BINDING = 0x889C
GL_FOG_COORDINATE_ARRAY_BUFFER_BINDING = 0x889D
GL_WEIGHT_ARRAY_BUFFER_BINDING = 0x889E
GL_FOG_COORD_SRC = 0x8450
GL_FOG_COORD = 0x8451
GL_CURRENT_FOG_COORD = 0x8453
GL_FOG_COORD_ARRAY_TYPE = 0x8454
GL_FOG_COORD_ARRAY_STRIDE = 0x8455
GL_FOG_COORD_ARRAY_POINTER = 0x8456
GL_FOG_COORD_ARRAY = 0x8457
GL_FOG_COORD_ARRAY_BUFFER_BINDING = 0x889D
GL_SRC0_RGB = 0x8580
GL_SRC1_RGB = 0x8581
GL_SRC2_RGB = 0x8582
GL_SRC0_ALPHA = 0x8588
GL_SRC2_ALPHA = 0x858A
GL_BLEND_EQUATION_RGB = 0x8009
GL_VERTEX_ATTRIB_ARRAY_ENABLED = 0x8622
GL_VERTEX_ATTRIB_ARRAY_SIZE = 0x8623
GL_VERTEX_ATTRIB_ARRAY_STRIDE = 0x8624
GL_VERTEX_ATTRIB_ARRAY_TYPE = 0x8625
GL_CURRENT_VERTEX_ATTRIB = 0x8626
GL_VERTEX_PROGRAM_POINT_SIZE = 0x8642
GL_VERTEX_ATTRIB_ARRAY_POINTER = 0x8645
GL_STENCIL_BACK_FUNC = 0x8800
GL_STENCIL_BACK_FAIL = 0x8801
GL_STENCIL_BACK_PASS_DEPTH_FAIL = 0x8802
GL_STENCIL_BACK_PASS_DEPTH_PASS = 0x8803
GL_MAX_DRAW_BUFFERS = 0x8824
GL_DRAW_BUFFER0 = 0x8825
GL_DRAW_BUFFER1 = 0x8826
GL_DRAW_BUFFER2 = 0x8827
GL_DRAW_BUFFER3 = 0x8828
GL_DRAW_BUFFER4 = 0x8829
GL_DRAW_BUFFER5 = 0x882A
GL_DRAW_BUFFER6 = 0x882B
GL_DRAW_BUFFER7 = 0x882C
GL_DRAW_BUFFER8 = 0x882D
GL_DRAW_BUFFER9 = 0x882E
GL_DRAW_BUFFER10 = 0x882F
GL_DRAW_BUFFER11 = 0x8830
GL_DRAW_BUFFER12 = 0x8831
GL_DRAW_BUFFER13 = 0x8832
GL_DRAW_BUFFER14 = 0x8833
GL_DRAW_BUFFER15 = 0x8834
GL_BLEND_EQUATION_ALPHA = 0x883D
GL_MAX_VERTEX_ATTRIBS = 0x8869
GL_VERTEX_ATTRIB_ARRAY_NORMALIZED = 0x886A
GL_MAX_TEXTURE_IMAGE_UNITS = 0x8872
GL_FRAGMENT_SHADER = 0x8B30
GL_VERTEX_SHADER = 0x8B31
GL_MAX_FRAGMENT_UNIFORM_COMPONENTS = 0x8B49
GL_MAX_VERTEX_UNIFORM_COMPONENTS = 0x8B4A
GL_MAX_VARYING_FLOATS = 0x8B4B
GL_MAX_VERTEX_TEXTURE_IMAGE_UNITS = 0x8B4C
GL_MAX_COMBINED_TEXTURE_IMAGE_UNITS = 0x8B4D
GL_SHADER_TYPE = 0x8B4F
GL_FLOAT_VEC2 = 0x8B50
GL_FLOAT_VEC3 = 0x8B51
GL_FLOAT_VEC4 = 0x8B52
GL_INT_VEC2 = 0x8B53
GL_INT_VEC3 = 0x8B54
GL_INT_VEC4 = 0x8B55
GL_BOOL = 0x8B56
GL_BOOL_VEC2 = 0x8B57
GL_BOOL_VEC3 = 0x8B58
GL_BOOL_VEC4 = 0x8B59
GL_FLOAT_MAT2 = 0x8B5A
GL_FLOAT_MAT3 = 0x8B5B
GL_FLOAT_MAT4 = 0x8B5C
GL_SAMPLER_1D = 0x8B5D
GL_SAMPLER_2D = 0x8B5E
GL_SAMPLER_3D = 0x8B5F
GL_SAMPLER_CUBE = 0x8B60
GL_SAMPLER_1D_SHADOW = 0x8B61
GL_SAMPLER_2D_SHADOW = 0x8B62
GL_DELETE_STATUS = 0x8B80
GL_COMPILE_STATUS = 0x8B81
GL_LINK_STATUS = 0x8B82
GL_VALIDATE_STATUS = 0x8B83
GL_INFO_LOG_LENGTH = 0x8B84
GL_ATTACHED_SHADERS = 0x8B85
GL_ACTIVE_UNIFORMS = 0x8B86
GL_ACTIVE_UNIFORM_MAX_LENGTH = 0x8B87
GL_SHADER_SOURCE_LENGTH = 0x8B88
GL_ACTIVE_ATTRIBUTES = 0x8B89
GL_ACTIVE_ATTRIBUTE_MAX_LENGTH = 0x8B8A
GL_FRAGMENT_SHADER_DERIVATIVE_HINT = 0x8B8B
GL_SHADING_LANGUAGE_VERSION = 0x8B8C
GL_CURRENT_PROGRAM = 0x8B8D
GL_POINT_SPRITE_COORD_ORIGIN = 0x8CA0
GL_LOWER_LEFT = 0x8CA1
GL_UPPER_LEFT = 0x8CA2
GL_STENCIL_BACK_REF = 0x8CA3
GL_STENCIL_BACK_VALUE_MASK = 0x8CA4
GL_STENCIL_BACK_WRITEMASK = 0x8CA5
GL_VERTEX_PROGRAM_TWO_SIDE = 0x8643
GL_POINT_SPRITE = 0x8861
GL_COORD_REPLACE = 0x8862
GL_MAX_TEXTURE_COORDS = 0x8871
GL_PIXEL_PACK_BUFFER = 0x88EB
GL_PIXEL_UNPACK_BUFFER = 0x88EC
GL_PIXEL_PACK_BUFFER_BINDING = 0x88ED
GL_PIXEL_UNPACK_BUFFER_BINDING = 0x88EF
GL_FLOAT_MAT2x3 = 0x8B65
GL_FLOAT_MAT2x4 = 0x8B66
GL_FLOAT_MAT3x2 = 0x8B67
GL_FLOAT_MAT3x4 = 0x8B68
GL_FLOAT_MAT4x2 = 0x8B69
GL_FLOAT_MAT4x3 = 0x8B6A
GL_SRGB = 0x8C40
GL_SRGB8 = 0x8C41
GL_SRGB_ALPHA = 0x8C42
GL_SRGB8_ALPHA8 = 0x8C43
GL_COMPRESSED_SRGB = 0x8C48
GL_COMPRESSED_SRGB_ALPHA = 0x8C49
GL_CURRENT_RASTER_SECONDARY_COLOR = 0x845F
GL_SLUMINANCE_ALPHA = 0x8C44
GL_SLUMINANCE8_ALPHA8 = 0x8C45
GL_SLUMINANCE = 0x8C46
GL_SLUMINANCE8 = 0x8C47
GL_COMPRESSED_SLUMINANCE = 0x8C4A
GL_COMPRESSED_SLUMINANCE_ALPHA = 0x8C4B

def __load_GL_VERSION_1_0(loader):
	if glVersion['major'] < 1 or (glVersion['major'] == 1
			and glVersion['minor'] < 0):
		return
	global glCullFace
	glCullFace = _makeFunction(loader('glCullFace'), None, c_uint)
	global glFrontFace
	glFrontFace = _makeFunction(loader('glFrontFace'), None, c_uint)
	global glHint
	glHint = _makeFunction(loader('glHint'), None, c_uint, c_uint)
	global glLineWidth
	glLineWidth = _makeFunction(loader('glLineWidth'), None, c_float)
	global glPointSize
	glPointSize = _makeFunction(loader('glPointSize'), None, c_float)
	global glPolygonMode
	glPolygonMode = _makeFunction(loader('glPolygonMode'), None, c_uint, c_uint)
	global glScissor
	glScissor = _makeFunction(loader('glScissor'), None, c_int, c_int, c_int, c_int)
	global glTexParameterf
	glTexParameterf = _makeFunction(loader('glTexParameterf'), None, c_uint, c_uint, c_float)
	global glTexParameterfv
	glTexParameterfv = _makeFunction(loader('glTexParameterfv'), None, c_uint, c_uint, POINTER(c_float))
	global glTexParameteri
	glTexParameteri = _makeFunction(loader('glTexParameteri'), None, c_uint, c_uint, c_int)
	global glTexParameteriv
	glTexParameteriv = _makeFunction(loader('glTexParameteriv'), None, c_uint, c_uint, POINTER(c_int))
	global glTexImage1D
	glTexImage1D = _makeFunction(loader('glTexImage1D'), None, c_uint, c_int, c_int, c_int, c_int, c_uint, c_uint, c_void_p)
	global glTexImage2D
	glTexImage2D = _makeFunction(loader('glTexImage2D'), None, c_uint, c_int, c_int, c_int, c_int, c_int, c_uint, c_uint, c_void_p)
	global glDrawBuffer
	glDrawBuffer = _makeFunction(loader('glDrawBuffer'), None, c_uint)
	global glClear
	glClear = _makeFunction(loader('glClear'), None, c_uint)
	global glClearColor
	glClearColor = _makeFunction(loader('glClearColor'), None, c_float, c_float, c_float, c_float)
	global glClearStencil
	glClearStencil = _makeFunction(loader('glClearStencil'), None, c_int)
	global glClearDepth
	glClearDepth = _makeFunction(loader('glClearDepth'), None, c_double)
	global glStencilMask
	glStencilMask = _makeFunction(loader('glStencilMask'), None, c_uint)
	global glColorMask
	glColorMask = _makeFunction(loader('glColorMask'), None, c_bool, c_bool, c_bool, c_bool)
	global glDepthMask
	glDepthMask = _makeFunction(loader('glDepthMask'), None, c_bool)
	global glDisable
	glDisable = _makeFunction(loader('glDisable'), None, c_uint)
	global glEnable
	glEnable = _makeFunction(loader('glEnable'), None, c_uint)
	global glFinish
	glFinish = _makeFunction(loader('glFinish'), None)
	global glFlush
	glFlush = _makeFunction(loader('glFlush'), None)
	global glBlendFunc
	glBlendFunc = _makeFunction(loader('glBlendFunc'), None, c_uint, c_uint)
	global glLogicOp
	glLogicOp = _makeFunction(loader('glLogicOp'), None, c_uint)
	global glStencilFunc
	glStencilFunc = _makeFunction(loader('glStencilFunc'), None, c_uint, c_int, c_uint)
	global glStencilOp
	glStencilOp = _makeFunction(loader('glStencilOp'), None, c_uint, c_uint, c_uint)
	global glDepthFunc
	glDepthFunc = _makeFunction(loader('glDepthFunc'), None, c_uint)
	global glPixelStoref
	glPixelStoref = _makeFunction(loader('glPixelStoref'), None, c_uint, c_float)
	global glPixelStorei
	glPixelStorei = _makeFunction(loader('glPixelStorei'), None, c_uint, c_int)
	global glReadBuffer
	glReadBuffer = _makeFunction(loader('glReadBuffer'), None, c_uint)
	global glReadPixels
	glReadPixels = _makeFunction(loader('glReadPixels'), None, c_int, c_int, c_int, c_int, c_uint, c_uint, c_void_p)
	global glGetBooleanv
	glGetBooleanv = _makeFunction(loader('glGetBooleanv'), None, c_uint, POINTER(c_bool))
	global glGetDoublev
	glGetDoublev = _makeFunction(loader('glGetDoublev'), None, c_uint, POINTER(c_double))
	global glGetError
	glGetError = _makeFunction(loader('glGetError'), c_uint)
	global glGetFloatv
	glGetFloatv = _makeFunction(loader('glGetFloatv'), None, c_uint, POINTER(c_float))
	global glGetIntegerv
	glGetIntegerv = _makeFunction(loader('glGetIntegerv'), None, c_uint, POINTER(c_int))
	global glGetString
	glGetString = _makeFunction(loader('glGetString'), POINTER(c_ubyte), c_uint)
	global glGetTexImage
	glGetTexImage = _makeFunction(loader('glGetTexImage'), None, c_uint, c_int, c_uint, c_uint, c_void_p)
	global glGetTexParameterfv
	glGetTexParameterfv = _makeFunction(loader('glGetTexParameterfv'), None, c_uint, c_uint, POINTER(c_float))
	global glGetTexParameteriv
	glGetTexParameteriv = _makeFunction(loader('glGetTexParameteriv'), None, c_uint, c_uint, POINTER(c_int))
	global glGetTexLevelParameterfv
	glGetTexLevelParameterfv = _makeFunction(loader('glGetTexLevelParameterfv'), None, c_uint, c_int, c_uint, POINTER(c_float))
	global glGetTexLevelParameteriv
	glGetTexLevelParameteriv = _makeFunction(loader('glGetTexLevelParameteriv'), None, c_uint, c_int, c_uint, POINTER(c_int))
	global glIsEnabled
	glIsEnabled = _makeFunction(loader('glIsEnabled'), c_bool, c_uint)
	global glDepthRange
	glDepthRange = _makeFunction(loader('glDepthRange'), None, c_double, c_double)
	global glViewport
	glViewport = _makeFunction(loader('glViewport'), None, c_int, c_int, c_int, c_int)
	global glNewList
	glNewList = _makeFunction(loader('glNewList'), None, c_uint, c_uint)
	global glEndList
	glEndList = _makeFunction(loader('glEndList'), None)
	global glCallList
	glCallList = _makeFunction(loader('glCallList'), None, c_uint)
	global glCallLists
	glCallLists = _makeFunction(loader('glCallLists'), None, c_int, c_uint, c_void_p)
	global glDeleteLists
	glDeleteLists = _makeFunction(loader('glDeleteLists'), None, c_uint, c_int)
	global glGenLists
	glGenLists = _makeFunction(loader('glGenLists'), c_uint, c_int)
	global glListBase
	glListBase = _makeFunction(loader('glListBase'), None, c_uint)
	global glBegin
	glBegin = _makeFunction(loader('glBegin'), None, c_uint)
	global glBitmap
	glBitmap = _makeFunction(loader('glBitmap'), None, c_int, c_int, c_float, c_float, c_float, c_float, POINTER(c_ubyte))
	global glColor3b
	glColor3b = _makeFunction(loader('glColor3b'), None, c_byte, c_byte, c_byte)
	global glColor3bv
	glColor3bv = _makeFunction(loader('glColor3bv'), None, POINTER(c_byte))
	global glColor3d
	glColor3d = _makeFunction(loader('glColor3d'), None, c_double, c_double, c_double)
	global glColor3dv
	glColor3dv = _makeFunction(loader('glColor3dv'), None, POINTER(c_double))
	global glColor3f
	glColor3f = _makeFunction(loader('glColor3f'), None, c_float, c_float, c_float)
	global glColor3fv
	glColor3fv = _makeFunction(loader('glColor3fv'), None, POINTER(c_float))
	global glColor3i
	glColor3i = _makeFunction(loader('glColor3i'), None, c_int, c_int, c_int)
	global glColor3iv
	glColor3iv = _makeFunction(loader('glColor3iv'), None, POINTER(c_int))
	global glColor3s
	glColor3s = _makeFunction(loader('glColor3s'), None, c_short, c_short, c_short)
	global glColor3sv
	glColor3sv = _makeFunction(loader('glColor3sv'), None, POINTER(c_short))
	global glColor3ub
	glColor3ub = _makeFunction(loader('glColor3ub'), None, c_ubyte, c_ubyte, c_ubyte)
	global glColor3ubv
	glColor3ubv = _makeFunction(loader('glColor3ubv'), None, POINTER(c_ubyte))
	global glColor3ui
	glColor3ui = _makeFunction(loader('glColor3ui'), None, c_uint, c_uint, c_uint)
	global glColor3uiv
	glColor3uiv = _makeFunction(loader('glColor3uiv'), None, POINTER(c_uint))
	global glColor3us
	glColor3us = _makeFunction(loader('glColor3us'), None, c_ushort, c_ushort, c_ushort)
	global glColor3usv
	glColor3usv = _makeFunction(loader('glColor3usv'), None, POINTER(c_ushort))
	global glColor4b
	glColor4b = _makeFunction(loader('glColor4b'), None, c_byte, c_byte, c_byte, c_byte)
	global glColor4bv
	glColor4bv = _makeFunction(loader('glColor4bv'), None, POINTER(c_byte))
	global glColor4d
	glColor4d = _makeFunction(loader('glColor4d'), None, c_double, c_double, c_double, c_double)
	global glColor4dv
	glColor4dv = _makeFunction(loader('glColor4dv'), None, POINTER(c_double))
	global glColor4f
	glColor4f = _makeFunction(loader('glColor4f'), None, c_float, c_float, c_float, c_float)
	global glColor4fv
	glColor4fv = _makeFunction(loader('glColor4fv'), None, POINTER(c_float))
	global glColor4i
	glColor4i = _makeFunction(loader('glColor4i'), None, c_int, c_int, c_int, c_int)
	global glColor4iv
	glColor4iv = _makeFunction(loader('glColor4iv'), None, POINTER(c_int))
	global glColor4s
	glColor4s = _makeFunction(loader('glColor4s'), None, c_short, c_short, c_short, c_short)
	global glColor4sv
	glColor4sv = _makeFunction(loader('glColor4sv'), None, POINTER(c_short))
	global glColor4ub
	glColor4ub = _makeFunction(loader('glColor4ub'), None, c_ubyte, c_ubyte, c_ubyte, c_ubyte)
	global glColor4ubv
	glColor4ubv = _makeFunction(loader('glColor4ubv'), None, POINTER(c_ubyte))
	global glColor4ui
	glColor4ui = _makeFunction(loader('glColor4ui'), None, c_uint, c_uint, c_uint, c_uint)
	global glColor4uiv
	glColor4uiv = _makeFunction(loader('glColor4uiv'), None, POINTER(c_uint))
	global glColor4us
	glColor4us = _makeFunction(loader('glColor4us'), None, c_ushort, c_ushort, c_ushort, c_ushort)
	global glColor4usv
	glColor4usv = _makeFunction(loader('glColor4usv'), None, POINTER(c_ushort))
	global glEdgeFlag
	glEdgeFlag = _makeFunction(loader('glEdgeFlag'), None, c_bool)
	global glEdgeFlagv
	glEdgeFlagv = _makeFunction(loader('glEdgeFlagv'), None, POINTER(c_bool))
	global glEnd
	glEnd = _makeFunction(loader('glEnd'), None)
	global glIndexd
	glIndexd = _makeFunction(loader('glIndexd'), None, c_double)
	global glIndexdv
	glIndexdv = _makeFunction(loader('glIndexdv'), None, POINTER(c_double))
	global glIndexf
	glIndexf = _makeFunction(loader('glIndexf'), None, c_float)
	global glIndexfv
	glIndexfv = _makeFunction(loader('glIndexfv'), None, POINTER(c_float))
	global glIndexi
	glIndexi = _makeFunction(loader('glIndexi'), None, c_int)
	global glIndexiv
	glIndexiv = _makeFunction(loader('glIndexiv'), None, POINTER(c_int))
	global glIndexs
	glIndexs = _makeFunction(loader('glIndexs'), None, c_short)
	global glIndexsv
	glIndexsv = _makeFunction(loader('glIndexsv'), None, POINTER(c_short))
	global glNormal3b
	glNormal3b = _makeFunction(loader('glNormal3b'), None, c_byte, c_byte, c_byte)
	global glNormal3bv
	glNormal3bv = _makeFunction(loader('glNormal3bv'), None, POINTER(c_byte))
	global glNormal3d
	glNormal3d = _makeFunction(loader('glNormal3d'), None, c_double, c_double, c_double)
	global glNormal3dv
	glNormal3dv = _makeFunction(loader('glNormal3dv'), None, POINTER(c_double))
	global glNormal3f
	glNormal3f = _makeFunction(loader('glNormal3f'), None, c_float, c_float, c_float)
	global glNormal3fv
	glNormal3fv = _makeFunction(loader('glNormal3fv'), None, POINTER(c_float))
	global glNormal3i
	glNormal3i = _makeFunction(loader('glNormal3i'), None, c_int, c_int, c_int)
	global glNormal3iv
	glNormal3iv = _makeFunction(loader('glNormal3iv'), None, POINTER(c_int))
	global glNormal3s
	glNormal3s = _makeFunction(loader('glNormal3s'), None, c_short, c_short, c_short)
	global glNormal3sv
	glNormal3sv = _makeFunction(loader('glNormal3sv'), None, POINTER(c_short))
	global glRasterPos2d
	glRasterPos2d = _makeFunction(loader('glRasterPos2d'), None, c_double, c_double)
	global glRasterPos2dv
	glRasterPos2dv = _makeFunction(loader('glRasterPos2dv'), None, POINTER(c_double))
	global glRasterPos2f
	glRasterPos2f = _makeFunction(loader('glRasterPos2f'), None, c_float, c_float)
	global glRasterPos2fv
	glRasterPos2fv = _makeFunction(loader('glRasterPos2fv'), None, POINTER(c_float))
	global glRasterPos2i
	glRasterPos2i = _makeFunction(loader('glRasterPos2i'), None, c_int, c_int)
	global glRasterPos2iv
	glRasterPos2iv = _makeFunction(loader('glRasterPos2iv'), None, POINTER(c_int))
	global glRasterPos2s
	glRasterPos2s = _makeFunction(loader('glRasterPos2s'), None, c_short, c_short)
	global glRasterPos2sv
	glRasterPos2sv = _makeFunction(loader('glRasterPos2sv'), None, POINTER(c_short))
	global glRasterPos3d
	glRasterPos3d = _makeFunction(loader('glRasterPos3d'), None, c_double, c_double, c_double)
	global glRasterPos3dv
	glRasterPos3dv = _makeFunction(loader('glRasterPos3dv'), None, POINTER(c_double))
	global glRasterPos3f
	glRasterPos3f = _makeFunction(loader('glRasterPos3f'), None, c_float, c_float, c_float)
	global glRasterPos3fv
	glRasterPos3fv = _makeFunction(loader('glRasterPos3fv'), None, POINTER(c_float))
	global glRasterPos3i
	glRasterPos3i = _makeFunction(loader('glRasterPos3i'), None, c_int, c_int, c_int)
	global glRasterPos3iv
	glRasterPos3iv = _makeFunction(loader('glRasterPos3iv'), None, POINTER(c_int))
	global glRasterPos3s
	glRasterPos3s = _makeFunction(loader('glRasterPos3s'), None, c_short, c_short, c_short)
	global glRasterPos3sv
	glRasterPos3sv = _makeFunction(loader('glRasterPos3sv'), None, POINTER(c_short))
	global glRasterPos4d
	glRasterPos4d = _makeFunction(loader('glRasterPos4d'), None, c_double, c_double, c_double, c_double)
	global glRasterPos4dv
	glRasterPos4dv = _makeFunction(loader('glRasterPos4dv'), None, POINTER(c_double))
	global glRasterPos4f
	glRasterPos4f = _makeFunction(loader('glRasterPos4f'), None, c_float, c_float, c_float, c_float)
	global glRasterPos4fv
	glRasterPos4fv = _makeFunction(loader('glRasterPos4fv'), None, POINTER(c_float))
	global glRasterPos4i
	glRasterPos4i = _makeFunction(loader('glRasterPos4i'), None, c_int, c_int, c_int, c_int)
	global glRasterPos4iv
	glRasterPos4iv = _makeFunction(loader('glRasterPos4iv'), None, POINTER(c_int))
	global glRasterPos4s
	glRasterPos4s = _makeFunction(loader('glRasterPos4s'), None, c_short, c_short, c_short, c_short)
	global glRasterPos4sv
	glRasterPos4sv = _makeFunction(loader('glRasterPos4sv'), None, POINTER(c_short))
	global glRectd
	glRectd = _makeFunction(loader('glRectd'), None, c_double, c_double, c_double, c_double)
	global glRectdv
	glRectdv = _makeFunction(loader('glRectdv'), None, POINTER(c_double), POINTER(c_double))
	global glRectf
	glRectf = _makeFunction(loader('glRectf'), None, c_float, c_float, c_float, c_float)
	global glRectfv
	glRectfv = _makeFunction(loader('glRectfv'), None, POINTER(c_float), POINTER(c_float))
	global glRecti
	glRecti = _makeFunction(loader('glRecti'), None, c_int, c_int, c_int, c_int)
	global glRectiv
	glRectiv = _makeFunction(loader('glRectiv'), None, POINTER(c_int), POINTER(c_int))
	global glRects
	glRects = _makeFunction(loader('glRects'), None, c_short, c_short, c_short, c_short)
	global glRectsv
	glRectsv = _makeFunction(loader('glRectsv'), None, POINTER(c_short), POINTER(c_short))
	global glTexCoord1d
	glTexCoord1d = _makeFunction(loader('glTexCoord1d'), None, c_double)
	global glTexCoord1dv
	glTexCoord1dv = _makeFunction(loader('glTexCoord1dv'), None, POINTER(c_double))
	global glTexCoord1f
	glTexCoord1f = _makeFunction(loader('glTexCoord1f'), None, c_float)
	global glTexCoord1fv
	glTexCoord1fv = _makeFunction(loader('glTexCoord1fv'), None, POINTER(c_float))
	global glTexCoord1i
	glTexCoord1i = _makeFunction(loader('glTexCoord1i'), None, c_int)
	global glTexCoord1iv
	glTexCoord1iv = _makeFunction(loader('glTexCoord1iv'), None, POINTER(c_int))
	global glTexCoord1s
	glTexCoord1s = _makeFunction(loader('glTexCoord1s'), None, c_short)
	global glTexCoord1sv
	glTexCoord1sv = _makeFunction(loader('glTexCoord1sv'), None, POINTER(c_short))
	global glTexCoord2d
	glTexCoord2d = _makeFunction(loader('glTexCoord2d'), None, c_double, c_double)
	global glTexCoord2dv
	glTexCoord2dv = _makeFunction(loader('glTexCoord2dv'), None, POINTER(c_double))
	global glTexCoord2f
	glTexCoord2f = _makeFunction(loader('glTexCoord2f'), None, c_float, c_float)
	global glTexCoord2fv
	glTexCoord2fv = _makeFunction(loader('glTexCoord2fv'), None, POINTER(c_float))
	global glTexCoord2i
	glTexCoord2i = _makeFunction(loader('glTexCoord2i'), None, c_int, c_int)
	global glTexCoord2iv
	glTexCoord2iv = _makeFunction(loader('glTexCoord2iv'), None, POINTER(c_int))
	global glTexCoord2s
	glTexCoord2s = _makeFunction(loader('glTexCoord2s'), None, c_short, c_short)
	global glTexCoord2sv
	glTexCoord2sv = _makeFunction(loader('glTexCoord2sv'), None, POINTER(c_short))
	global glTexCoord3d
	glTexCoord3d = _makeFunction(loader('glTexCoord3d'), None, c_double, c_double, c_double)
	global glTexCoord3dv
	glTexCoord3dv = _makeFunction(loader('glTexCoord3dv'), None, POINTER(c_double))
	global glTexCoord3f
	glTexCoord3f = _makeFunction(loader('glTexCoord3f'), None, c_float, c_float, c_float)
	global glTexCoord3fv
	glTexCoord3fv = _makeFunction(loader('glTexCoord3fv'), None, POINTER(c_float))
	global glTexCoord3i
	glTexCoord3i = _makeFunction(loader('glTexCoord3i'), None, c_int, c_int, c_int)
	global glTexCoord3iv
	glTexCoord3iv = _makeFunction(loader('glTexCoord3iv'), None, POINTER(c_int))
	global glTexCoord3s
	glTexCoord3s = _makeFunction(loader('glTexCoord3s'), None, c_short, c_short, c_short)
	global glTexCoord3sv
	glTexCoord3sv = _makeFunction(loader('glTexCoord3sv'), None, POINTER(c_short))
	global glTexCoord4d
	glTexCoord4d = _makeFunction(loader('glTexCoord4d'), None, c_double, c_double, c_double, c_double)
	global glTexCoord4dv
	glTexCoord4dv = _makeFunction(loader('glTexCoord4dv'), None, POINTER(c_double))
	global glTexCoord4f
	glTexCoord4f = _makeFunction(loader('glTexCoord4f'), None, c_float, c_float, c_float, c_float)
	global glTexCoord4fv
	glTexCoord4fv = _makeFunction(loader('glTexCoord4fv'), None, POINTER(c_float))
	global glTexCoord4i
	glTexCoord4i = _makeFunction(loader('glTexCoord4i'), None, c_int, c_int, c_int, c_int)
	global glTexCoord4iv
	glTexCoord4iv = _makeFunction(loader('glTexCoord4iv'), None, POINTER(c_int))
	global glTexCoord4s
	glTexCoord4s = _makeFunction(loader('glTexCoord4s'), None, c_short, c_short, c_short, c_short)
	global glTexCoord4sv
	glTexCoord4sv = _makeFunction(loader('glTexCoord4sv'), None, POINTER(c_short))
	global glVertex2d
	glVertex2d = _makeFunction(loader('glVertex2d'), None, c_double, c_double)
	global glVertex2dv
	glVertex2dv = _makeFunction(loader('glVertex2dv'), None, POINTER(c_double))
	global glVertex2f
	glVertex2f = _makeFunction(loader('glVertex2f'), None, c_float, c_float)
	global glVertex2fv
	glVertex2fv = _makeFunction(loader('glVertex2fv'), None, POINTER(c_float))
	global glVertex2i
	glVertex2i = _makeFunction(loader('glVertex2i'), None, c_int, c_int)
	global glVertex2iv
	glVertex2iv = _makeFunction(loader('glVertex2iv'), None, POINTER(c_int))
	global glVertex2s
	glVertex2s = _makeFunction(loader('glVertex2s'), None, c_short, c_short)
	global glVertex2sv
	glVertex2sv = _makeFunction(loader('glVertex2sv'), None, POINTER(c_short))
	global glVertex3d
	glVertex3d = _makeFunction(loader('glVertex3d'), None, c_double, c_double, c_double)
	global glVertex3dv
	glVertex3dv = _makeFunction(loader('glVertex3dv'), None, POINTER(c_double))
	global glVertex3f
	glVertex3f = _makeFunction(loader('glVertex3f'), None, c_float, c_float, c_float)
	global glVertex3fv
	glVertex3fv = _makeFunction(loader('glVertex3fv'), None, POINTER(c_float))
	global glVertex3i
	glVertex3i = _makeFunction(loader('glVertex3i'), None, c_int, c_int, c_int)
	global glVertex3iv
	glVertex3iv = _makeFunction(loader('glVertex3iv'), None, POINTER(c_int))
	global glVertex3s
	glVertex3s = _makeFunction(loader('glVertex3s'), None, c_short, c_short, c_short)
	global glVertex3sv
	glVertex3sv = _makeFunction(loader('glVertex3sv'), None, POINTER(c_short))
	global glVertex4d
	glVertex4d = _makeFunction(loader('glVertex4d'), None, c_double, c_double, c_double, c_double)
	global glVertex4dv
	glVertex4dv = _makeFunction(loader('glVertex4dv'), None, POINTER(c_double))
	global glVertex4f
	glVertex4f = _makeFunction(loader('glVertex4f'), None, c_float, c_float, c_float, c_float)
	global glVertex4fv
	glVertex4fv = _makeFunction(loader('glVertex4fv'), None, POINTER(c_float))
	global glVertex4i
	glVertex4i = _makeFunction(loader('glVertex4i'), None, c_int, c_int, c_int, c_int)
	global glVertex4iv
	glVertex4iv = _makeFunction(loader('glVertex4iv'), None, POINTER(c_int))
	global glVertex4s
	glVertex4s = _makeFunction(loader('glVertex4s'), None, c_short, c_short, c_short, c_short)
	global glVertex4sv
	glVertex4sv = _makeFunction(loader('glVertex4sv'), None, POINTER(c_short))
	global glClipPlane
	glClipPlane = _makeFunction(loader('glClipPlane'), None, c_uint, POINTER(c_double))
	global glColorMaterial
	glColorMaterial = _makeFunction(loader('glColorMaterial'), None, c_uint, c_uint)
	global glFogf
	glFogf = _makeFunction(loader('glFogf'), None, c_uint, c_float)
	global glFogfv
	glFogfv = _makeFunction(loader('glFogfv'), None, c_uint, POINTER(c_float))
	global glFogi
	glFogi = _makeFunction(loader('glFogi'), None, c_uint, c_int)
	global glFogiv
	glFogiv = _makeFunction(loader('glFogiv'), None, c_uint, POINTER(c_int))
	global glLightf
	glLightf = _makeFunction(loader('glLightf'), None, c_uint, c_uint, c_float)
	global glLightfv
	glLightfv = _makeFunction(loader('glLightfv'), None, c_uint, c_uint, POINTER(c_float))
	global glLighti
	glLighti = _makeFunction(loader('glLighti'), None, c_uint, c_uint, c_int)
	global glLightiv
	glLightiv = _makeFunction(loader('glLightiv'), None, c_uint, c_uint, POINTER(c_int))
	global glLightModelf
	glLightModelf = _makeFunction(loader('glLightModelf'), None, c_uint, c_float)
	global glLightModelfv
	glLightModelfv = _makeFunction(loader('glLightModelfv'), None, c_uint, POINTER(c_float))
	global glLightModeli
	glLightModeli = _makeFunction(loader('glLightModeli'), None, c_uint, c_int)
	global glLightModeliv
	glLightModeliv = _makeFunction(loader('glLightModeliv'), None, c_uint, POINTER(c_int))
	global glLineStipple
	glLineStipple = _makeFunction(loader('glLineStipple'), None, c_int, c_ushort)
	global glMaterialf
	glMaterialf = _makeFunction(loader('glMaterialf'), None, c_uint, c_uint, c_float)
	global glMaterialfv
	glMaterialfv = _makeFunction(loader('glMaterialfv'), None, c_uint, c_uint, POINTER(c_float))
	global glMateriali
	glMateriali = _makeFunction(loader('glMateriali'), None, c_uint, c_uint, c_int)
	global glMaterialiv
	glMaterialiv = _makeFunction(loader('glMaterialiv'), None, c_uint, c_uint, POINTER(c_int))
	global glPolygonStipple
	glPolygonStipple = _makeFunction(loader('glPolygonStipple'), None, POINTER(c_ubyte))
	global glShadeModel
	glShadeModel = _makeFunction(loader('glShadeModel'), None, c_uint)
	global glTexEnvf
	glTexEnvf = _makeFunction(loader('glTexEnvf'), None, c_uint, c_uint, c_float)
	global glTexEnvfv
	glTexEnvfv = _makeFunction(loader('glTexEnvfv'), None, c_uint, c_uint, POINTER(c_float))
	global glTexEnvi
	glTexEnvi = _makeFunction(loader('glTexEnvi'), None, c_uint, c_uint, c_int)
	global glTexEnviv
	glTexEnviv = _makeFunction(loader('glTexEnviv'), None, c_uint, c_uint, POINTER(c_int))
	global glTexGend
	glTexGend = _makeFunction(loader('glTexGend'), None, c_uint, c_uint, c_double)
	global glTexGendv
	glTexGendv = _makeFunction(loader('glTexGendv'), None, c_uint, c_uint, POINTER(c_double))
	global glTexGenf
	glTexGenf = _makeFunction(loader('glTexGenf'), None, c_uint, c_uint, c_float)
	global glTexGenfv
	glTexGenfv = _makeFunction(loader('glTexGenfv'), None, c_uint, c_uint, POINTER(c_float))
	global glTexGeni
	glTexGeni = _makeFunction(loader('glTexGeni'), None, c_uint, c_uint, c_int)
	global glTexGeniv
	glTexGeniv = _makeFunction(loader('glTexGeniv'), None, c_uint, c_uint, POINTER(c_int))
	global glFeedbackBuffer
	glFeedbackBuffer = _makeFunction(loader('glFeedbackBuffer'), None, c_int, c_uint, POINTER(c_float))
	global glSelectBuffer
	glSelectBuffer = _makeFunction(loader('glSelectBuffer'), None, c_int, POINTER(c_uint))
	global glRenderMode
	glRenderMode = _makeFunction(loader('glRenderMode'), c_int, c_uint)
	global glInitNames
	glInitNames = _makeFunction(loader('glInitNames'), None)
	global glLoadName
	glLoadName = _makeFunction(loader('glLoadName'), None, c_uint)
	global glPassThrough
	glPassThrough = _makeFunction(loader('glPassThrough'), None, c_float)
	global glPopName
	glPopName = _makeFunction(loader('glPopName'), None)
	global glPushName
	glPushName = _makeFunction(loader('glPushName'), None, c_uint)
	global glClearAccum
	glClearAccum = _makeFunction(loader('glClearAccum'), None, c_float, c_float, c_float, c_float)
	global glClearIndex
	glClearIndex = _makeFunction(loader('glClearIndex'), None, c_float)
	global glIndexMask
	glIndexMask = _makeFunction(loader('glIndexMask'), None, c_uint)
	global glAccum
	glAccum = _makeFunction(loader('glAccum'), None, c_uint, c_float)
	global glPopAttrib
	glPopAttrib = _makeFunction(loader('glPopAttrib'), None)
	global glPushAttrib
	glPushAttrib = _makeFunction(loader('glPushAttrib'), None, c_uint)
	global glMap1d
	glMap1d = _makeFunction(loader('glMap1d'), None, c_uint, c_double, c_double, c_int, c_int, POINTER(c_double))
	global glMap1f
	glMap1f = _makeFunction(loader('glMap1f'), None, c_uint, c_float, c_float, c_int, c_int, POINTER(c_float))
	global glMap2d
	glMap2d = _makeFunction(loader('glMap2d'), None, c_uint, c_double, c_double, c_int, c_int, c_double, c_double, c_int, c_int, POINTER(c_double))
	global glMap2f
	glMap2f = _makeFunction(loader('glMap2f'), None, c_uint, c_float, c_float, c_int, c_int, c_float, c_float, c_int, c_int, POINTER(c_float))
	global glMapGrid1d
	glMapGrid1d = _makeFunction(loader('glMapGrid1d'), None, c_int, c_double, c_double)
	global glMapGrid1f
	glMapGrid1f = _makeFunction(loader('glMapGrid1f'), None, c_int, c_float, c_float)
	global glMapGrid2d
	glMapGrid2d = _makeFunction(loader('glMapGrid2d'), None, c_int, c_double, c_double, c_int, c_double, c_double)
	global glMapGrid2f
	glMapGrid2f = _makeFunction(loader('glMapGrid2f'), None, c_int, c_float, c_float, c_int, c_float, c_float)
	global glEvalCoord1d
	glEvalCoord1d = _makeFunction(loader('glEvalCoord1d'), None, c_double)
	global glEvalCoord1dv
	glEvalCoord1dv = _makeFunction(loader('glEvalCoord1dv'), None, POINTER(c_double))
	global glEvalCoord1f
	glEvalCoord1f = _makeFunction(loader('glEvalCoord1f'), None, c_float)
	global glEvalCoord1fv
	glEvalCoord1fv = _makeFunction(loader('glEvalCoord1fv'), None, POINTER(c_float))
	global glEvalCoord2d
	glEvalCoord2d = _makeFunction(loader('glEvalCoord2d'), None, c_double, c_double)
	global glEvalCoord2dv
	glEvalCoord2dv = _makeFunction(loader('glEvalCoord2dv'), None, POINTER(c_double))
	global glEvalCoord2f
	glEvalCoord2f = _makeFunction(loader('glEvalCoord2f'), None, c_float, c_float)
	global glEvalCoord2fv
	glEvalCoord2fv = _makeFunction(loader('glEvalCoord2fv'), None, POINTER(c_float))
	global glEvalMesh1
	glEvalMesh1 = _makeFunction(loader('glEvalMesh1'), None, c_uint, c_int, c_int)
	global glEvalPoint1
	glEvalPoint1 = _makeFunction(loader('glEvalPoint1'), None, c_int)
	global glEvalMesh2
	glEvalMesh2 = _makeFunction(loader('glEvalMesh2'), None, c_uint, c_int, c_int, c_int, c_int)
	global glEvalPoint2
	glEvalPoint2 = _makeFunction(loader('glEvalPoint2'), None, c_int, c_int)
	global glAlphaFunc
	glAlphaFunc = _makeFunction(loader('glAlphaFunc'), None, c_uint, c_float)
	global glPixelZoom
	glPixelZoom = _makeFunction(loader('glPixelZoom'), None, c_float, c_float)
	global glPixelTransferf
	glPixelTransferf = _makeFunction(loader('glPixelTransferf'), None, c_uint, c_float)
	global glPixelTransferi
	glPixelTransferi = _makeFunction(loader('glPixelTransferi'), None, c_uint, c_int)
	global glPixelMapfv
	glPixelMapfv = _makeFunction(loader('glPixelMapfv'), None, c_uint, c_int, POINTER(c_float))
	global glPixelMapuiv
	glPixelMapuiv = _makeFunction(loader('glPixelMapuiv'), None, c_uint, c_int, POINTER(c_uint))
	global glPixelMapusv
	glPixelMapusv = _makeFunction(loader('glPixelMapusv'), None, c_uint, c_int, POINTER(c_ushort))
	global glCopyPixels
	glCopyPixels = _makeFunction(loader('glCopyPixels'), None, c_int, c_int, c_int, c_int, c_uint)
	global glDrawPixels
	glDrawPixels = _makeFunction(loader('glDrawPixels'), None, c_int, c_int, c_uint, c_uint, c_void_p)
	global glGetClipPlane
	glGetClipPlane = _makeFunction(loader('glGetClipPlane'), None, c_uint, POINTER(c_double))
	global glGetLightfv
	glGetLightfv = _makeFunction(loader('glGetLightfv'), None, c_uint, c_uint, POINTER(c_float))
	global glGetLightiv
	glGetLightiv = _makeFunction(loader('glGetLightiv'), None, c_uint, c_uint, POINTER(c_int))
	global glGetMapdv
	glGetMapdv = _makeFunction(loader('glGetMapdv'), None, c_uint, c_uint, POINTER(c_double))
	global glGetMapfv
	glGetMapfv = _makeFunction(loader('glGetMapfv'), None, c_uint, c_uint, POINTER(c_float))
	global glGetMapiv
	glGetMapiv = _makeFunction(loader('glGetMapiv'), None, c_uint, c_uint, POINTER(c_int))
	global glGetMaterialfv
	glGetMaterialfv = _makeFunction(loader('glGetMaterialfv'), None, c_uint, c_uint, POINTER(c_float))
	global glGetMaterialiv
	glGetMaterialiv = _makeFunction(loader('glGetMaterialiv'), None, c_uint, c_uint, POINTER(c_int))
	global glGetPixelMapfv
	glGetPixelMapfv = _makeFunction(loader('glGetPixelMapfv'), None, c_uint, POINTER(c_float))
	global glGetPixelMapuiv
	glGetPixelMapuiv = _makeFunction(loader('glGetPixelMapuiv'), None, c_uint, POINTER(c_uint))
	global glGetPixelMapusv
	glGetPixelMapusv = _makeFunction(loader('glGetPixelMapusv'), None, c_uint, POINTER(c_ushort))
	global glGetPolygonStipple
	glGetPolygonStipple = _makeFunction(loader('glGetPolygonStipple'), None, POINTER(c_ubyte))
	global glGetTexEnvfv
	glGetTexEnvfv = _makeFunction(loader('glGetTexEnvfv'), None, c_uint, c_uint, POINTER(c_float))
	global glGetTexEnviv
	glGetTexEnviv = _makeFunction(loader('glGetTexEnviv'), None, c_uint, c_uint, POINTER(c_int))
	global glGetTexGendv
	glGetTexGendv = _makeFunction(loader('glGetTexGendv'), None, c_uint, c_uint, POINTER(c_double))
	global glGetTexGenfv
	glGetTexGenfv = _makeFunction(loader('glGetTexGenfv'), None, c_uint, c_uint, POINTER(c_float))
	global glGetTexGeniv
	glGetTexGeniv = _makeFunction(loader('glGetTexGeniv'), None, c_uint, c_uint, POINTER(c_int))
	global glIsList
	glIsList = _makeFunction(loader('glIsList'), c_bool, c_uint)
	global glFrustum
	glFrustum = _makeFunction(loader('glFrustum'), None, c_double, c_double, c_double, c_double, c_double, c_double)
	global glLoadIdentity
	glLoadIdentity = _makeFunction(loader('glLoadIdentity'), None)
	global glLoadMatrixf
	glLoadMatrixf = _makeFunction(loader('glLoadMatrixf'), None, POINTER(c_float))
	global glLoadMatrixd
	glLoadMatrixd = _makeFunction(loader('glLoadMatrixd'), None, POINTER(c_double))
	global glMatrixMode
	glMatrixMode = _makeFunction(loader('glMatrixMode'), None, c_uint)
	global glMultMatrixf
	glMultMatrixf = _makeFunction(loader('glMultMatrixf'), None, POINTER(c_float))
	global glMultMatrixd
	glMultMatrixd = _makeFunction(loader('glMultMatrixd'), None, POINTER(c_double))
	global glOrtho
	glOrtho = _makeFunction(loader('glOrtho'), None, c_double, c_double, c_double, c_double, c_double, c_double)
	global glPopMatrix
	glPopMatrix = _makeFunction(loader('glPopMatrix'), None)
	global glPushMatrix
	glPushMatrix = _makeFunction(loader('glPushMatrix'), None)
	global glRotated
	glRotated = _makeFunction(loader('glRotated'), None, c_double, c_double, c_double, c_double)
	global glRotatef
	glRotatef = _makeFunction(loader('glRotatef'), None, c_float, c_float, c_float, c_float)
	global glScaled
	glScaled = _makeFunction(loader('glScaled'), None, c_double, c_double, c_double)
	global glScalef
	glScalef = _makeFunction(loader('glScalef'), None, c_float, c_float, c_float)
	global glTranslated
	glTranslated = _makeFunction(loader('glTranslated'), None, c_double, c_double, c_double)
	global glTranslatef
	glTranslatef = _makeFunction(loader('glTranslatef'), None, c_float, c_float, c_float)

def __load_GL_VERSION_1_1(loader):
	if glVersion['major'] < 1 or (glVersion['major'] == 1
			and glVersion['minor'] < 1):
		return
	global glDrawArrays
	glDrawArrays = _makeFunction(loader('glDrawArrays'), None, c_uint, c_int, c_int)
	global glDrawElements
	glDrawElements = _makeFunction(loader('glDrawElements'), None, c_uint, c_int, c_uint, c_void_p)
	global glGetPointerv
	glGetPointerv = _makeFunction(loader('glGetPointerv'), None, c_uint, POINTER(c_void_p))
	global glPolygonOffset
	glPolygonOffset = _makeFunction(loader('glPolygonOffset'), None, c_float, c_float)
	global glCopyTexImage1D
	glCopyTexImage1D = _makeFunction(loader('glCopyTexImage1D'), None, c_uint, c_int, c_uint, c_int, c_int, c_int, c_int)
	global glCopyTexImage2D
	glCopyTexImage2D = _makeFunction(loader('glCopyTexImage2D'), None, c_uint, c_int, c_uint, c_int, c_int, c_int, c_int, c_int)
	global glCopyTexSubImage1D
	glCopyTexSubImage1D = _makeFunction(loader('glCopyTexSubImage1D'), None, c_uint, c_int, c_int, c_int, c_int, c_int)
	global glCopyTexSubImage2D
	glCopyTexSubImage2D = _makeFunction(loader('glCopyTexSubImage2D'), None, c_uint, c_int, c_int, c_int, c_int, c_int, c_int, c_int)
	global glTexSubImage1D
	glTexSubImage1D = _makeFunction(loader('glTexSubImage1D'), None, c_uint, c_int, c_int, c_int, c_uint, c_uint, c_void_p)
	global glTexSubImage2D
	glTexSubImage2D = _makeFunction(loader('glTexSubImage2D'), None, c_uint, c_int, c_int, c_int, c_int, c_int, c_uint, c_uint, c_void_p)
	global glBindTexture
	glBindTexture = _makeFunction(loader('glBindTexture'), None, c_uint, c_uint)
	global glDeleteTextures
	glDeleteTextures = _makeFunction(loader('glDeleteTextures'), None, c_int, POINTER(c_uint))
	global glGenTextures
	glGenTextures = _makeFunction(loader('glGenTextures'), None, c_int, POINTER(c_uint))
	global glIsTexture
	glIsTexture = _makeFunction(loader('glIsTexture'), c_bool, c_uint)
	global glArrayElement
	glArrayElement = _makeFunction(loader('glArrayElement'), None, c_int)
	global glColorPointer
	glColorPointer = _makeFunction(loader('glColorPointer'), None, c_int, c_uint, c_int, c_void_p)
	global glDisableClientState
	glDisableClientState = _makeFunction(loader('glDisableClientState'), None, c_uint)
	global glEdgeFlagPointer
	glEdgeFlagPointer = _makeFunction(loader('glEdgeFlagPointer'), None, c_int, c_void_p)
	global glEnableClientState
	glEnableClientState = _makeFunction(loader('glEnableClientState'), None, c_uint)
	global glIndexPointer
	glIndexPointer = _makeFunction(loader('glIndexPointer'), None, c_uint, c_int, c_void_p)
	global glInterleavedArrays
	glInterleavedArrays = _makeFunction(loader('glInterleavedArrays'), None, c_uint, c_int, c_void_p)
	global glNormalPointer
	glNormalPointer = _makeFunction(loader('glNormalPointer'), None, c_uint, c_int, c_void_p)
	global glTexCoordPointer
	glTexCoordPointer = _makeFunction(loader('glTexCoordPointer'), None, c_int, c_uint, c_int, c_void_p)
	global glVertexPointer
	glVertexPointer = _makeFunction(loader('glVertexPointer'), None, c_int, c_uint, c_int, c_void_p)
	global glAreTexturesResident
	glAreTexturesResident = _makeFunction(loader('glAreTexturesResident'), c_bool, c_int, POINTER(c_uint), POINTER(c_bool))
	global glPrioritizeTextures
	glPrioritizeTextures = _makeFunction(loader('glPrioritizeTextures'), None, c_int, POINTER(c_uint), POINTER(c_float))
	global glIndexub
	glIndexub = _makeFunction(loader('glIndexub'), None, c_ubyte)
	global glIndexubv
	glIndexubv = _makeFunction(loader('glIndexubv'), None, POINTER(c_ubyte))
	global glPopClientAttrib
	glPopClientAttrib = _makeFunction(loader('glPopClientAttrib'), None)
	global glPushClientAttrib
	glPushClientAttrib = _makeFunction(loader('glPushClientAttrib'), None, c_uint)

def __load_GL_VERSION_1_2(loader):
	if glVersion['major'] < 1 or (glVersion['major'] == 1
			and glVersion['minor'] < 2):
		return
	global glDrawRangeElements
	glDrawRangeElements = _makeFunction(loader('glDrawRangeElements'), None, c_uint, c_uint, c_uint, c_int, c_uint, c_void_p)
	global glTexImage3D
	glTexImage3D = _makeFunction(loader('glTexImage3D'), None, c_uint, c_int, c_int, c_int, c_int, c_int, c_int, c_uint, c_uint, c_void_p)
	global glTexSubImage3D
	glTexSubImage3D = _makeFunction(loader('glTexSubImage3D'), None, c_uint, c_int, c_int, c_int, c_int, c_int, c_int, c_int, c_uint, c_uint, c_void_p)
	global glCopyTexSubImage3D
	glCopyTexSubImage3D = _makeFunction(loader('glCopyTexSubImage3D'), None, c_uint, c_int, c_int, c_int, c_int, c_int, c_int, c_int, c_int)

def __load_GL_VERSION_1_3(loader):
	if glVersion['major'] < 1 or (glVersion['major'] == 1
			and glVersion['minor'] < 3):
		return
	global glActiveTexture
	glActiveTexture = _makeFunction(loader('glActiveTexture'), None, c_uint)
	global glSampleCoverage
	glSampleCoverage = _makeFunction(loader('glSampleCoverage'), None, c_float, c_bool)
	global glCompressedTexImage3D
	glCompressedTexImage3D = _makeFunction(loader('glCompressedTexImage3D'), None, c_uint, c_int, c_uint, c_int, c_int, c_int, c_int, c_int, c_void_p)
	global glCompressedTexImage2D
	glCompressedTexImage2D = _makeFunction(loader('glCompressedTexImage2D'), None, c_uint, c_int, c_uint, c_int, c_int, c_int, c_int, c_void_p)
	global glCompressedTexImage1D
	glCompressedTexImage1D = _makeFunction(loader('glCompressedTexImage1D'), None, c_uint, c_int, c_uint, c_int, c_int, c_int, c_void_p)
	global glCompressedTexSubImage3D
	glCompressedTexSubImage3D = _makeFunction(loader('glCompressedTexSubImage3D'), None, c_uint, c_int, c_int, c_int, c_int, c_int, c_int, c_int, c_uint, c_int, c_void_p)
	global glCompressedTexSubImage2D
	glCompressedTexSubImage2D = _makeFunction(loader('glCompressedTexSubImage2D'), None, c_uint, c_int, c_int, c_int, c_int, c_int, c_uint, c_int, c_void_p)
	global glCompressedTexSubImage1D
	glCompressedTexSubImage1D = _makeFunction(loader('glCompressedTexSubImage1D'), None, c_uint, c_int, c_int, c_int, c_uint, c_int, c_void_p)
	global glGetCompressedTexImage
	glGetCompressedTexImage = _makeFunction(loader('glGetCompressedTexImage'), None, c_uint, c_int, c_void_p)
	global glClientActiveTexture
	glClientActiveTexture = _makeFunction(loader('glClientActiveTexture'), None, c_uint)
	global glMultiTexCoord1d
	glMultiTexCoord1d = _makeFunction(loader('glMultiTexCoord1d'), None, c_uint, c_double)
	global glMultiTexCoord1dv
	glMultiTexCoord1dv = _makeFunction(loader('glMultiTexCoord1dv'), None, c_uint, POINTER(c_double))
	global glMultiTexCoord1f
	glMultiTexCoord1f = _makeFunction(loader('glMultiTexCoord1f'), None, c_uint, c_float)
	global glMultiTexCoord1fv
	glMultiTexCoord1fv = _makeFunction(loader('glMultiTexCoord1fv'), None, c_uint, POINTER(c_float))
	global glMultiTexCoord1i
	glMultiTexCoord1i = _makeFunction(loader('glMultiTexCoord1i'), None, c_uint, c_int)
	global glMultiTexCoord1iv
	glMultiTexCoord1iv = _makeFunction(loader('glMultiTexCoord1iv'), None, c_uint, POINTER(c_int))
	global glMultiTexCoord1s
	glMultiTexCoord1s = _makeFunction(loader('glMultiTexCoord1s'), None, c_uint, c_short)
	global glMultiTexCoord1sv
	glMultiTexCoord1sv = _makeFunction(loader('glMultiTexCoord1sv'), None, c_uint, POINTER(c_short))
	global glMultiTexCoord2d
	glMultiTexCoord2d = _makeFunction(loader('glMultiTexCoord2d'), None, c_uint, c_double, c_double)
	global glMultiTexCoord2dv
	glMultiTexCoord2dv = _makeFunction(loader('glMultiTexCoord2dv'), None, c_uint, POINTER(c_double))
	global glMultiTexCoord2f
	glMultiTexCoord2f = _makeFunction(loader('glMultiTexCoord2f'), None, c_uint, c_float, c_float)
	global glMultiTexCoord2fv
	glMultiTexCoord2fv = _makeFunction(loader('glMultiTexCoord2fv'), None, c_uint, POINTER(c_float))
	global glMultiTexCoord2i
	glMultiTexCoord2i = _makeFunction(loader('glMultiTexCoord2i'), None, c_uint, c_int, c_int)
	global glMultiTexCoord2iv
	glMultiTexCoord2iv = _makeFunction(loader('glMultiTexCoord2iv'), None, c_uint, POINTER(c_int))
	global glMultiTexCoord2s
	glMultiTexCoord2s = _makeFunction(loader('glMultiTexCoord2s'), None, c_uint, c_short, c_short)
	global glMultiTexCoord2sv
	glMultiTexCoord2sv = _makeFunction(loader('glMultiTexCoord2sv'), None, c_uint, POINTER(c_short))
	global glMultiTexCoord3d
	glMultiTexCoord3d = _makeFunction(loader('glMultiTexCoord3d'), None, c_uint, c_double, c_double, c_double)
	global glMultiTexCoord3dv
	glMultiTexCoord3dv = _makeFunction(loader('glMultiTexCoord3dv'), None, c_uint, POINTER(c_double))
	global glMultiTexCoord3f
	glMultiTexCoord3f = _makeFunction(loader('glMultiTexCoord3f'), None, c_uint, c_float, c_float, c_float)
	global glMultiTexCoord3fv
	glMultiTexCoord3fv = _makeFunction(loader('glMultiTexCoord3fv'), None, c_uint, POINTER(c_float))
	global glMultiTexCoord3i
	glMultiTexCoord3i = _makeFunction(loader('glMultiTexCoord3i'), None, c_uint, c_int, c_int, c_int)
	global glMultiTexCoord3iv
	glMultiTexCoord3iv = _makeFunction(loader('glMultiTexCoord3iv'), None, c_uint, POINTER(c_int))
	global glMultiTexCoord3s
	glMultiTexCoord3s = _makeFunction(loader('glMultiTexCoord3s'), None, c_uint, c_short, c_short, c_short)
	global glMultiTexCoord3sv
	glMultiTexCoord3sv = _makeFunction(loader('glMultiTexCoord3sv'), None, c_uint, POINTER(c_short))
	global glMultiTexCoord4d
	glMultiTexCoord4d = _makeFunction(loader('glMultiTexCoord4d'), None, c_uint, c_double, c_double, c_double, c_double)
	global glMultiTexCoord4dv
	glMultiTexCoord4dv = _makeFunction(loader('glMultiTexCoord4dv'), None, c_uint, POINTER(c_double))
	global glMultiTexCoord4f
	glMultiTexCoord4f = _makeFunction(loader('glMultiTexCoord4f'), None, c_uint, c_float, c_float, c_float, c_float)
	global glMultiTexCoord4fv
	glMultiTexCoord4fv = _makeFunction(loader('glMultiTexCoord4fv'), None, c_uint, POINTER(c_float))
	global glMultiTexCoord4i
	glMultiTexCoord4i = _makeFunction(loader('glMultiTexCoord4i'), None, c_uint, c_int, c_int, c_int, c_int)
	global glMultiTexCoord4iv
	glMultiTexCoord4iv = _makeFunction(loader('glMultiTexCoord4iv'), None, c_uint, POINTER(c_int))
	global glMultiTexCoord4s
	glMultiTexCoord4s = _makeFunction(loader('glMultiTexCoord4s'), None, c_uint, c_short, c_short, c_short, c_short)
	global glMultiTexCoord4sv
	glMultiTexCoord4sv = _makeFunction(loader('glMultiTexCoord4sv'), None, c_uint, POINTER(c_short))
	global glLoadTransposeMatrixf
	glLoadTransposeMatrixf = _makeFunction(loader('glLoadTransposeMatrixf'), None, POINTER(c_float))
	global glLoadTransposeMatrixd
	glLoadTransposeMatrixd = _makeFunction(loader('glLoadTransposeMatrixd'), None, POINTER(c_double))
	global glMultTransposeMatrixf
	glMultTransposeMatrixf = _makeFunction(loader('glMultTransposeMatrixf'), None, POINTER(c_float))
	global glMultTransposeMatrixd
	glMultTransposeMatrixd = _makeFunction(loader('glMultTransposeMatrixd'), None, POINTER(c_double))

def __load_GL_VERSION_1_4(loader):
	if glVersion['major'] < 1 or (glVersion['major'] == 1
			and glVersion['minor'] < 4):
		return
	global glBlendFuncSeparate
	glBlendFuncSeparate = _makeFunction(loader('glBlendFuncSeparate'), None, c_uint, c_uint, c_uint, c_uint)
	global glMultiDrawArrays
	glMultiDrawArrays = _makeFunction(loader('glMultiDrawArrays'), None, c_uint, POINTER(c_int), POINTER(c_int), c_int)
	global glMultiDrawElements
	glMultiDrawElements = _makeFunction(loader('glMultiDrawElements'), None, c_uint, POINTER(c_int), c_uint, POINTER(c_void_p), c_int)
	global glPointParameterf
	glPointParameterf = _makeFunction(loader('glPointParameterf'), None, c_uint, c_float)
	global glPointParameterfv
	glPointParameterfv = _makeFunction(loader('glPointParameterfv'), None, c_uint, POINTER(c_float))
	global glPointParameteri
	glPointParameteri = _makeFunction(loader('glPointParameteri'), None, c_uint, c_int)
	global glPointParameteriv
	glPointParameteriv = _makeFunction(loader('glPointParameteriv'), None, c_uint, POINTER(c_int))
	global glFogCoordf
	glFogCoordf = _makeFunction(loader('glFogCoordf'), None, c_float)
	global glFogCoordfv
	glFogCoordfv = _makeFunction(loader('glFogCoordfv'), None, POINTER(c_float))
	global glFogCoordd
	glFogCoordd = _makeFunction(loader('glFogCoordd'), None, c_double)
	global glFogCoorddv
	glFogCoorddv = _makeFunction(loader('glFogCoorddv'), None, POINTER(c_double))
	global glFogCoordPointer
	glFogCoordPointer = _makeFunction(loader('glFogCoordPointer'), None, c_uint, c_int, c_void_p)
	global glSecondaryColor3b
	glSecondaryColor3b = _makeFunction(loader('glSecondaryColor3b'), None, c_byte, c_byte, c_byte)
	global glSecondaryColor3bv
	glSecondaryColor3bv = _makeFunction(loader('glSecondaryColor3bv'), None, POINTER(c_byte))
	global glSecondaryColor3d
	glSecondaryColor3d = _makeFunction(loader('glSecondaryColor3d'), None, c_double, c_double, c_double)
	global glSecondaryColor3dv
	glSecondaryColor3dv = _makeFunction(loader('glSecondaryColor3dv'), None, POINTER(c_double))
	global glSecondaryColor3f
	glSecondaryColor3f = _makeFunction(loader('glSecondaryColor3f'), None, c_float, c_float, c_float)
	global glSecondaryColor3fv
	glSecondaryColor3fv = _makeFunction(loader('glSecondaryColor3fv'), None, POINTER(c_float))
	global glSecondaryColor3i
	glSecondaryColor3i = _makeFunction(loader('glSecondaryColor3i'), None, c_int, c_int, c_int)
	global glSecondaryColor3iv
	glSecondaryColor3iv = _makeFunction(loader('glSecondaryColor3iv'), None, POINTER(c_int))
	global glSecondaryColor3s
	glSecondaryColor3s = _makeFunction(loader('glSecondaryColor3s'), None, c_short, c_short, c_short)
	global glSecondaryColor3sv
	glSecondaryColor3sv = _makeFunction(loader('glSecondaryColor3sv'), None, POINTER(c_short))
	global glSecondaryColor3ub
	glSecondaryColor3ub = _makeFunction(loader('glSecondaryColor3ub'), None, c_ubyte, c_ubyte, c_ubyte)
	global glSecondaryColor3ubv
	glSecondaryColor3ubv = _makeFunction(loader('glSecondaryColor3ubv'), None, POINTER(c_ubyte))
	global glSecondaryColor3ui
	glSecondaryColor3ui = _makeFunction(loader('glSecondaryColor3ui'), None, c_uint, c_uint, c_uint)
	global glSecondaryColor3uiv
	glSecondaryColor3uiv = _makeFunction(loader('glSecondaryColor3uiv'), None, POINTER(c_uint))
	global glSecondaryColor3us
	glSecondaryColor3us = _makeFunction(loader('glSecondaryColor3us'), None, c_ushort, c_ushort, c_ushort)
	global glSecondaryColor3usv
	glSecondaryColor3usv = _makeFunction(loader('glSecondaryColor3usv'), None, POINTER(c_ushort))
	global glSecondaryColorPointer
	glSecondaryColorPointer = _makeFunction(loader('glSecondaryColorPointer'), None, c_int, c_uint, c_int, c_void_p)
	global glWindowPos2d
	glWindowPos2d = _makeFunction(loader('glWindowPos2d'), None, c_double, c_double)
	global glWindowPos2dv
	glWindowPos2dv = _makeFunction(loader('glWindowPos2dv'), None, POINTER(c_double))
	global glWindowPos2f
	glWindowPos2f = _makeFunction(loader('glWindowPos2f'), None, c_float, c_float)
	global glWindowPos2fv
	glWindowPos2fv = _makeFunction(loader('glWindowPos2fv'), None, POINTER(c_float))
	global glWindowPos2i
	glWindowPos2i = _makeFunction(loader('glWindowPos2i'), None, c_int, c_int)
	global glWindowPos2iv
	glWindowPos2iv = _makeFunction(loader('glWindowPos2iv'), None, POINTER(c_int))
	global glWindowPos2s
	glWindowPos2s = _makeFunction(loader('glWindowPos2s'), None, c_short, c_short)
	global glWindowPos2sv
	glWindowPos2sv = _makeFunction(loader('glWindowPos2sv'), None, POINTER(c_short))
	global glWindowPos3d
	glWindowPos3d = _makeFunction(loader('glWindowPos3d'), None, c_double, c_double, c_double)
	global glWindowPos3dv
	glWindowPos3dv = _makeFunction(loader('glWindowPos3dv'), None, POINTER(c_double))
	global glWindowPos3f
	glWindowPos3f = _makeFunction(loader('glWindowPos3f'), None, c_float, c_float, c_float)
	global glWindowPos3fv
	glWindowPos3fv = _makeFunction(loader('glWindowPos3fv'), None, POINTER(c_float))
	global glWindowPos3i
	glWindowPos3i = _makeFunction(loader('glWindowPos3i'), None, c_int, c_int, c_int)
	global glWindowPos3iv
	glWindowPos3iv = _makeFunction(loader('glWindowPos3iv'), None, POINTER(c_int))
	global glWindowPos3s
	glWindowPos3s = _makeFunction(loader('glWindowPos3s'), None, c_short, c_short, c_short)
	global glWindowPos3sv
	glWindowPos3sv = _makeFunction(loader('glWindowPos3sv'), None, POINTER(c_short))
	global glBlendColor
	glBlendColor = _makeFunction(loader('glBlendColor'), None, c_float, c_float, c_float, c_float)
	global glBlendEquation
	glBlendEquation = _makeFunction(loader('glBlendEquation'), None, c_uint)

def __load_GL_VERSION_1_5(loader):
	if glVersion['major'] < 1 or (glVersion['major'] == 1
			and glVersion['minor'] < 5):
		return
	global glGenQueries
	glGenQueries = _makeFunction(loader('glGenQueries'), None, c_int, POINTER(c_uint))
	global glDeleteQueries
	glDeleteQueries = _makeFunction(loader('glDeleteQueries'), None, c_int, POINTER(c_uint))
	global glIsQuery
	glIsQuery = _makeFunction(loader('glIsQuery'), c_bool, c_uint)
	global glBeginQuery
	glBeginQuery = _makeFunction(loader('glBeginQuery'), None, c_uint, c_uint)
	global glEndQuery
	glEndQuery = _makeFunction(loader('glEndQuery'), None, c_uint)
	global glGetQueryiv
	glGetQueryiv = _makeFunction(loader('glGetQueryiv'), None, c_uint, c_uint, POINTER(c_int))
	global glGetQueryObjectiv
	glGetQueryObjectiv = _makeFunction(loader('glGetQueryObjectiv'), None, c_uint, c_uint, POINTER(c_int))
	global glGetQueryObjectuiv
	glGetQueryObjectuiv = _makeFunction(loader('glGetQueryObjectuiv'), None, c_uint, c_uint, POINTER(c_uint))
	global glBindBuffer
	glBindBuffer = _makeFunction(loader('glBindBuffer'), None, c_uint, c_uint)
	global glDeleteBuffers
	glDeleteBuffers = _makeFunction(loader('glDeleteBuffers'), None, c_int, POINTER(c_uint))
	global glGenBuffers
	glGenBuffers = _makeFunction(loader('glGenBuffers'), None, c_int, POINTER(c_uint))
	global glIsBuffer
	glIsBuffer = _makeFunction(loader('glIsBuffer'), c_bool, c_uint)
	global glBufferData
	glBufferData = _makeFunction(loader('glBufferData'), None, c_uint, ptrdiff_t, c_void_p, c_uint)
	global glBufferSubData
	glBufferSubData = _makeFunction(loader('glBufferSubData'), None, c_uint, ptrdiff_t, ptrdiff_t, c_void_p)
	global glGetBufferSubData
	glGetBufferSubData = _makeFunction(loader('glGetBufferSubData'), None, c_uint, ptrdiff_t, ptrdiff_t, c_void_p)
	global glMapBuffer
	glMapBuffer = _makeFunction(loader('glMapBuffer'), c_void_p, c_uint, c_uint)
	global glUnmapBuffer
	glUnmapBuffer = _makeFunction(loader('glUnmapBuffer'), c_bool, c_uint)
	global glGetBufferParameteriv
	glGetBufferParameteriv = _makeFunction(loader('glGetBufferParameteriv'), None, c_uint, c_uint, POINTER(c_int))
	global glGetBufferPointerv
	glGetBufferPointerv = _makeFunction(loader('glGetBufferPointerv'), None, c_uint, c_uint, POINTER(c_void_p))

def __load_GL_VERSION_2_0(loader):
	if glVersion['major'] < 2 or (glVersion['major'] == 2
			and glVersion['minor'] < 0):
		return
	global glBlendEquationSeparate
	glBlendEquationSeparate = _makeFunction(loader('glBlendEquationSeparate'), None, c_uint, c_uint)
	global glDrawBuffers
	glDrawBuffers = _makeFunction(loader('glDrawBuffers'), None, c_int, POINTER(c_uint))
	global glStencilOpSeparate
	glStencilOpSeparate = _makeFunction(loader('glStencilOpSeparate'), None, c_uint, c_uint, c_uint, c_uint)
	global glStencilFuncSeparate
	glStencilFuncSeparate = _makeFunction(loader('glStencilFuncSeparate'), None, c_uint, c_uint, c_int, c_uint)
	global glStencilMaskSeparate
	glStencilMaskSeparate = _makeFunction(loader('glStencilMaskSeparate'), None, c_uint, c_uint)
	global glAttachShader
	glAttachShader = _makeFunction(loader('glAttachShader'), None, c_uint, c_uint)
	global glBindAttribLocation
	glBindAttribLocation = _makeFunction(loader('glBindAttribLocation'), None, c_uint, c_uint, c_char_p)
	global glCompileShader
	glCompileShader = _makeFunction(loader('glCompileShader'), None, c_uint)
	global glCreateProgram
	glCreateProgram = _makeFunction(loader('glCreateProgram'), c_uint)
	global glCreateShader
	glCreateShader = _makeFunction(loader('glCreateShader'), c_uint, c_uint)
	global glDeleteProgram
	glDeleteProgram = _makeFunction(loader('glDeleteProgram'), None, c_uint)
	global glDeleteShader
	glDeleteShader = _makeFunction(loader('glDeleteShader'), None, c_uint)
	global glDetachShader
	glDetachShader = _makeFunction(loader('glDetachShader'), None, c_uint, c_uint)
	global glDisableVertexAttribArray
	glDisableVertexAttribArray = _makeFunction(loader('glDisableVertexAttribArray'), None, c_uint)
	global glEnableVertexAttribArray
	glEnableVertexAttribArray = _makeFunction(loader('glEnableVertexAttribArray'), None, c_uint)
	global glGetActiveAttrib
	glGetActiveAttrib = _makeFunction(loader('glGetActiveAttrib'), None, c_uint, c_uint, c_int, POINTER(c_int), POINTER(c_int), POINTER(c_uint), c_char_p)
	global glGetActiveUniform
	glGetActiveUniform = _makeFunction(loader('glGetActiveUniform'), None, c_uint, c_uint, c_int, POINTER(c_int), POINTER(c_int), POINTER(c_uint), c_char_p)
	global glGetAttachedShaders
	glGetAttachedShaders = _makeFunction(loader('glGetAttachedShaders'), None, c_uint, c_int, POINTER(c_int), POINTER(c_uint))
	global glGetAttribLocation
	glGetAttribLocation = _makeFunction(loader('glGetAttribLocation'), c_int, c_uint, c_char_p)
	global glGetProgramiv
	glGetProgramiv = _makeFunction(loader('glGetProgramiv'), None, c_uint, c_uint, POINTER(c_int))
	global glGetProgramInfoLog
	glGetProgramInfoLog = _makeFunction(loader('glGetProgramInfoLog'), None, c_uint, c_int, POINTER(c_int), c_char_p)
	global glGetShaderiv
	glGetShaderiv = _makeFunction(loader('glGetShaderiv'), None, c_uint, c_uint, POINTER(c_int))
	global glGetShaderInfoLog
	glGetShaderInfoLog = _makeFunction(loader('glGetShaderInfoLog'), None, c_uint, c_int, POINTER(c_int), c_char_p)
	global glGetShaderSource
	glGetShaderSource = _makeFunction(loader('glGetShaderSource'), None, c_uint, c_int, POINTER(c_int), c_char_p)
	global glGetUniformLocation
	glGetUniformLocation = _makeFunction(loader('glGetUniformLocation'), c_int, c_uint, c_char_p)
	global glGetUniformfv
	glGetUniformfv = _makeFunction(loader('glGetUniformfv'), None, c_uint, c_int, POINTER(c_float))
	global glGetUniformiv
	glGetUniformiv = _makeFunction(loader('glGetUniformiv'), None, c_uint, c_int, POINTER(c_int))
	global glGetVertexAttribdv
	glGetVertexAttribdv = _makeFunction(loader('glGetVertexAttribdv'), None, c_uint, c_uint, POINTER(c_double))
	global glGetVertexAttribfv
	glGetVertexAttribfv = _makeFunction(loader('glGetVertexAttribfv'), None, c_uint, c_uint, POINTER(c_float))
	global glGetVertexAttribiv
	glGetVertexAttribiv = _makeFunction(loader('glGetVertexAttribiv'), None, c_uint, c_uint, POINTER(c_int))
	global glGetVertexAttribPointerv
	glGetVertexAttribPointerv = _makeFunction(loader('glGetVertexAttribPointerv'), None, c_uint, c_uint, POINTER(c_void_p))
	global glIsProgram
	glIsProgram = _makeFunction(loader('glIsProgram'), c_bool, c_uint)
	global glIsShader
	glIsShader = _makeFunction(loader('glIsShader'), c_bool, c_uint)
	global glLinkProgram
	glLinkProgram = _makeFunction(loader('glLinkProgram'), None, c_uint)
	global glShaderSource
	glShaderSource = _makeFunction(loader('glShaderSource'), None, c_uint, c_int, POINTER(c_char_p), POINTER(c_int))
	global glUseProgram
	glUseProgram = _makeFunction(loader('glUseProgram'), None, c_uint)
	global glUniform1f
	glUniform1f = _makeFunction(loader('glUniform1f'), None, c_int, c_float)
	global glUniform2f
	glUniform2f = _makeFunction(loader('glUniform2f'), None, c_int, c_float, c_float)
	global glUniform3f
	glUniform3f = _makeFunction(loader('glUniform3f'), None, c_int, c_float, c_float, c_float)
	global glUniform4f
	glUniform4f = _makeFunction(loader('glUniform4f'), None, c_int, c_float, c_float, c_float, c_float)
	global glUniform1i
	glUniform1i = _makeFunction(loader('glUniform1i'), None, c_int, c_int)
	global glUniform2i
	glUniform2i = _makeFunction(loader('glUniform2i'), None, c_int, c_int, c_int)
	global glUniform3i
	glUniform3i = _makeFunction(loader('glUniform3i'), None, c_int, c_int, c_int, c_int)
	global glUniform4i
	glUniform4i = _makeFunction(loader('glUniform4i'), None, c_int, c_int, c_int, c_int, c_int)
	global glUniform1fv
	glUniform1fv = _makeFunction(loader('glUniform1fv'), None, c_int, c_int, POINTER(c_float))
	global glUniform2fv
	glUniform2fv = _makeFunction(loader('glUniform2fv'), None, c_int, c_int, POINTER(c_float))
	global glUniform3fv
	glUniform3fv = _makeFunction(loader('glUniform3fv'), None, c_int, c_int, POINTER(c_float))
	global glUniform4fv
	glUniform4fv = _makeFunction(loader('glUniform4fv'), None, c_int, c_int, POINTER(c_float))
	global glUniform1iv
	glUniform1iv = _makeFunction(loader('glUniform1iv'), None, c_int, c_int, POINTER(c_int))
	global glUniform2iv
	glUniform2iv = _makeFunction(loader('glUniform2iv'), None, c_int, c_int, POINTER(c_int))
	global glUniform3iv
	glUniform3iv = _makeFunction(loader('glUniform3iv'), None, c_int, c_int, POINTER(c_int))
	global glUniform4iv
	glUniform4iv = _makeFunction(loader('glUniform4iv'), None, c_int, c_int, POINTER(c_int))
	global glUniformMatrix2fv
	glUniformMatrix2fv = _makeFunction(loader('glUniformMatrix2fv'), None, c_int, c_int, c_bool, POINTER(c_float))
	global glUniformMatrix3fv
	glUniformMatrix3fv = _makeFunction(loader('glUniformMatrix3fv'), None, c_int, c_int, c_bool, POINTER(c_float))
	global glUniformMatrix4fv
	glUniformMatrix4fv = _makeFunction(loader('glUniformMatrix4fv'), None, c_int, c_int, c_bool, POINTER(c_float))
	global glValidateProgram
	glValidateProgram = _makeFunction(loader('glValidateProgram'), None, c_uint)
	global glVertexAttrib1d
	glVertexAttrib1d = _makeFunction(loader('glVertexAttrib1d'), None, c_uint, c_double)
	global glVertexAttrib1dv
	glVertexAttrib1dv = _makeFunction(loader('glVertexAttrib1dv'), None, c_uint, POINTER(c_double))
	global glVertexAttrib1f
	glVertexAttrib1f = _makeFunction(loader('glVertexAttrib1f'), None, c_uint, c_float)
	global glVertexAttrib1fv
	glVertexAttrib1fv = _makeFunction(loader('glVertexAttrib1fv'), None, c_uint, POINTER(c_float))
	global glVertexAttrib1s
	glVertexAttrib1s = _makeFunction(loader('glVertexAttrib1s'), None, c_uint, c_short)
	global glVertexAttrib1sv
	glVertexAttrib1sv = _makeFunction(loader('glVertexAttrib1sv'), None, c_uint, POINTER(c_short))
	global glVertexAttrib2d
	glVertexAttrib2d = _makeFunction(loader('glVertexAttrib2d'), None, c_uint, c_double, c_double)
	global glVertexAttrib2dv
	glVertexAttrib2dv = _makeFunction(loader('glVertexAttrib2dv'), None, c_uint, POINTER(c_double))
	global glVertexAttrib2f
	glVertexAttrib2f = _makeFunction(loader('glVertexAttrib2f'), None, c_uint, c_float, c_float)
	global glVertexAttrib2fv
	glVertexAttrib2fv = _makeFunction(loader('glVertexAttrib2fv'), None, c_uint, POINTER(c_float))
	global glVertexAttrib2s
	glVertexAttrib2s = _makeFunction(loader('glVertexAttrib2s'), None, c_uint, c_short, c_short)
	global glVertexAttrib2sv
	glVertexAttrib2sv = _makeFunction(loader('glVertexAttrib2sv'), None, c_uint, POINTER(c_short))
	global glVertexAttrib3d
	glVertexAttrib3d = _makeFunction(loader('glVertexAttrib3d'), None, c_uint, c_double, c_double, c_double)
	global glVertexAttrib3dv
	glVertexAttrib3dv = _makeFunction(loader('glVertexAttrib3dv'), None, c_uint, POINTER(c_double))
	global glVertexAttrib3f
	glVertexAttrib3f = _makeFunction(loader('glVertexAttrib3f'), None, c_uint, c_float, c_float, c_float)
	global glVertexAttrib3fv
	glVertexAttrib3fv = _makeFunction(loader('glVertexAttrib3fv'), None, c_uint, POINTER(c_float))
	global glVertexAttrib3s
	glVertexAttrib3s = _makeFunction(loader('glVertexAttrib3s'), None, c_uint, c_short, c_short, c_short)
	global glVertexAttrib3sv
	glVertexAttrib3sv = _makeFunction(loader('glVertexAttrib3sv'), None, c_uint, POINTER(c_short))
	global glVertexAttrib4Nbv
	glVertexAttrib4Nbv = _makeFunction(loader('glVertexAttrib4Nbv'), None, c_uint, POINTER(c_byte))
	global glVertexAttrib4Niv
	glVertexAttrib4Niv = _makeFunction(loader('glVertexAttrib4Niv'), None, c_uint, POINTER(c_int))
	global glVertexAttrib4Nsv
	glVertexAttrib4Nsv = _makeFunction(loader('glVertexAttrib4Nsv'), None, c_uint, POINTER(c_short))
	global glVertexAttrib4Nub
	glVertexAttrib4Nub = _makeFunction(loader('glVertexAttrib4Nub'), None, c_uint, c_ubyte, c_ubyte, c_ubyte, c_ubyte)
	global glVertexAttrib4Nubv
	glVertexAttrib4Nubv = _makeFunction(loader('glVertexAttrib4Nubv'), None, c_uint, POINTER(c_ubyte))
	global glVertexAttrib4Nuiv
	glVertexAttrib4Nuiv = _makeFunction(loader('glVertexAttrib4Nuiv'), None, c_uint, POINTER(c_uint))
	global glVertexAttrib4Nusv
	glVertexAttrib4Nusv = _makeFunction(loader('glVertexAttrib4Nusv'), None, c_uint, POINTER(c_ushort))
	global glVertexAttrib4bv
	glVertexAttrib4bv = _makeFunction(loader('glVertexAttrib4bv'), None, c_uint, POINTER(c_byte))
	global glVertexAttrib4d
	glVertexAttrib4d = _makeFunction(loader('glVertexAttrib4d'), None, c_uint, c_double, c_double, c_double, c_double)
	global glVertexAttrib4dv
	glVertexAttrib4dv = _makeFunction(loader('glVertexAttrib4dv'), None, c_uint, POINTER(c_double))
	global glVertexAttrib4f
	glVertexAttrib4f = _makeFunction(loader('glVertexAttrib4f'), None, c_uint, c_float, c_float, c_float, c_float)
	global glVertexAttrib4fv
	glVertexAttrib4fv = _makeFunction(loader('glVertexAttrib4fv'), None, c_uint, POINTER(c_float))
	global glVertexAttrib4iv
	glVertexAttrib4iv = _makeFunction(loader('glVertexAttrib4iv'), None, c_uint, POINTER(c_int))
	global glVertexAttrib4s
	glVertexAttrib4s = _makeFunction(loader('glVertexAttrib4s'), None, c_uint, c_short, c_short, c_short, c_short)
	global glVertexAttrib4sv
	glVertexAttrib4sv = _makeFunction(loader('glVertexAttrib4sv'), None, c_uint, POINTER(c_short))
	global glVertexAttrib4ubv
	glVertexAttrib4ubv = _makeFunction(loader('glVertexAttrib4ubv'), None, c_uint, POINTER(c_ubyte))
	global glVertexAttrib4uiv
	glVertexAttrib4uiv = _makeFunction(loader('glVertexAttrib4uiv'), None, c_uint, POINTER(c_uint))
	global glVertexAttrib4usv
	glVertexAttrib4usv = _makeFunction(loader('glVertexAttrib4usv'), None, c_uint, POINTER(c_ushort))
	global glVertexAttribPointer
	glVertexAttribPointer = _makeFunction(loader('glVertexAttribPointer'), None, c_uint, c_int, c_uint, c_bool, c_int, c_void_p)

def __load_GL_VERSION_2_1(loader):
	if glVersion['major'] < 2 or (glVersion['major'] == 2
			and glVersion['minor'] < 1):
		return
	global glUniformMatrix2x3fv
	glUniformMatrix2x3fv = _makeFunction(loader('glUniformMatrix2x3fv'), None, c_int, c_int, c_bool, POINTER(c_float))
	global glUniformMatrix3x2fv
	glUniformMatrix3x2fv = _makeFunction(loader('glUniformMatrix3x2fv'), None, c_int, c_int, c_bool, POINTER(c_float))
	global glUniformMatrix2x4fv
	glUniformMatrix2x4fv = _makeFunction(loader('glUniformMatrix2x4fv'), None, c_int, c_int, c_bool, POINTER(c_float))
	global glUniformMatrix4x2fv
	glUniformMatrix4x2fv = _makeFunction(loader('glUniformMatrix4x2fv'), None, c_int, c_int, c_bool, POINTER(c_float))
	global glUniformMatrix3x4fv
	glUniformMatrix3x4fv = _makeFunction(loader('glUniformMatrix3x4fv'), None, c_int, c_int, c_bool, POINTER(c_float))
	global glUniformMatrix4x3fv
	glUniformMatrix4x3fv = _makeFunction(loader('glUniformMatrix4x3fv'), None, c_int, c_int, c_bool, POINTER(c_float))

def loadGL(loader=_getProcAddress):
	if loader is _getProcAddress:
		_loadGLLibrary()
	# OpenGL 1.0 will export this... let's just make our own temp reference
	_tempGlgs = _makeFunction(loader("glGetString"), POINTER(c_ubyte), c_uint)
	versionStr = cast(_tempGlgs(GL_VERSION), c_char_p)
	match = re.search(rb'(\d+).(\d+)', versionStr.value)
	majorBStr, minorBStr = match.group(1, 2)
	glVersion["major"] = int(majorBStr)
	glVersion["minor"] = int(minorBStr)
	__load_GL_VERSION_1_0(loader)
	__load_GL_VERSION_1_1(loader)
	__load_GL_VERSION_1_2(loader)
	__load_GL_VERSION_1_3(loader)
	__load_GL_VERSION_1_4(loader)
	__load_GL_VERSION_1_5(loader)
	__load_GL_VERSION_2_0(loader)
	__load_GL_VERSION_2_1(loader)
