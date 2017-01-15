from setuptools import setup
from distutils.extension import Extension

from Cython.Distutils import build_ext

ext_modules = [
    Extension(name='tulipy_gen',
              sources=['../libindicators/tiamalgamation.c', 'tulipy_gen.pyx'],
              language='c',
              include_dirs=['../libindicators', '../tulipy/lib'],
    )
]

setup(
    name='tulipy_gen',
    cmdclass={'build_ext': build_ext},
    ext_modules=ext_modules,
)

