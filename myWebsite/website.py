from flask import Flask, render_template
from flask import request

app=Flask('website')


@app.route('/')
def start():
    return render_template('startUp.html')

@app.route('/HOME')
def home():
    return render_template('home.html')
