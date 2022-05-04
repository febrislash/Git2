#!/bin/python3
from flask import Flask, escape, request
from flask import Flask, render_template, request, redirect, abort, jsonify, send_from_directory, url_for, g

app = Flask(__name__)


@app.route('/')
def home():
    return render_template('home.html')

if __name__ == '__main__':
    app.run(debug=True)