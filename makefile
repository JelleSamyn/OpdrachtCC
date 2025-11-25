PROJECT_NAME=opdrachtcc
DC=docker compose

.PHONY: up down restart logs build clean-volumes

up:
	$(DC) up -d --build

down:
	$(DC) down

restart: down up

logs:
	$(DC) logs -f

build:
	$(DC) build

clean-volumes:
	$(DC) down -v
