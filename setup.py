from setuptools import setup, find_packages
from distutils.extension import Extension

import numpy as np
from Cython.Build import cythonize
from Cython.Distutils import build_ext

with open('README.md') as f:
    long_description = f.read()

ext_modules = [
    Extension(
        name='tulipy.lib',
        language='c++',
        sources=['tulipy/lib/__init__.pyx',
                 'libindicators/tiamalgamation.c',
                 'libindicators/pst_indicators/pst_indicators.cpp',
                 'libindicators/pst_indicators/pst_manager.cpp'],
        include_dirs=['libindicators', 'libindicators/pst_indicators', 'tulipy/lib', np.get_include()],
        extra_compile_args=["-lm", "-std=c++14"],
        #library_dirs=['tulipy'],
        #libraries=['indicators'],
        #extra_link_args=["-Wl,-rpath=."],
        #extra_link_args=["-Wl,-rpath=/opt/anaconda3/lib/python3.8/site-packages/tulipy-0.4.0-py3.8-linux-x86_64.egg/tulipy"],
    )
]

setup(
    name='tulipy',
    description='Financial Technical Analysis Indicator Library. Python bindings for https://github.com/TulipCharts/tulipindicators',
    long_description=long_description,
    long_description_content_type='text/markdown; charset=UTF-8',
    version='0.4.0',
    url='https://github.com/cirla/tulipy',
    author='https://github.com/cirla/tulipy/blob/master/AUTHORS',
    license='LGPL-3.0',
    cmdclass={'build_ext': build_ext},
    ext_modules=ext_modules,
    packages=find_packages(exclude=["tests"]),
    install_requires=['numpy'],
    setup_requires=['Cython', 'numpy'],
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
