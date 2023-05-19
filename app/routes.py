from flask import render_template, request, redirect, url_for
from models import Users, db


def init_routes(app):

    @app.route('/')
    def index():
        return render_template('index.html')

    @app.route('/login', methods=['GET', 'POST'])
    def login():

        if request.method == 'POST':
            email = request.form['username']
            password = request.form['password']
            user = Users(email=email, password=password)
            db.session.add(user)
            db.session.commit()
            return redirect(url_for('home', username=email))
        else:
            return render_template('login.html', error='Invalid username or password')

    @app.route('/home/<username>')
    def home(username):
        return render_template('home.html', username=username)