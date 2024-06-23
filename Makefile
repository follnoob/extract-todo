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

# .PHONY: major
# major: # Bump version
# 	@bumpversion major --allow-dirty

# .PHONY: minor
# minor: # Bump version
# 	@bumpversion minor --allow-dirty

# .PHONY: patch
# patch: # Bump version
# 	@bumpversion patch --allow-dirty

.PHONY: clean
clean:
	@-rm -rf dist
	@-rm -rf build
	@-rm -rf src/*.egg-info