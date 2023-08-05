pytest_bin := py.test
pytest_opts := --doctest-modules --ignore=rhino/vendor
coverage_opts := --cov=rhino --cov=examples --cov-report=term --cov-report=html
test_cmd := $(pytest_bin) $(pytest_opts)
test_targets := test/ rhino/

test:
	$(test_cmd) $(test_targets)

cover:
	$(test_cmd) $(coverage_opts) $(test_targets)

build: test
	rm dist/*.tar.gz
	python setup.py sdist
	rm -rf /tmp/rhino-sdist
	virtualenv /tmp/rhino-sdist
	/tmp/rhino-sdist/bin/pip install dist/*.tar.gz
	/tmp/rhino-sdist/bin/python -c 'import rhino; print rhino.__version__'

testpypi: build
	python setup.py sdist upload -r test
	rm -rf /tmp/rhino-testpypi
	virtualenv /tmp/rhino-testpypi
	/tmp/rhino-testpypi/bin/pip install -i https://testpypi.python.org/pypi rhino
	/tmp/rhino-testpypi/bin/python -c 'import rhino; print rhino.__version__'

release: testpypi
	python setup.py sdist upload -r pypi
	rm -rf /tmp/rhino-pypi
	virtualenv /tmp/rhino-pypi
	/tmp/rhino-pypi/bin/pip install rhino
	/tmp/rhino-pypi/bin/python -c 'import rhino; print rhino.__version__'

.PHONY: test cover build testpypi release

README.rst: README.mkd
	pandoc --from=markdown --to=rst $< > $@
