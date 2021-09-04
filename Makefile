.PHONY: all \
		setup \
		run \
		black \
		flake8 \
		mypy

venv/bin/activate: ## alias for virtual environment
	python -m venv venv

setup: venv/bin/activate ## project setup
	. venv/bin/activate; pip install pip wheel setuptools
	. venv/bin/activate; pip install -r requirements.txt

run: venv/bin/activate ## run project
	. venv/bin/activate; python app.py

lint: venv/bin/activate ## lint
	. venv/bin/activate; black .
	. venv/bin/activate; flake8 .
	. venv/bin/activate; mypy .
	. venv/bin/activate; isort .
