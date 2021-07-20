build:
	python3 setup.py build_ext --inplace

clean:
	rm -rf ./build ./dist \
		   ./tulipy/*.so ./tulipy/*.pyc \
		   ./tulipy/lib/*.c \
		   ./*.egg-info

install:
	python3 setup.py install

test: install
	python3 tests/test.py

