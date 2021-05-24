pwd=$(shell pwd)
home=$(HOME)

build:
	docker-compose build

up: build
	docker-compose up

down:
	docker-compose kill
	docker-compose rm -f

flake8:
	python -m flake8 $(pwd)/linkgraph_app/

test:
	python $(pwd)/linkgraph/manage.py test