DOCKER_COMPOSE = docker compose -f docker-compose.yaml
CONTAINERS = yus_auto_api yus_auto_pgadmin yus_auto_database

build:
	$(DOCKER_COMPOSE) build --pull --no-cache

up:
	$(DOCKER_COMPOSE) up --detach --wait

down:
	$(DOCKER_COMPOSE) down

up-debug:
	$(DOCKER_COMPOSE) up

clean: down
	docker rmi $(CONTAINERS) || exit 0

stop:
	docker stop $(CONTAINERS)

rm-containers: stop
	docker rm $(CONTAINERS)

full-clean: rm-containers
	docker image prune -af
	docker system prune -af
	docker volume prune -af