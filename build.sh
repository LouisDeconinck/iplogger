#!/bin/bash

# Install dependencies
pip install -r requirements.txt

# Create Django superuser if CREATE_SUPERUSER environment variable is set
if [[ $CREATE_SUPERUSER ]]; then
  echo "Creating Django superuser..."
  python iplogger/manage.py createsuperuser --no-input
fi