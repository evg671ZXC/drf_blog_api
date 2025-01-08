#!/bin/bash
set -e

uv run gunicorn -c gunicorn.conf.py src.flicksy.wsgi:application