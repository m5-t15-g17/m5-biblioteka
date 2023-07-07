#!/usr/bin/env bash
#exit in error
set -o errexit

pip install -r requirements.txt
python manage.py collectstatic --no-input
pytohn manage.py migrate