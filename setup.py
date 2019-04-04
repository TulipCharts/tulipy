from setuptools import setup, find_packages
from distutils.extension import Extension

import numpy as np
from Cython.Distutils import build_ext

with open('README.md') as f:
    long_description = f.read()

ext_modules = [
    Extension(name='tulipy.lib',
              sources=['libindicators/tiamalgamation.c', 'tulipy/lib/__init__.pyx'],
              language='c',
              include_dirs=['libindicators', 'tulipy/lib', np.get_include()],
    )
]

setup(
    name='tulipy',
    description='Financial Technical Analysis Indicator Library. Python bindings for https://github.com/TulipCharts/tulipindicators',
    long_description=long_description,
    long_description_content_type='text/markdown',
    version='0.3.1',
    url='https://github.com/cirla/tulipy',
    author='https://github.com/cirla/tulipy/blob/master/AUTHORS',
    license='LGPL-3.0',
    cmdclass={'build_ext': build_ext},
    ext_modules=ext_modules,
    packages=find_packages(exclude=["tests"]),
    install_requires=['numpy', 'pandas'],
    setup_requires=['Cython', 'numpy', 'pandas'],
    classifiers=[
        'Development Status :: 4 - Beta',
        'Intended Audience :: Developers',
        'Intended Audience :: Financial and Insurance Industry',
        'License :: OSI Approved :: GNU Lesser General Public License v3 (LGPLv3)',
        'Operating System :: OS Independent',
        'Programming Language :: Cython',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 3',
        'Topic :: Office/Business :: Financial',
        'Topic :: Scientific/Engineering :: Information Analysis',
    ],
)

