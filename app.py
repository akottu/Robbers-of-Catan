from flask import Flask, render_template, redirect, url_for, request
# from flask_sqlalchemy import SQLAlchemy
# import models
# import forms


app = Flask(__name__)
# app.secret_key = 's3cr3t'
# app.config.from_object('config')
# db = SQLAlchemy(app, session_options={'autocommit': False})


@app.route('/')
def index():
    return render_template('index.html');

@app.route('/news')
def news():
    return render_template('news.html');

@app.route('/about')
# includes managers
def about():
    return render_template('about.html');

@app.route('/records')
def records():
    return render_template('records.html');

@app.route('/seasons')
def seasons():
    return render_template('seasons.html');

@app.route('/players')
def players():
    return render_template('players.html');

@app.route('/profile')
def profile():
    return render_template('profile.html');

@app.route('/login')
def login():
    return render_template('login.html');

@app.route('/register')
def register():
    return render_template('register.html');

if __name__ == '__main__':
	app.run(debug=True)