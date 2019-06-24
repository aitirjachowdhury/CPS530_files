from flask import Flask, render_template, request
from wtforms import Form, TextField, TextAreaField, StringField, SubmitField
from flask_bootstrap import Bootstrap


app=Flask('website')
Bootstrap(app)

@app.route('/')
def start():
    return render_template('startUp.html')

@app.route('/HOME')
def home():
    return render_template('home.html')

@app.route('/image')
def image_library():
    return render_template('image.html')
