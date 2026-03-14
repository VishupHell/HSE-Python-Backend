PIP := .venv/bin/pip
PYTHON3 = python3
MANAGE = $(PYTHON3) manage.py

run:
	docker-compose up -d --build
	$(MANAGE) runserver

migrate:
	$(MANAGE) migrate

# Создание новых миграций
makemigrations:
	$(MANAGE) makemigrations

superuser:
	$(MANAGE) createsuperuser

tests:
	$(MANAGE) test
