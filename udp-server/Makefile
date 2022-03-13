SERVER_VERSION ?= 'v1'
SERVER_PORT ?= '2000'

HUB ?= 'localhost:5000'
TAG ?= 'app'

run:
	SERVER_VERSION=$(SERVER_VERSION) SERVER_PORT=$(SERVER_PORT) python3 udp.py

docker:
	docker build -t $(HUB)/udp-echo:$(TAG) .
	docker push $(HUB)/udp-echo:$(TAG)