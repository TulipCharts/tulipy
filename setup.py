from distutils.core import setup
from distutils.extension import Extension

import numpy as np
from Cython.Distutils import build_ext

ext_modules = [
    Extension(name='tulipy',
              sources=['libindicators/tiamalgamation.c', 'src/tulipy.pyx'],
              language='c',
              include_dirs=['libindicators', 'src', np.get_include()],
    )
]

setup(
    name='tulipy',
    cmdclass={'build_ext': build_ext},
    ext_modules=ext_modules,
)

