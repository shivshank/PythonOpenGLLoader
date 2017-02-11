# Another Way to use OpenGL in Python

I've written this mostly for fun.

Not for use just yet. Only tested up to OpenGL 2.1. No support for extensions.

Dead simple Windows only OpenGL loader, generated from the [Khronos XML spec](https://cvs.khronos.org/svn/repos/ogl/trunk/doc/registry/public/api), inspired from and based off of [glad](https://github.com/Dav1dde/glad).

There are no convenience functions (for now). Most will require using ctypes directly.

# Usage

Generate a gl module by running the lib module, i.e. `python -m lib`. To modify what functions are available you will need to modify \_\_main\_\_.py (CLI is TODO).

```
gl.loadGL([loader])
```

`loadGL` will load as many OpenGL functions as possible. `loader` is an optional argument and must be a callable that takes a Python String and either returns a valid function address or a ctypes FuncPtr.

And then you just... use OpenGL.

# Examples

Examples will require that a [GLFW wrapper](https://github.com/FlorianRhiem/pyGLFW) (such as Flroian Rhiem's) is on the module path. This will likewise require GLFW to be accessible. Notice that the chosen wrapper uses its own naming conventions.
