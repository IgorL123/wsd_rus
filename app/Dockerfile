FROM ubuntu:latest
LABEL authors="igor"

RUN apt-get update -y
RUN apt-get install -y python3-pip python3 build-essential
COPY . /app
WORKDIR /app
RUN pip3 install -r app/requirements.txt


ENV FLASK_APP=app/app.py
ENV FLASK_DEBUG=true
ENV FLASK_ENV=development

CMD ["sh", "-c", "sleep 1 && python3 -m flask run --host=0.0.0.0  && flask db init && flask db migrate && flask db upgrate"]
