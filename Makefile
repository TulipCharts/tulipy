build:
	python setup.py build_ext --inplace

clean:
	rm -rf ./build ./dist tulipy.so src/tulipy.c tulipy.egg-info

install:
	python setup.py install

test: install
	python tests/test.py

