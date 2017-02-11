from ctypes import * # c_int, c_float, c_double, c_uint, byref
import sys
import os

print('Changing CWD to parent directory')
os.chdir('..')
print('Adding ./ to Python module path')
sys.path.append('.')
import gl_generated_example as gl
# I am using Florian Rhiem's GLFW binding, hence the GLFW function renaming
# https://github.com/FlorianRhiem/pyGLFW/blob/master/glfw.py
import glfw

class TestOpenGL1:
    def __init__(self):
        pass
    def setup(self, window):
        self.window = window
    def render(self):
        # adapted-ish from Nicolas P. Rougier's GLFW binding test
        # https://github.com/rougier/pyglfw/blob/master/simple.py
        # perma:
        # https://github.com/rougier/pyglfw/blob/d5d1f596b5bac06f2a78d09ca85806acdcedd308/simple.py
        width, height = glfw.get_framebuffer_size(self.window)
        ratio = width / float(height)
        gl.glViewport(0, 0, width, height)
        gl.glClear(gl.GL_COLOR_BUFFER_BIT)
        gl.glMatrixMode(gl.GL_PROJECTION)
        gl.glLoadIdentity()
        gl.glOrtho(-ratio, ratio, -1, 1, 1, -1)
        gl.glMatrixMode(gl.GL_MODELVIEW)
        gl.glLoadIdentity()
        gl.glBegin(gl.GL_TRIANGLES)
        gl.glColor3f(1, 0, 0)
        gl.glVertex3f(-0.6, -0.4, 0)
        gl.glColor3f(0, 1, 0)
        gl.glVertex3f(0.6, -0.4, 0)
        gl.glColor3f(0, 0, 1)
        gl.glVertex3f(0, 0.6, 0)
        gl.glEnd()

class TestOpenGL2_1:
    """ Basic 2.1 test using VBOs. Does not use any shaders. """
    def setup(self, window):
        # adapted from LWGL2's OpenGL3 tutorial (minus VAOs, hence it runs on 2.1)
        gl.glViewport(0, 0, 640, 480)
        # set up the quad
        vertexData = [
            # left bottom triangle
            -0.5, 0.5, 0.0,
            -0.5, -0.5, 0.0,
            0.5, -0.5, 0.0,
            # right top triangle
            0.5, -0.5, 0.0,
            0.5, 0.5, 0.0,
            -0.5, 0.5, 0.0
        ]
        self.vertexCount = 6
        vertexDataArrayType = c_float * (self.vertexCount * 3)
        vertexCArray = vertexDataArrayType(*vertexData)
        self.vbo = c_uint(0)
        gl.glGenBuffers(1, byref(self.vbo))
        if not self.vbo.value:
            raise RuntimeError("Could not create VBO")
        gl.glBindBuffer(gl.GL_ARRAY_BUFFER, self.vbo)
        gl.glBufferData(gl.GL_ARRAY_BUFFER, self.vertexCount * 3 * 4,
                        vertexCArray, gl.GL_STATIC_DRAW)
        gl.glBindBuffer(gl.GL_ARRAY_BUFFER, 0)
        error = gl.glGetError()
        if error:
            print('Errors:', error)
    def render(self):
        gl.glClear(gl.GL_COLOR_BUFFER_BIT)
        gl.glBindBuffer(gl.GL_ARRAY_BUFFER, self.vbo)
        gl.glEnableVertexAttribArray(0)
        gl.glVertexAttribPointer(0, 3, gl.GL_FLOAT, False, 0, 0)
        gl.glDrawArrays(gl.GL_TRIANGLES, 0, self.vertexCount)
        gl.glDisableVertexAttribArray(0)
        gl.glBindBuffer(gl.GL_ARRAY_BUFFER, 0)
        error = gl.glGetError()
        if error:
            print('Errors:', error)

def run(renderable):
    # adapted from GLFW docs
    if not glfw.init():
        raise RuntimeError("Failed to init GLFW")

    window = glfw.create_window(640, 480, "Hello World", None, None)
    try:
        if not window:
            raise RuntimeError
        glfw.make_context_current(window)
        gl.loadGL(glfw.get_proc_address)
        renderable.setup(window)
        gl.glClearColor(0.5, 0.25, 1.0, 1.0)

        while not glfw.window_should_close(window):
            # do gl stuff
            renderable.render()
            # end gl stuff
            glfw.swap_buffers(window)
            glfw.poll_events()
    finally:
        glfw.terminate()

if __name__ == "__main__":
    run(TestOpenGL1())
    run(TestOpenGL2_1())
