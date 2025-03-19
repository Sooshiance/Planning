VENV = ./.venv
YARN = yarn
PYTHON = $(VENV)/bin/python3.11
MANAGE = $(PYTHON) ./backend/manage.py

.PHONY: install
install:
	@if [ ! -f "$(VENV)/bin/activate" ]; then \
		echo "Creating virtual environment"; \
		python3.11 -m venv $(VENV); \
		$(PYTHON) -m pip install -r ./backend/requirements/base.txt; \
		$(PYTHON) -m pip install -r ./backend/requirements/development.txt; \
	else \
		echo "Virtual environment already exists. Skipping creation."; \
		$(PYTHON) -m pip install -r ./backend/requirements/base.txt; \
		$(PYTHON) -m pip install -r ./backend/requirements/development.txt; \
	fi

.PHONY: migrations
migrations:
	$(MANAGE) makemigrations

.PHONY: migrate
migrate:
	$(MANAGE) migrate

.PHONY: superuser
superuser:
	$(MANAGE) createsuperuser

.PHONY: test
test:
	$(MANAGE) test

.PHONY: run
run:
	$(MANAGE) runserver

.PHONY: start
start:
	$(YARN) start

clean:
	echo "Cleaning up __pycache__ and other unnecessary files..."
	find . -type d -name '__pycache__' -exec rm -rf {} + || true
	find . -type d -name '*.egg-info' -exec rm -rf {} + || true
	find . -type d -name '.pytest_cache' -exec rm -rf {} + || true
	echo "Cleanup complete."