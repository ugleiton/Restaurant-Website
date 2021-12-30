.PHONY: secret-key
secret-key:
	docker exec kuttadmin sh -c "python -c 'from django.core.management.utils import get_random_secret_key; print(get_random_secret_key())'"

.PHONY: build-base
build-base:
	docker build -t registry.gitlab.com/ugleiton/foodmenu:base -f Dockerfile-base .

.PHONY: build
build:
	docker build -t registry.gitlab.com/ugleiton/foodmenu:latest .

.PHONY: up
up:
	docker-compose -f docker-compose-dev.yml up -d
	docker-compose -f docker-compose-dev.yml logs -f foodmenu

.PHONY: down
down:
	docker-compose -f docker-compose-dev.yml down

.PHONY: restart
restart:
	docker-compose -f docker-compose-dev.yml restart


#7C4ued6eNCrZce7y

