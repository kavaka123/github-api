.PHONY: clean

GIT_COMMIT_SHA := $(shell git rev-parse --short HEAD)
SERVICE_NAME := github-api

docker/tests: clean
	docker build -t ${SERVICE_NAME}-test:${GIT_COMMIT_SHA} -f Dockerfile.test .
	docker run --rm ${SERVICE_NAME}-test:${GIT_COMMIT_SHA}

docker/build: docker/tests
	docker build -t ${SERVICE_NAME}:${GIT_COMMIT_SHA} .

docker/run: docker/build
	docker run -d -p 8080:8080 --name ${SERVICE_NAME}-service ${SERVICE_NAME}:${GIT_COMMIT_SHA}

clean:
	docker rm -f ${SERVICE_NAME}-service || true
	docker rmi ${SERVICE_NAME}:${GIT_COMMIT_SHA} || true
	docker rmi ${SERVICE_NAME}-test:${GIT_COMMIT_SHA} || true
	docker rm -f ${SERVICE_NAME}-test || true