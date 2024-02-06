#!/bin/bash

# Install dependencies
pip install -r requirements.txt

python manage.py collectstatic --no-input

# Create Django superuser if CREATE_SUPERUSER environment variable is set

echo "Creating Django superuser..."
python manage.py createsuperuser --no-input
echo "Django superuser created"
