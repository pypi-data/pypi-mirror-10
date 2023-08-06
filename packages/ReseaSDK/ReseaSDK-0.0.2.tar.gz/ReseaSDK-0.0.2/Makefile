debug:
	py.test -v --doctest-modules --pdb reseasdk tests

test:
	py.test -v --doctest-modules reseasdk tests

ci_test:
	py.test -v --doctest-modules --cov reseasdk tests


install:
	python3 setup.py install

pep8:
	pep8 .


register:
	python3 setup.py register

release:
	if [ "$(RELEASE_VERSION)" = "" ] ; then \
        echo "error: set RELEASE_VERSION"; \
        exit 1 ; \
    fi
	echo "__version__ = '$(RELEASE_VERSION)'" > reseasdk/version.py
	git add .
	git commit -m "version $(RELEASE_VERSION)"
	git tag "v$(RELEASE_VERSION)"

upload:
	python3 setup.py sdist upload
	git push
	git push --tags
