build:
	python setup.py build_ext --inplace

clean:
	rm -rf ./build ./dist \
		   ./tulipy/*.so ./tulipy/*.pyc \
		   ./tulipy/lib/*.c \
		   ./*.egg-info

install:
	python setup.py install

test: install
	python tests/test.py

