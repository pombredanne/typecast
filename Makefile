
test: install
	env/bin/nosetests --with-coverage --cover-package=typecast --cover-erase

install: env/bin/python

env/bin/python:
	virtualenv env
	env/bin/pip install --upgrade pip
	env/bin/pip install -e .
	env/bin/pip install nose coverage wheel

upload:
	env/bin/python setup.py sdist bdist_wheel upload

clean:
	rm -rf env
