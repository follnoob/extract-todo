VERSION=minor
.PHONY: all dist sdist wheel bump test
all: dist

dist: sdist wheel

wheel:
	python setup.py bdist_wheel

sdist:
	python setup.py sdist

# Run tests
test:
	python3 -m nose

# Bump version
bump:
	bumpversion ${VERSION}

# Clean environment
clean:
	-rm -rf dist
	-rm -rf build
	-rm -rf *.egg-info