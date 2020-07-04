import os
import requests
from flask import Flask, session,render_template, redirect, url_for, request

# Configure app
app = Flask(__name__)

@app.route("/")
def index():
    return render_template('index.html')

@app.route("/projects")
def projects():
    return render_template('projects.html')

@app.route("/writing")
def writing():
    return render_template('writing.html')

@app.route("/about")
def about():
    return render_template('about.html')

@app.route("/contact")
def contact():
    return render_template('contact.html')


if __name__ == '__main__':
    app.run(debug=True)
