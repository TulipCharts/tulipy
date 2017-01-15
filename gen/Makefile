all: gen

build:
	python setup.py build_ext --inplace

gen: build
	python gen.py --output-dir='../tulipy'

clean:
	rm -rf ./build ./*.c ./*.so

