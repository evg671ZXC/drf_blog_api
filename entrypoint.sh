#!/bin/bash
set -e

# uv run gunicorn -c gunicorn.conf.py src.flicksy.wsgi:application
uv run manage.py runserver 0.0.0.0:8000