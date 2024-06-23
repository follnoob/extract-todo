# Config
PYTHON=python

build:
	@${PYTHON} -m build

.PHONY: extract-todo
extract-todo:
	extract-todo

.PHONY: test
test: # Run tests
	@${PYTHON} -m unittest -b

.PHONY: clean
clean:
	@-rm -rf dist
	@-rm -rf build
	@-rm -rf src/*.egg-info