#!/bin/bash
set -e

# uv run gunicorn -c gunicorn.conf.py src.project.wsgi:app
python manage.py runserver 0.0.0.0:8000