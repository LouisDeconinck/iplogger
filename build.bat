@echo off

REM Install dependencies
pip install -r requirements.txt

REM Create Django superuser if CREATE_SUPERUSER environment variable is set
if defined CREATE_SUPERUSER (
  echo Creating Django superuser...
  python iplogger/manage.py createsuperuser --no-input
)