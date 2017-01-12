all:
	python setup.py build_ext --inplace

clean:
	rm -rf ./build ./dist tulipy.so src/tulipy.c tulipy.egg-info

