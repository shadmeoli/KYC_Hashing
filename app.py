from flask import Flask, jsonify
from flask import render_template, request, url_for, redirect
# from flask_bootstrap import Bootstrap

import httpx
from datetime import datetime
import json


# initilizing flask app
app = Flask(__name__)
# Bootstrap(app)


# endpoint/webhook server
@app.route('/', methods=['GET', 'POST'])
def index():

    # cheaking the kind of methods allowed
    if request.method == 'GET':
        return render_template('index.html')
    # getting input data from the client side 
    if request.method == 'POST':
        return render_template('index.html')
    else:
        return render_template('index.html')


# creating the server in-app entry point
if __name__ == '__main__':
    app.run(
        host="127.0.0.1",
        port=8000,
        debug=True
    )