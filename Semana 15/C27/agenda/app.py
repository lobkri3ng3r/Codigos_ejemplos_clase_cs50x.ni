# Importar las librerias
from flask import Flask, render_template, request, redirect
from cs50 import SQL

# Crear la conexion con la BD
cursor = SQL("sqlite:///datos.db")

# Instancia para nuestro servidor web
app = Flask(__name__)

# Ruta index
@app.route("/",methods=["GET","POST"])
def index():

    print(request.method)

    if request.method == "POST":

        nombre = request.form.get("nombre")
        telefono = request.form.get("telefono")

        if not nombre or not telefono:
            return render_template("Error.html",mensaje="Hay mas de un campo vacio")

        cursor.execute("INSERT INTO info(nombre,telefono) VALUES(?,?)",nombre,telefono)

        return redirect("/")
    else:
        lista = cursor.execute("SELECT * FROM info")
        return render_template("index.html",info=lista)

@app.route("/eliminar",methods=["POST"])
def eliminar():
    print(request.method)

    muerto = request.form.get("eliminar")

    if muerto:
        cursor.execute("DELETE FROM info WHERE id = ?",muerto)
    else:
        return render_template("Error.html",mensaje="Algo salio muy muy mal")
    return redirect("/")

@app.route("/editar",methods=["GET"])
def editar():
     lista = cursor.execute("SELECT * FROM info")
     return render_template("editar.html",lista=lista)


@app.route("/actualizar",methods=["POST"])
def actualizar():

    nombre = request.form.get("nombre")
    telefono = request.form.get("telefono")
    clave = request.form.get("id")

    if not nombre or not telefono:
        return render_template("Error.html",mensaje="Hay mas de un campo vacio")

    cursor.execute("UPDATE info SET nombre=?, telefono=? WHERE id = ?",nombre,telefono,clave)

    return redirect("/")
