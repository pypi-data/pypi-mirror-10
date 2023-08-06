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

upload:
	python3 setup.py sdist upload
