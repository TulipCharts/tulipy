build:
	gcc -v
	python3 --version
	python3 setup.py build_ext --inplace

clean:
	rm -rf ./build ./dist \
		   ./tulipy/*.so ./tulipy/*.pyc \
		   ./tulipy/lib/*.c \
		   ./*.egg-info

install:
	python3 setup.py install
	ls -l /opt/anaconda3/lib/python3.8/site-packages/tulipy-0.4.0-py3.8-linux-x86_64.egg/tulipy/

test:
	python3 tests/test.py

