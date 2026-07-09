from flask import Flask, render_template, request, redirect, url_for
import requests
import json

app = Flask(__name__, template_folder='templates')
app.config['SECRET_KEY'] = 'una-clave-secreta-000001'

token = '493346043f223ae9890d44a30ec2771966f40744'
headers = {
        "Authorization": f"Token {token}",
        "Content-Type": "application/json"
    }

API_URL = "http://localhost:8000/api"


def mapear_nombres_edificios(departamentos, edificios):
    """
    Reemplaza la url de 'edificio' en cada departamento por el nombre
    del edificio asociado, para poder mostrarlo en las plantillas.
    """
    nombres = {e['url']: e['nombre'] for e in edificios}
    for d in departamentos:
        d['edificio_nombre'] = nombres.get(d['edificio'], '')
    return departamentos


@app.route("/")
def home():
    """
    """
    r_edificios = requests.get(f"{API_URL}/edificios/", headers=headers)
    edificios = json.loads(r_edificios.content)['results']
    numero_edificios = json.loads(r_edificios.content)['count']

    r_departamentos = requests.get(f"{API_URL}/departamentos/", headers=headers)
    departamentos = json.loads(r_departamentos.content)['results']
    numero_departamentos = json.loads(r_departamentos.content)['count']
    departamentos = mapear_nombres_edificios(departamentos, edificios)

    return render_template("index.html", edificios=edificios,
    numero_edificios=numero_edificios, departamentos=departamentos,
    numero_departamentos=numero_departamentos)


@app.route("/edificios")
def listar_edificios():
    """
    """
    r = requests.get(f"{API_URL}/edificios/", headers=headers)
    edificios = json.loads(r.content)['results']
    numero_edificios = json.loads(r.content)['count']

    return render_template("listar_edificios.html", edificios=edificios,
    numero_edificios=numero_edificios)


@app.route("/departamentos")
def listar_departamentos():
    """
    """
    r = requests.get(f"{API_URL}/departamentos/", headers=headers)
    departamentos = json.loads(r.content)['results']
    numero_departamentos = json.loads(r.content)['count']

    r_edificios = requests.get(f"{API_URL}/edificios/", headers=headers)
    edificios = json.loads(r_edificios.content)['results']
    departamentos = mapear_nombres_edificios(departamentos, edificios)

    return render_template("listar_departamentos.html", departamentos=departamentos,
    numero_departamentos=numero_departamentos)


@app.route("/edificios/crear", methods=['GET', 'POST'])
def crear_edificio():
    """
    """
    if request.method == 'POST':
        datos = {
            "nombre": request.form['nombre'],
            "direccion": request.form['direccion'],
            "ciudad": request.form['ciudad'],
            "tipo": request.form['tipo'],
        }
        requests.post(f"{API_URL}/edificios/", headers=headers, data=json.dumps(datos))
        return redirect(url_for('listar_edificios'))

    return render_template("crear_edificio.html")


@app.route("/departamentos/crear", methods=['GET', 'POST'])
def crear_departamento():
    """
    """
    if request.method == 'POST':
        datos = {
            "nombre_propietario": request.form['nombre_propietario'],
            "costo_departamento": request.form['costo_departamento'],
            "num_cuartos": request.form['num_cuartos'],
            "edificio": request.form['edificio'],
        }
        requests.post(f"{API_URL}/departamentos/", headers=headers, data=json.dumps(datos))
        return redirect(url_for('listar_departamentos'))

    r = requests.get(f"{API_URL}/edificios/", headers=headers)
    edificios = json.loads(r.content)['results']
    return render_template("crear_departamento.html", edificios=edificios)






if __name__ == '__main__':
    app.run(debug=True)
