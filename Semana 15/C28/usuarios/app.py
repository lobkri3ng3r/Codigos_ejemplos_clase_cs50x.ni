from flask import Flask, render_template, request, redirect, session
from flask_session import Session
from cs50 import SQL
from werkzeug.security import check_password_hash, generate_password_hash


# Configuracion de la app
app = Flask(__name__)

# conectar la base de datos
cursor = SQL("sqlite:///datos.db")

# Configurar la session
app.config["SESSION_PERMANENT"] = False
app.config["SESSION_TYPE"] = "filesystem"
Session(app)


@app.route("/")
def index():
    usuario = session.get("name")
    id = session.get("user_id")
    return render_template("index.html",usuario=usuario,id=id)


@app.route("/login", methods=["GET", "POST"])
def login():

    if request.method == "POST":
        correo = request.form.get("correo")
        contra = request.form.get("contra")

        if not correo or not contra:
            return "CAMPOS VACIOS"

        info = cursor.execute("SELECT * from user WHERE correo = ? ",correo)[0]

        if len(info) != 0 and not check_password_hash(info["contra"],contra):
            return ("error")

        session["name"] = info["nombre"]
        session["user_id"] = info["id"]
        print(session["name"])
        print(session["user_id"])

        return redirect("/")

    # METODO GET
    return render_template("login.html")


@app.route("/register", methods=["GET","POST"])
def register():

    if request.method == "POST":

        nombre = request.form.get("nombre")
        correo = request.form.get("correo")
        contra = generate_password_hash(request.form.get("contra"))

        # verificar que no existan campos vacios
        if not nombre or not correo or not contra:
            return "NO PUEDEN HABER CAMPOS VACIOS"

        cursor.execute("INSERT INTO user(correo,nombre,contra)VALUES(?,?,?)",correo,nombre,contra)
        print(f"{nombre}, {correo}, {contra}")
        return redirect("/login")
    # METODO GET
    return render_template("register.html")

@app.route("/cerrar",methods=["POST"])
def cerrar():

    session.clear()
    return redirect("/")
