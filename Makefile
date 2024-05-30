.PHONY: build up down migrate createsuperuser

build:
    docker-compose build

up:
    docker-compose up

down:
    docker-compose down

migrate:
    docker-compose exec web python manage.py migrate

createsuperuser:
    docker-compose exec web python manage.py createsuperuser

