#!/bin/sh
NEW_RELIC_CONFIG_FILE=/app/docker/newrelic.ini newrelic-admin run-program gunicorn meeting.wsgi --limit-request-line 0 -w 4 -b :80 --timeout 60 --access-logfile - --access-logformat '%({X-Forwarded-For}i)s %(u)s %(t)s "%(r)s" %(s)s %({88-user-id}o)s %(b)s "%(a)s" %(L)s'
