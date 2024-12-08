up:
	docker compose up
build:
	docker compose build --no-cache --force-rm
# composer-update:
# 	docker compose exec app composer update
# laravel-install:
# 	docker compose exec app composer create-project --prefer-dist laravel/laravel .
# install-recommend-packages:
# 	docker compose exec app composer require bensampo/laravel-enum
# key-generate:
# 	docker compose exec app php artisan key:generate
# chmod:
# 	docker compose exec app chmod -R 777 storage bootstrap/cache
# create-project:
# 	@make laravel-install
# 	@make key-generate
# 	docker compose exec app php artisan storage:link
# 	@make chmod
# install-react:
# 	docker compose exec app composer require laravel/ui
# 	docker compose exec app php artisan ui react --auth
# install-ts:
# 	docker compose exec app npm install -D @types/node @types/react @types/react-dom @types/react-router-dom
# install-react-packages:
# 	docker compose exec app npm install -D react-router-dom change-case react-hook-form zod @hookform/resolvers swr @linaria/core @linaria/react @linaria/babel-preset @linaria/rollup @linaria/server @microsoft/tsdoc react-loader-spinner jspdf html2canvas exceljs
# install-eslint:
# 	docker compose exec app npm install -D eslint eslint-config-airbnb eslint-config-airbnb-typescript eslint-plugin-react eslint-plugin-react-hooks
# install-test-packages:
# 	docker compose exec app npm install -D jest @types/jest ts-jest @testing-library/react @testing-library/jest-dom @testing-library/user-event linaria-jest jest-environment-jsdom eslint-plugin-jest eslint-plugin-jest-dom eslint-plugin-testing-library
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
ps:
	docker compose ps
logs:
	docker compose logs
logs-watch:
	docker compose logs --follow
log-web:
	docker compose logs web
log-web-watch:
	docker compose logs --follow web
log-app:
	docker compose logs app
log-app-watch:
	docker compose logs --follow app
log-db:
	docker compose logs db
log-db-watch:
	docker compose logs --follow db
web:
	docker compose exec web ash
pytest-%:
	docker compose exec web pytest ${@:pytest-%=%}
app:
	docker compose exec api bash
# make-migration-%:
# 	docker compose exec app php artisan make:migration create_${@:make-migration-%=%}_table
# migrate:
# 	docker compose exec app php artisan migrate
# fresh:
# 	docker compose exec app php artisan migrate:fresh --seed
# make-model-%:
# 	docker compose exec app php artisan make:model ${@:make-model-%=%}
# make-seeder-%:
# 	docker compose exec app php artisan make:seeder ${@:make-seeder-%=%}
# seed:
# 	docker compose exec app php artisan db:seed
# make-controller-%:
# 	docker compose exec app php artisan make:controller ${@:make-controller-%=%}
# make-api-controller-%:
# 	docker compose exec app php artisan make:controller ${@:make-api-controller-%=%} --api
# make-resource-controller-%:
# 	docker compose exec app php artisan make:controller ${@:make-resource-controller-%=%} --resource
# make-request-%:
# 	docker compose exec app php artisan make:request ${@:make-request-%=%}
# dacapo:
# 	docker compose exec app php artisan dacapo
# rollback-test:
# 	docker compose exec app php artisan migrate:fresh
# 	docker compose exec app php artisan migrate:refresh
# tinker:
# 	docker compose exec client php artisan tinker
# make-test-%:
# 	docker compose exec client php artisan make:test ${@:make-test-%=%} --pest
# make-unit-test-%:
# 	docker compose exec client php artisan make:test ${@:make-unit-test-%=%} --unit --pest
# test:
# 	docker compose exec client php artisan test
# # test-class:
# # 	docker compose exec client ./vendor/bin/phpunit -v ${class}
# test-unit:
# 	docker compose exec client php artisan test --testsuite=Unit
# test-feature:
# 	docker compose exec client php artisan test --testsuite=Feature
# optimize:
# 	docker compose exec client php artisan optimize
# optimize-clear:
# 	docker compose exec client php artisan optimize:clear
# cache:
# 	docker compose exec client composer dump-autoload -o
# 	@make optimize
# 	docker compose exec client php artisan event:cache
# 	docker compose exec client php artisan view:cache
# cache-clear:
# 	docker compose exec client composer clear-cache
# 	@make optimize-clear
# 	docker compose exec client php artisan event:clear
# 	docker compose exec client php artisan cache:clear
# 	docker compose exec client php artisan config:clear
deno-dev:
	docker compose exec frontend deno run dev
# deno-watch:
# 	docker compose exec client deno run --allow-env --allow-net --watch src/index.tsx
npm-ig:
	docker compose exec frontend npm i -g npm
npm-install:
	docker compose exec frontend npm install
npm-update:
	cd src
	docker compose exec frontend npm-check-updates -u
npm-dev:
	docker compose exec frontend npm run dev
npm-build:
	docker compose exec frontend npm run build
npm-build-watch:
	docker compose exec frontend npm run build:watch
npm-preview:
	docker compose exec frontend npm run preview
# npm-hot:
# 	docker compose exec web npm run hot
# npm-eslint:
# 	docker compose exec web npm run eslint
npm-lint:
	docker compose exec client npm run lint
npm-lintfix:
	docker compose exec client npm run lint -- --fix
# npm-format:
# 	docker compose exec app npm run format
npm-test:
	docker compose exec client npm run test
npm-test-watch:
	docker compose exec client npm run test -- --watch
# npm-check-updates:
# 	docker compose exec app npx -p npm-check-updates -c "ncu"
# npm-update:
# 	docker compose exec app npx -p npm-check-updates -c "ncu -u"
db:
	docker compose exec db bash
sql:
	docker compose exec db bash -c 'mysql -u $$MYSQL_USER -p$$MYSQL_PASSWORD $$MYSQL_DATABASE'
redis:
	docker compose exec redis redis-cli
# ide-helper:
# 	docker compose exec app php artisan clear-compiled
# 	docker compose exec app php artisan ide-helper:generate
# 	docker compose exec app php artisan ide-helper:meta
# 	docker compose exec app php artisan ide-helper:models --nowrite
