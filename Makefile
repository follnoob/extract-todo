# Config
PYTHON=python
PYPI_SERVER=pypi

.PHONY: dist
dist: sdist wheel

.PHONY: wheel
wheel:
	@${PYTHON} setup.py bdist_wheel

.PHONY: sdist
sdist:
	@${PYTHON} setup.py sdist

.PHONY: tests
tests: # Run tests
	@${PYTHON} -m nose

.PHONY: major
major: # Bump version
	@bumpversion major

.PHONY: minor
minor: # Bump version
	@bumpversion minor

.PHONY: patch
patch: # Bump version
	@bumpversion patch

.PHONY: release
release: clean dist # Package and upload release
	@twine upload -r $(PYPI_SERVER) dist/*

.PHONY: clean
clean:
	@-rm -rf dist
	@-rm -rf build
	@-rm -rf *.egg-info