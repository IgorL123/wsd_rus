from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()


class Users(db.Model):
    __tablename__ = "users"
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    email = db.Column(db.String(), nullable=False)
    password_hash = db.Column(db.String(), nullable=False)

    def __repr__(self):
        return f"<User {self.id}, {self.email}, {self.password_hash}>"

    def __init__(self, email, password):
        self.email = email
        self.password_hash = password


class Requests(db.Model):
    __tablename__ = "requests"
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    text = db.Column(db.String(), nullable=False)
    #date = db.Column(db.Date)
    word = db.Column(db.String(), nullable=False)
    #id_user = db.Column()

    def __repr__(self):
        return f"<User {self.id}, {self.email}, {self.password_hash}>"

    def __init__(self, text, word):
        self.text = text
        self.word = word
