from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()


class Users(db.Model):
    __tablename__ = "users"
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    email = db.Column(db.String(), nullable=False, unique=True)
    password_hash = db.Column(db.String(), nullable=False)

    def __repr__(self):
        return f"<User {self.id}, {self.email}, {self.password_hash}>"

    def __init__(self, email, password):
        self.email = email
        #hashing
        self.password_hash = password


class Requests(db.Model):
    __tablename__ = "requests"
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    text = db.Column(db.String(), nullable=False)
    date = db.Column(db.Date)
    word = db.Column(db.String(), nullable=False)

    def __init__(self, text, word):
        self.text = text
        self.word = word


class Response(db.Model):
    __tablename__ = "response"
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    text = db.Column(db.String(), nullable=False)
    grade = db.Column(db.Integer)

    def __init__(self, text, grade=None):
        self.text = text
        if grade is not None:
            self.grade = grade
