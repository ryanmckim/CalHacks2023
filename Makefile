BACKEND_DIR = backend
FRONTEND_DIR = frontend
BACKEND_IMAGE_NAME = tuneai-app-api
FRONTEND_IMAGE_NAME = tuneai-app-client

API_SERVICE = api
CLIENT_SERVICE = client

build:
    docker-compose build

run:
    docker-compose up -d

stop:
    docker-compose down

clean:
    docker-compose down --rmi all --volumes --remove-orphans

run-backend:
    docker-compose up -d $(API_SERVICE)

run-frontend:
    docker-compose up -d $(CLIENT_SERVICE)