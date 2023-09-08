import os
from dotenv import load_dotenv
load_dotenv()


class Config(object):
    SQLALCHEMY_DATABASE_URI = os.getenv("DATABASE_URl")
    SECRET_KEY = os.getenv("SECRET_KEY")
    SESSION_COOKIE_NAME = "session"
    SESSION_PERMANENT = True
    LOGDIR = "app/logs/"
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    MODEL = "fasttext"
    FASTTEXT = "app/backend/core/model/fasttext/model.model"
    TINYBERT = "cointegrated/rubert-tiny"
    LABSE = "cointegrated/LaBSE-en-ru"
