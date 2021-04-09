all: gen

gen: build
	@echo '---> gen'
	python gen.py --output-dir='../tulipy'

build:
	@echo '---> build'
	python setup.py build_ext --inplace

clean:
	@echo '---> clean'
	rm -rf ./build ./*.c ./*.so

