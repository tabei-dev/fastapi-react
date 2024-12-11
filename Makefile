up:
	docker compose up
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
	@make up
destroy:
	docker compose down --rmi all --volumes --remove-orphans
prune-volumes:
	docker volume prune -f
ps:
	docker compose ps
ps-a:
	docker compose ps -a
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

backend:
	docker compose exec backend sh
pip-ig:
	docker compose exec backend pip install -U pip
pip-install:
	docker compose exec backend pip install -r requirements.txt
pytest:
	docker compose exec backend pytest tests/

frontend:
	docker compose exec frontend sh
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

db:
	docker compose exec db bash
sql:
	docker compose exec db bash -c 'mysql -u $$MYSQL_USER -p$$MYSQL_PASSWORD $$MYSQL_DATABASE'
redis:
	docker compose exec redis redis-cli
