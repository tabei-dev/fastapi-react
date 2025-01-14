up:
	docker compose up
upd:
	docker compose up -d
build:
	docker compose build --no-cache --force-rm
stop:
	docker compose stop
down:
	docker compose down --remove-orphans
down-v:
	docker compose down --remove-orphans --volumes
restart:
	@make down
	@make upd
destroy:
	docker compose down --rmi all --volumes --remove-orphans
prune-volumes:
	docker volume prune -f
ps:
	docker compose ps
logs:
	docker compose logs
logs-watch:
	docker compose logs --follow
# log-web:
# 	docker compose logs web
# log-web-watch:
# 	docker compose logs --follow web
log-backend:
	docker compose logs backend
log-backend-watch:
	docker compose logs --follow backend
log-frontend:
	docker compose logs frontend
log-frontend-watch:
	docker compose logs --follow frontend
log-db:
	docker compose logs db
log-db-watch:
	docker compose logs --follow db

# web:
# 	docker compose exec web ash
# pytest-%:
# 	docker compose exec web pytest ${@:pytest-%=%}

backend-bash:
	docker compose exec backend bash
pip-ig:
	docker compose exec backend pip install -U pip
pip-install:
	docker compose exec backend pip install -r requirements.txt
pip-install-%:
	docker compose exec backend pip install ${@:pip-install-%=%}
pip-uninstall-%:
	docker compose exec backend pip uninstall ${@:pip-uninstall-%=%}
pytest:
	docker compose exec backend pytest -s tests/
mypy:
	docker compose exec backend mypy .
rm-migrations:
	rm -rf apps/backend/alembic/versions/*
	docker compose exec backend rm -rf alembic/versions/*
init-migrations:
	docker compose exec backend pipenv run alembic revision --autogenerate -m "initial migration"
upgrade-head:
	docker compose exec backend pipenv run alembic upgrade head
seed:
	docker compose exec backend python3 alembic/seed.py
init-db:
	mkdir -p apps/backend/alembic/versions
	@make db-reset
	@make rm-migrations
	@make init-migrations
	@make upgrade-head
	@make seed

# 仮想環境を初期化するターゲット
init-venv:
	python3 -m venv venv
	source venv/bin/activate && pip install -r apps/backend/requirements.txt
# 仮想環境をアクティベートして依存関係をインストールするターゲット
pip-install-venv:
	source venv/bin/activate && pip install -r apps/backend/requirements.txt

frontend-bash:
	docker compose exec frontend bash
npm-ig:
	docker compose exec frontend npm i -g npm
npm-install:
	docker compose exec frontend npm install
npm-update:
	cd apps/frontend && ncu -u
	@make npm-install
# docker compose exec frontend npm-check-updates -u
npm-dev:
	docker compose exec frontend npm run dev
npm-build:
	docker compose exec frontend npm run build
npm-build-watch:
	docker compose exec frontend npm run build:watch
npm-preview:
	docker compose exec frontend npm run preview
# npm-hot:
# 	docker compose exec frontend npm run hot
# npm-eslint:
# 	docker compose exec frontend npm run eslint
npm-lint:
	docker compose exec frontend npm run lint
npm-lintfix:
	docker compose exec frontend npm run lint -- --fix
# npm-format:
# 	docker compose exec frontend npm run format
npm-test:
	docker compose exec frontend npm run test
npm-test-watch:
	docker compose exec frontend npm run test -- --watch
# npm-check-updates:
# 	docker compose exec frontend npx -p npm-check-updates -c "ncu"
# npm-update:
# 	docker compose exec frontend npx -p npm-check-updates -c "ncu -u"

db-bash:
	docker compose exec db bash
# sql:
# 	docker compose exec db bash -c 'mysql -u $$MYSQL_USER -p$$MYSQL_PASSWORD $$MYSQL_DATABASE'
# redis:
# 	docker compose exec redis redis-cli
db-reset:
	@make down-v
	@make upd

