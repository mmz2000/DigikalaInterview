#!/bin/sh

echo "Waiting for postgres..."

while ! nc -z $DEFAULT_DATABASE_HOST $DEFAULT_DATABASE_PORT; do
  sleep 0.1
done

echo "PostgreSQL started"

exec "$@"

/usr/sbin/crond -f -l 8
# python manage.py flush --no-input
# python manage.py migrate
