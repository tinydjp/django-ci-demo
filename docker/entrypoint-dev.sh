#!/bin/sh

if [ "$DEBUG" == "True" ]; then
    python demo/manage.py runserver 0.0.0.0:80
else
    source /app/docker/entrypoint.sh
fi
