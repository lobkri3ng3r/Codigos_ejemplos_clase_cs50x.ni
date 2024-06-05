CREATE TABLE usuarios (
    id INT PRIMARY KEY,
    nombre TEXT NOT NULL,
    email TEXT UNIQUE NOT NULL,
    contraseña TEXT NOT NULL
);

CREATE TABLE contactos (
    id INT PRIMARY KEY,
    usuario_id INT,
    nombre TEXT NOT NULL,
    FOREIGN KEY (usuario_id) REFERENCES usuarios(id)
);

CREATE TABLE numeros_telefonicos (
    id INT PRIMARY KEY ,
    contacto_id INT,
    numero_telefono TEXT NOT NULL,
    FOREIGN KEY (contacto_id) REFERENCES contactos(id)
);
