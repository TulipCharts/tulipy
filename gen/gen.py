import argparse
import os

from tulipy_gen import gen


def main():
    parser = argparse.ArgumentParser(description='Generate tulipy')
    parser.add_argument('--output-dir', type=str, default='.',
                        help='destination for generated tulipy module')

    args = parser.parse_args()

    with open(os.path.join(args.output_dir, '__init__.py'), 'w') as init_py:
        with open(os.path.join(args.output_dir, 'lib', '__init__.pyx'), 'w') as lib_pyx:
            gen(init_py, lib_pyx)


if __name__ == '__main__':
    main()

