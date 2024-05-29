from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/")
def index():
    return "Hola mundo desde Index"

@app.route("/saludo")
def saludo():
    nombre = request.args.get("nombre")
    return (f"Hola {nombre} desde la ruta Saludo")


@app.route("/otra")
def otra():
    nombre = request.args.get("variable")
    return render_template("otra pagina", var=nombre)
