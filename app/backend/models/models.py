from flask_sqlalchemy import SQLAlchemy
from flask_login import UserMixin
from sqlalchemy.sql import func

db = SQLAlchemy()


class Users(UserMixin, db.Model):
    __tablename__ = "users"
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    email = db.Column(db.String(100), nullable=False, unique=True)
    password_hash = db.Column(db.String(), nullable=False)

    def __repr__(self):
        return f"<User {self.id}, {self.email}, {self.password_hash}>"

    def __init__(self, email, password):
        self.email = email
        self.password_hash = password


class Request(db.Model):
    __tablename__ = "requests"
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    text = db.Column(db.String(1000), nullable=False)
    date = db.Column(db.DateTime(), default=func.now())
    word = db.Column(db.String(25), nullable=False)
    id_user = db.Column(db.Integer, db.ForeignKey(Users.id))
    user = db.relationship("Users", backref='request', primaryjoin="Users.id == Request.id_user")

    def __init__(self, text, word, id_user):
        self.text = text
        self.word = word
        self.id_user = id_user

    def __repr__(self):
        return f"{self.text}"


class Response(db.Model):
    __tablename__ = "response"
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    text = db.Column(db.String(500), nullable=False)
    grade = db.Column(db.Integer)
    model_type = db.Column(db.String(10))
    score = db.Column(db.Float)
    id_request = db.Column(db.Integer, db.ForeignKey(Request.id))
    request = db.relationship('Request', backref='response',
                              primaryjoin='Request.id == Response.id_request')

    def __init__(self, text, id_request, model_type, score, grade=None):
        self.text = text
        self.id_request = id_request
        self.model_type = model_type
        self.score = score
        if grade is not None:
            self.grade = grade
