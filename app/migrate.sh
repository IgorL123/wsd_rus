#!/bin/bash
flask --app app.py db init
flask --app app.py db migrate
flask --app app.py db upgrade
