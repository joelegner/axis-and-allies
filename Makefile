SHELL := /bin/zsh

export PIPENV_IGNORE_VIRTUALENVS=1

.PHONY: run
run: build
	pipenv run python axisandallies

.PHONY: build
build: clean
	@echo "TODO: Add any build code to Makefile."

.PHONY: clean
clean:
	@echo "TODO: Add cleaning code to Makefile."

.PHONY: test
test: mypy
	pipenv run pytest --cov=axisandallies --cov-report html

.PHONY: coverage
coverage: test
	open htmlcov/index.html

.PHONY: mypy
mypy:
	pipenv run mypy axisandallies