#!/bin/bash
flask --app app/prod.py db init
flask --app app/prod.py db migrate
flask --app app/prod.py db upgrade