from flask import Flask, redirect, url_for

app = Flask(__name__, static_url_path='/static')

@app.route("/")
def index():
    return app.send_static_file('index.html')

@app.route("/f")
def philo():
    return redirect("https://drive.google.com/file/d/0B1ZVeCv9HaaJZ002WDNFM0Znd2s/view", code=302)
