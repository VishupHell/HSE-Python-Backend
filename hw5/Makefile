PIP := .venv/bin/pip
PYTHON3 = python3
MANAGE = $(PYTHON3) manage.py

run:
	$(MANAGE) runserver

migrate:
	$(MANAGE) migrate

# Создание новых миграций
makemigrations:
	$(MANAGE) makemigrations