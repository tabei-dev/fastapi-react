rm-migrations:
	rm -rf ./migration/versions/*
init-migrations:
	pipenv run alembic revision --autogenerate -m "initial migration"
upgrade-head:
	pipenv run alembic upgrade head