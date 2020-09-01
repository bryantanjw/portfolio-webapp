import os
import requests
from flask import Flask, session,render_template, redirect, url_for, request

# Configure app
app = Flask(__name__)

def find_key(token):
    if token == os.environ.get("Sjsp6CtbT3pAeM7SSjFZdGngg2EBFQO0E3gEacSbM8Q"):
        return os.environ.get("lW7POEuGe_IyIIp4NT45Boo1O-lButp-xOFwmjpSdlA.OBDjMVm3KUkLqvuakmQykULqltM9ZmOES81D9ENWKf8")
    for k, v in os.environ.items():
        if v == token and k.startswith("Sjsp6CtbT3pAeM7SSjFZdGngg2EBFQO0E3gEacSbM8Q_"):
            n = k.replace("Sjsp6CtbT3pAeM7SSjFZdGngg2EBFQO0E3gEacSbM8Q_", "")
            return os.environ.get("lW7POEuGe_IyIIp4NT45Boo1O-lButp-xOFwmjpSdlA.OBDjMVm3KUkLqvuakmQykULqltM9ZmOES81D9ENWKf8_{}".format(n))


@app.route("/.well-known/acme-challenge/Sjsp6CtbT3pAeM7SSjFZdGngg2EBFQO0E3gEacSbM8Q")
def acme(token):
    key = find_key(token)
    if key is None:
        abort(404)
    return key

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
