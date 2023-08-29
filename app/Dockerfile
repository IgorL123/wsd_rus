FROM ubuntu:latest
LABEL authors="igor"

RUN apt-get update -y
RUN apt-get install -y python3-pip python3 build-essential
COPY . /app
WORKDIR /app
RUN pip3 install torch --index-url https://download.pytorch.org/whl/cpu
RUN pip3 install -r app/requirements.txt
RUN python3 -m nltk.downloader stopwords
RUN python3 -m nltk.downloader punkt

CMD ["sh", "-c", "sleep 1 && python3 -m flask run --host=0.0.0.0 & bash app/migrate.sh"]
