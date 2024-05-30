.PHONY: build up down create-migration migrate create-superuser shell

build:
	docker-compose build

up:
	docker-compose up -d

down:
	docker-compose down

create-migration:
	docker-compose exec web python manage.py makemigrations

migrate:
	docker-compose exec web python manage.py migrate

create-superuser:
	docker-compose exec web python manage.py createsuperuser

shell:
	docker-compose exec web python manage.py shell

