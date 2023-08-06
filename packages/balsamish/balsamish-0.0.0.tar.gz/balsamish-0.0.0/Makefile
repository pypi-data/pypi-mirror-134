.DEFAULT_GOAL := help
.PHONY: build clean help publish test

export PYTHONPATH=./src:./test

build: ## Build the package
	@python setup.py sdist

clean: ## Remove generated artifacts
	@rm -rf build dist balsam.egg-info VERSION .eggs

help: ## Show this help
	@fgrep -h "##" $(MAKEFILE_LIST) | \
	fgrep -v fgrep | sed -e 's/## */##/' | column -t -s##

publish: ## Publish the package to PyPI (requires PYPI_USER and PYPI_PASSWORD)
	@twine upload dist/* --repository-url https://upload.pypi.org/legacy/ \
						 -u ${PYPI_USER} -p ${PYPI_PASSWORD} \
						 --skip-existing

test: ## Test the package
	@python setup.py pytest

version: ## Write the version file
	@git describe --tags --exact-match > VERSION
