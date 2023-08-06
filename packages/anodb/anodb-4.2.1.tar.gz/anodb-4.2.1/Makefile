.ONESHELL:

.PHONY: check
check: venv
	. venv/bin/activate
	type python3
	mypy anodb.py
	flake8 --ignore=E127 anodb.py
	cd test && make check

.PHONY: clean clean-venv
clean:
	$(RM) -r __pycache__ */__pycache__ *.egg-info dist build .mypy_cache .pytest_cache

clean-venv:
	$(RM) -r venv

.PHONY: install
install:
	pip3 install -e .

venv:
	python3 -m venv venv
	venv/bin/pip install wheel pytest coverage
	venv/bin/pip install pytest-postgresql psycopg2 psycopg pymysql
	venv/bin/pip install -e .

dist:
	python3 setup.py sdist bdist_wheel

.PHONY: publish
publish: dist
	# provide pypi login/pw…
	twine upload --repository anodb dist/*
