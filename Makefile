# Config
PYTHON=python
PYPI_SERVER=pypi

build:
	@${PYTHON} -m build

.PHONY: test
test: # Run tests
	@${PYTHON} -m unittest -b

.PHONY: major
major: # Bump version
	@bumpversion major --allow-dirty

.PHONY: minor
minor: # Bump version
	@bumpversion minor --allow-dirty

.PHONY: patch
patch: # Bump version
	@bumpversion patch --allow-dirty

.PHONY: release
release: clean dist # Package and upload release
	@twine upload -r $(PYPI_SERVER) dist/*

.PHONY: clean
clean:
	@-rm -rf dist
	@-rm -rf build
	@-rm -rf src/*.egg-info