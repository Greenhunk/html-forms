from flask import Flask, render_template, request
import smtplib
import requests

app = Flask(__name__)

@app.route('/')
def home():
    return render_template("index.html")

@app.route('/login', methods= ["POST"])
def receive_data():
    return "ok"


if __name__ == "__main__":
    app.run(debug=True)
