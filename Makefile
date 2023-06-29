include .env

dev: stop start

stop:
	docker-compose down

start:
	docker-compose up -d --build
	docker-compose exec store python manage.py migrate --settings=floship_test.settings.settings_store
	docker-compose exec warehouse python manage.py migrate --settings=floship_test.settings.settings_warehouse