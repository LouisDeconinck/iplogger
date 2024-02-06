#!/bin/bash

# Install dependencies
pip install -r requirements.txt

python manage.py collectstatic --no-input

# Create Django superuser if CREATE_SUPERUSER environment variable is set
if [[ $CREATE_SUPERUSER ]]; then
  echo "Creating Django superuser..."
  python iplogger/manage.py createsuperuser --no-input
  echo "Django superuser created"
fi