import sqlite3

#conectar la db
conn = sqlite3.connect("mike.db")

#colocamos el cursor
db = conn.cursor()

db.execute('''
            CREATE TABLE IF NOT EXISTS Personas
            (
                    id integer PRIMARY KEY AUTOINCREMENT,
                    nombre varchar(20) NOT NULL,
                    numero_telf varchar(20) NOT NULL,
                    correo varchar(255) NOT NULL,
                    es_alumno BOOLEAN,
                    es_profe BOOLEAN
            )
        ''')

db.execute('''
            CREATE TABLE IF NOT EXISTS Grupo
            (
                    id integer PRIMARY KEY AUTOINCREMENT,
                    nombre_grupo varchar(2) NOT NULL,
                    turno varchar(255) NOT NULL
            )
        ''')

db.execute('''
            CREATE TABLE IF NOT EXISTS Personas_grupo
            (
                    id integer PRIMARY KEY AUTOINCREMENT,
                    id_persona integer NOT NULL,
                    id_grupo integer NOT NULL,
                    FOREIGN KEY(id_persona) REFERENCES Personas(id),
                    FOREIGN KEY(id_grupo) REFERENCES Grupo(id)
            )
        ''')

def menu():

    while(True):
        try:
            ans = int(input("1)Ingresar una persona\n2)Mostrar la info\n3)Ingresar nuevo grupo4)Salir pofavo"))
            if ans < 1 or ans > 4:
                raise ValueError("ta malo")
        except ValueError:
            print(":c")
        else:
            if ans == 1:
                ingresarDatos()
            if ans == 4:
                print("Salir...")
                break

def ingresarDatos():
    nombre = input("nombre> ")
    numero_telf = input("numero telf> ")
    correo = input("correo> ")
    status = input("Es profe o alumno? [P/A]")

    if status == 'A' or status == 'a':
        es_alumno = True
        es_profe = False
    elif(status == 'p' or status == 'P'):
        es_alumno = False
        es_profe = True
    else:
        print("opcion invalida")

    db.execute('''
                INSERT INTO Personas(nombre,numero_telf,correo,es_alumno,es_profe)
                VALUES(?,?,?,?,?)
               ''',(nombre,numero_telf,correo,es_alumno,es_profe))

    conn.commit()

menu()
