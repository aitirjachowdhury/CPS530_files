# Basic flask application

from flask import Flask
app=Flask(__name__)




@app.route('/')
def index():
    return '<h1>Learning Flask</h1>'

@app.route('/user')
def user(name):
    return render_template('startUp.html')
