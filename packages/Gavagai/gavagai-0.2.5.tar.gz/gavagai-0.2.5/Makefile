.PHONY: clean venv install test test-install

venv:
	virtualenv venv

install: venv
	. venv/bin/activate; pip install .

test-install: install
	. venv/bin/activate; pip install -r requirements.txt

test: 
	. venv/bin/activate; py.test test

release: test-install
	. venv/bin/activate; python setup.py sdist upload

build: test-install
	. venv/bin/activate; python setup.py sdist

clean:
	rm -rf venv