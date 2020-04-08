#!/bin/sh

python manage.py migrate
python manage.py migrate --database=irm
