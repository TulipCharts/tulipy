from setuptools import setup
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
    description='Python bindings for https://github.com/TulipCharts/tulipindicators',
    version=0.1,
    url='https://github.com/cirla/tulipy',
    author='Tim Cheeseman <tim@timcheeseman.com>',
    license='LGPL-3.0',
    cmdclass={'build_ext': build_ext},
    ext_modules=ext_modules,
    setup_requires=['cython', 'numpy'],
    requires=['numpy'],
)

