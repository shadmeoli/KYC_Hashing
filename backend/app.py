from textwrap import indent
from flask import Flask, jsonify
from flask import render_template, request, url_for, redirect
from flask import Flask, request, jsonify
# from blockfrost import verify_webhook_signature, SignatureVerificationError
# from flask_bootstrap import Bootstrap

# import httpx
from datetime import datetime
import json


# initilizing flask app
app = Flask(__name__)
# Bootstrap(app)

SECRET_AUTH_TOKEN = "@@@3q5vTVerhShadKimzakyc#vhvhg "


# endpoint/webhook server
@app.route('/', methods=['GET', 'POST'])
def index():

    return jsonify({"server" : "Running"})

@app.route('/metrix')
def home():
    return jsonify({"test": 200})

# creating the server in-app entry point
if __name__ == '__main__':
    app.run(
        host="15.185.32.191",
        port=5000,
        debug=True
    )
