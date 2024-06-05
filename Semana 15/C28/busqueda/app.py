from cs50 import SQL
from flask import Flask, redirect, render_template, request, session

# Configure app
app = Flask(__name__)

# Connect to database
db = SQL("sqlite:///shows.db")

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/search')
def search():
    busqueda = request.args.get("q")

    if busqueda is None:
        return "Ingrese un elemento a buscar"

    else:
        shows = db.execute('''SELECT * FROM shows WHERE title LIKE "%:busqueda%" ''', busqueda=busqueda)
        return 
