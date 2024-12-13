rm-migrations:
	rm -rf ./alembic/versions/*
init-migrations:
	pipenv run alembic revision --autogenerate -m "initial migration"
upgrade-head:
	pipenv run alembic upgrade head