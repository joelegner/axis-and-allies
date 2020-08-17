SHELL=/bin/bash

yaml_dir = battles
yaml_files = $(wildcard $(yaml_dir)/*.yaml)
report_files = $(yaml_files:.yaml=.txt)

export PIPENV_IGNORE_VIRTUALENVS=1

.PHONY: run
run: $(report_files)

%.txt : %.yaml
	pipenv run python run.py $<

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

.PHONY: touch
touch:
	touch battles/*.yaml

.PHONY: rerun
rerun: touch run

.PHONY: docs
docs:
	# Just a simple remake of all the docs in Markdown format
	# The README.md file just points to these docs
	pdoc --force --output-dir docs axisandallies
