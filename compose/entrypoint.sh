#!/bin/bash

echo "Starting entrypoint script..."

# Wait for the database to be ready
echo "Waiting for database..."
while ! nc -z "$MYSQL_HOST" "$MYSQL_PORT";
  do sleep 1
  done
echo "Database is ready."

# Apply database migrations
echo "Applying database migrations..."
python django_backend/manage.py migrate --noinput

# Collect static files
# echo "Collecting static files..."
# python src/manage.py collectstatic --noinput

# Start the server using the command passed to the container
echo "Starting server..."
exec "$@"