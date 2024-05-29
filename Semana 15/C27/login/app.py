from flask import Flask, redirect, render_template, request, session
from flask_session import Session

# Configure app
app = Flask(__name__)

# Configure session
app.config["SESSION_PERMANENT"] = False
app.config["SESSION_TYPE"] = "filesystem"
Session(app)

usuarios = ["Mike","Elo","Susan"]

@app.route("/")
def index():
    if not session.get("name"):
        return redirect("/login")
    return render_template("index.html")


@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        usuario = request.form.get("name")
        contra =  int(request.form.get("pass"))


        if usuario in usuarios:
            if contra == 123456:
                session["name"] = request.form.get("name")
                return redirect("/")
            else:
                return "Password invalido"
        else:
            return "Usuario no valido"

    return render_template("login.html")


@app.route("/logout")
def logout():
    session["name"] = None
    return redirect("/")
