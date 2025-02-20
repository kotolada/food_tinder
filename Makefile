SHELL = /bin/bash

.DEFAULT_GOAL := up

# Build the Docker images using the compose file
build:
	@echo "Building Docker images..."
	docker-compose -f docker-compose.yml build

# Start the containers in detached mode and tail the logs
up: 
	@echo "Starting containers..."
	docker-compose -f docker-compose.yml up -d && docker-compose -f docker-compose.yml logs -f --tail=10

# Update (restart a specific service, here 'bot') then bring the services up
update:
	@echo "Restarting 'bot' service and updating containers..."
	docker-compose -f docker-compose.yml restart django_backend && make up

# Stop all containers defined in the compose file
stop:
	@echo "Stopping containers..."
	docker-compose -f docker-compose.yml stop

# Shut down and remove containers, networks, etc.
down:
	@echo "Taking down the Docker environment..."
	docker-compose -f docker-compose.yml down

createsuperuser:
	@echo "Creating superuser..."
	docker-compose -f docker-compose.yml exec web python django_backend/manage.py createsuperuser