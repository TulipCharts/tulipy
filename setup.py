import argparse
import sys

from distutils.core import setup
from distutils.extension import Extension

import numpy as np
from Cython.Distutils import build_ext

parser = argparse.ArgumentParser(description='tulipy setup')
parser.add_argument('--include-dir', type=str, default='/usr/local/include',
                    help='include directory containing indicators.h')
parser.add_argument('--lib-path', type=str, default='/usr/local/lib/libindicators.a',
                    help='full path to libindicators.a')

args, _ = parser.parse_known_args()

for a in ['--include-dir', '--lib-path']:
    try:
        i = sys.argv.index(a)
        v = sys.argv[i + 1]
        sys.argv.remove(a)
        sys.argv.remove(v)
    except:
        pass

ext_modules = [
    Extension(name='tulipy',
              sources=['src/tulipy.pyx'],
              language='c',
              include_dirs=['src', np.get_include(), args.include_dir],
              extra_objects=[args.lib_path])
]

setup(
    name='tulipy',
    cmdclass={'build_ext': build_ext},
    ext_modules=ext_modules,
)

