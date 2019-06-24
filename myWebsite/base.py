from flask import Flask
from flask import request
app=Flask(__name__)

from flask import render_template

@app.route('/')
#@app.route('/portfolio/<home>')
def me():
    return render_template('startUp.html')
