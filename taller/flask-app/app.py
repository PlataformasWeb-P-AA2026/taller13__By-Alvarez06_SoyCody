from flask import Flask, render_template, request, redirect
import requests
import json 

app = Flask(__name__, template_folder='templates')
app.config['SECRET_KEY'] = 'una-clave-secreta-000001'

token = '493346043f223ae9890d44a30ec2771966f40744'
headers = {
        "Authorization": f"Token {token}",
        "Content-Type": "application/json"
    }

@app.route("/")
def home():
    """
    """
    r_edificios = requests.get("http://localhost:8000/api/edificios/",
            auth=('cody', 'admin123.'))
    edificios = json.loads(r_edificios.content)['results']
    numero_edificios = json.loads(r_edificios.content)['count']

    r_departamentos = requests.get("http://localhost:8000/api/departamentos/",
            headers=headers)
    departamentos = json.loads(r_departamentos.content)['results']
    numero_departamentos = json.loads(r_departamentos.content)['count']

    return render_template("index.html", edificios=edificios,
    numero_edificios=numero_edificios, departamentos=departamentos,
    numero_departamentos=numero_departamentos)








if __name__ == '__main__':
    app.run(debug=True)
