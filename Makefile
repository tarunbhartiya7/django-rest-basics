run:
	docker-compose up

stop:
	docker-compose down

migrations:
	python manage.py makemigrations
	python manage.py migrate
