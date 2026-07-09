from flask import Flask, render_template, request, redirect
import requests
import json 

app = Flask(__name__, template_folder='templates')

token = 0
headers = {
        "Authorization": f"Token {token}",
        "Content-Type": "application/json"
    }

@app.route("/")
def home():
    return "¡Hola mundo!"








if __name__ == '__main__':
    app.run(debug=True)
