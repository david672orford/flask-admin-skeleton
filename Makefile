DOCKER_IMAGE=
DOCKER_CONTAINER=
DOCKER_NET=static
DOCKER_IP=172.18.0.X
UID=$(shell ls -ldn instance | cut -d' ' -f3)

all: pull build restart

pull:
	git pull

build:
	docker build --build-arg uid=$(UID) --tag $(DOCKER_IMAGE) .

build-no-cache:
	docker build --no-cache --build-arg uid=$(UID) --tag $(DOCKER_IMAGE) .

start:
	docker run --name $(DOCKER_CONTAINER) \
		-d --restart=always \
		--net $(DOCKER_NET) --ip $(DOCKER_IP) \
		-v /etc/localtime:/etc/localtime:ro \
		-v `pwd`/instance:/app/instance \
		$(DOCKER_IMAGE)

stop:
	docker stop $(DOCKER_CONTAINER)
	docker rm $(DOCKER_CONTAINER)

restart: stop start

shell:
	docker exec -it $(DOCKER_CONTAINER) /bin/sh

logs:
	docker logs $(DOCKER_CONTAINER)

tail:
	docker logs -f $(DOCKER_CONTAINER)


