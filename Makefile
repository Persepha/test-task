pip-install-dev:
	pip install --upgrade pip pip-tools
	pip-compile requirements/dev.in -o web/requirements-dev.txt
	pip-sync web/requirements-dev.txt

pip-install:
	pip install --upgrade pip pip-tools
	pip-compile requirements/base.in -o web/requirements.txt
	pip-sync web/requirements.txt

pip-update:
	pip install --upgrade pip pip-tools
	pip-compile requirements/base.in -o web/requirements.txt
	pip-compile requirements/dev.in -o web/requirements-dev.txt
	pip-sync web/requirements.txt web/requirements-dev.txt

build-server:
	docker-compose up -d --build

server:
	docker-compose up

down-server:
	docker-compose down

docker-collectstatic:
	docker-compose exec web /opt/venv/bin/python manage.py collectstatic --no-input

docker-migrations:
	docker-compose exec web /opt/venv/bin/python manage.py makemigrations

docker-migrate:
	docker-compose exec web /opt/venv/bin/python manage.py migrate

test-coverage:
	docker-compose exec web /opt/venv/bin/coverage run --source="." manage.py test .

coverage-html:
	docker-compose exec web /opt/venv/bin/coverage