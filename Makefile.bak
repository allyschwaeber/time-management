.PHONY:init
init:
	pipenv shell --python 3.8

.PHONY: install
install:
	pipenv install

.PHONY: format
format:
	black .

.PHONY: lint
lint:
	flake8 . --ignore=E501

.PHONY: clean
clean:
	find . -name '*.pyc' -exec rm --force {} +
	find . -name '*.pyo' -exec rm --force {} +

.PHONY: test
test:
	python -m unittest discover time_management "*_test.py"

.PHONY: cover
cover:
	coverage run -m --source=./time_management/ unittest discover time_management "*_test.py"
	coverage report
	coverage html

.PHONY: run
run:
	python3 time_management/main.py

.PHONY: remove
remove:
	pipenv --rm