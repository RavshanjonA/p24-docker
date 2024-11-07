user:
	python3 manage.py createsuperuser
mig:
	python3 manage.py makemigrations
migrate:
	python3 manage.py migrate
up:
	docker compose up
build:
	docker compose build
down:
	docker compose down -v
up-d:
	docker compose up -d
up-build-d:
	docker compose up --build -d
