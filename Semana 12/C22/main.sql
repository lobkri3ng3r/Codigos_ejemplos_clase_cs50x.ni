
CREATE TABLE IF NOT EXISTS series (
    id INTEGER PRIMARY KEY,
    nombre TEXT,
    genero TEXT,
    temporada INTEGER,
    rating REAL
);

insert into series(nombre, genero, temporada, rating) VALUES
('Bridgerton', 'Drama', 3, 8),
('Black Mirror', 'Ciencia Ficción', 5, 9.8),
('El hombre en el castillo', 'Accion', 4, 10),
('Breaking Bad', 'Drama', 5, 9.5),
('Game of Thrones', 'Fantasía', 8, 9.3),
('Stranger Things', 'Ciencia Ficción', 4, 8.7),
('Friends', 'Comedia', 10, 8.9),
('The Crown', 'Drama Histórico', 4, 8.7);


Select * from series;
