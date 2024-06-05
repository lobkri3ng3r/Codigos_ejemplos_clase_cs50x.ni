from flask import Flask, flash, render_template, redirect, request, session
from flask_session import Session
from cs50 import SQL

db = SQL("sqlite:///agenda.db")

# Configure app
app = Flask(__name__)

# Configure session
app.config["SESSION_PERMANENT"] = False
app.config["SESSION_TYPE"] = "filesystem"
Session(app)


@app.route("/", methods=["GET", "POST"])
def index():

    if not session.get("user_id"):
        return redirect("/login")

    usuario = session.get("name")
    u_id = session.get("user_id")

    datos = db.execute('''
            SELECT contactos.id,contactos.nombre, numeros_telefonicos.numero_telefono from usuarios
            JOIN contactos ON contactos.usuario_id = usuarios.id
            JOIN numeros_telefonicos on contactos.id = numeros_telefonicos.contacto_id
            where contactos.usuario_id = ?
        ''',u_id)


    if request.method == "POST":

        nombre = request.form.get("nombre")
        numero = request.form.get("numero")
        persona = session.get("user_id")

        if not nombre or not numero:
            return "Campos vacios"

        com = db.execute("SELECT nombre from contactos where nombre = ?", nombre)
        if com:
            return "Contacto ya existente"


        # Insertando un contacto de un usuario en particular
        db.execute(
            "INSERT INTO contactos(usuario_id,nombre)VALUES(?,?)", persona, nombre)

        # Extraemos el id de ese contacto
        id_contacto = db.execute("SELECT id from contactos where nombre = ?", nombre)
        id_contacto = id_contacto[0]["id"]
        # Insertando un Numero para el contacto
        db.execute(
            "INSERT INTO numeros_telefonicos(contacto_id,numero_telefono)VALUES(?,?)", id_contacto, numero)

        return redirect("/")

    else:
        return render_template("index.html", usuario=usuario,datos=datos)


@app.route("/login", methods=["GET", "POST"])
def login():

    session.clear()

    if request.method == "POST":

        correo = request.form.get("email")
        contra = int(request.form.get("pass"))

        if not correo or not contra:
            return "Hay campos vacios"

        info = db.execute(
            "SELECT * FROM usuarios where email = ?", correo)

        print(info)

        if len(info) > 1 and info["contra"] != contra and correo != info["email"]:
            print("algo salio mal")

        # print(info[0]['id'])
        session["user_id"] = info[0]["id"]
        session["name"] = info[0]["nombre"]
        print(session["user_id"])

        return redirect("/")

    return render_template("login.html")


@app.route("/register")
def register():
    return render_template("register.html")


@app.route("/cierre")
def cierre():
    session.clear()
    return redirect("/login")
