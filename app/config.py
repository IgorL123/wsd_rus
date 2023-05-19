import os
from dotenv import load_dotenv
load_dotenv()


class Config(object):
    SQLALCHEMY_DATABASE_URI = os.getenv("DATABASE_URl")
    SQLALCHEMY_TRACK_MODIFICATIONS = False
