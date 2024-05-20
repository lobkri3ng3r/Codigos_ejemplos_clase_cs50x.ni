CREATE TABLE personas(
    id INTEGER,
    nombre text,
    edad INTEGER,
    genero text,
    PRIMARY KEY(id)
);

CREATE TABLE telefono(
    idTelefono INTEGER,
    idPersona INTEGER,
    numero INTEGER,
    PRIMARY KEY(idTelefono),
    FOREIGN KEY(idPersona) REFERENCES personas(id)
);

.schema 
