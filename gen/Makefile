all: gen

build:
	python3 setup.py build_ext --inplace

gen: build
	python3 gen.py --output-dir='../tulipy'

clean:
	rm -rf ./build ./*.c ./*.so

