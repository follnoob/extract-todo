VERSION=patch
.PHONY: all dist sdist wheel version
all: dist

dist: sdist wheel

wheel:
	python setup.py bdist_wheel

sdist:
	python setup.py sdist

clean:
	-rm -rf dist
	-rm -rf build
	-rm -rf *.egg-info

version:
	bumpversion ${VERSION}