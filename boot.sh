#!/bin/sh

exec gunicorn -b 0.0.0.0:6000 --reload --access-logfile - --error-logfile - manage:app --timeout=120
