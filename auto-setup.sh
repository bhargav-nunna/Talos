#!/bin/sh
nohup env FLASK_APP=robotCommandServer.py flask run -host='0.0.0.0' &
