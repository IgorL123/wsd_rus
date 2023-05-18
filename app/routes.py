from flask import render_template, request, redirect, url_for


users = [
    {"username": "user1", "password": "password1"},
    {"username": "user2", "password": "password2"},
    {"username": "user3", "password": "password3"}
]


def init_routes(app):

    @app.route('/')
    def index():
        return render_template('index.html')

    @app.route('/login', methods=['GET', 'POST'])
    def login():
        if request.method == 'POST':
            username = request.form['username']
            password = request.form['password']
            for user in users:
                if user['username'] == username and user['password'] == password:
                    return redirect(url_for('home', username=username))
            return render_template('login.html', error='Invalid username or password')
        else:
            return render_template('login.html')

    @app.route('/home/<username>')
    def home(username):
        return render_template('home.html', username=username)