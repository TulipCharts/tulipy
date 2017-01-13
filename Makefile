build:
	python setup.py build_ext --inplace

clean:
	rm -rf ./build ./dist ./*.so ./src/tulipy.pyx ./src/*.c ./*.egg-info

install:
	python setup.py install

test: install
	python tests/test.py

