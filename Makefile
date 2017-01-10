all:
	python setup.py build_ext --inplace --include-dir ../tulipindicators --lib-path ../tulipindicators/libindicators.a

clean:
	rm -rf ./build tulipy.so src/tulipy.c

