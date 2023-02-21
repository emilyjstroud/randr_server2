#!/bin/bash
rm -rf levelupapi/migrations
rm db.sqlite3
python3 manage.py migrate
python3 manage.py makemigrations randrapi
python3 manage.py migrate randrapi
python3 manage.py loaddata users
python3 manage.py loaddata locations
python3 manage.py loaddata rivers
python3 manage.py loaddata rapids
python3 manage.py loaddata river_rapids
