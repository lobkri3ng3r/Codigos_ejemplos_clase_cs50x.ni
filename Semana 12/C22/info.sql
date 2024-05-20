-- CREATE TABLE videoJuego(
--     nombre ,
--     precio ,
--     genero ,
--     rating ,
--     plataforma ,
--     conectividad ,
--     espacioDisco
-- );

-- .schema
-- izacion de los insert
-- INSERT INTO videoJuego(nombre,precio,genero,rating,plataforma ,conectividad,espacioDisco)
-- VALUES ('Minecraft',34.99,"Aventura",4.8,"pc","offline - online",500.0);

-- INSERT INTO videoJuego(nombre, precio, genero, rating, plataforma, conectividad, espacioDisco)
-- VALUES ('The Witcher 3: Wild Hunt', 29.99, 'RPG', 4.9, 'PS4', 'Online', 50.0);

-- INSERT INTO videoJuego(nombre, precio, genero, rating, plataforma, conectividad, espacioDisco)
-- VALUES ('Call of Duty: Modern Warfare', 59.99, 'Shooter', 4.7, 'Xbox One', 'Online', 150.0);

-- INSERT INTO videoJuego(nombre, precio, genero, rating, plataforma, conectividad, espacioDisco)
-- VALUES ('Animal Crossing: New Horizons', 49.99, 'Simulación', 4.8, 'Nintendo Switch', 'Offline - Online', 25.0);

-- INSERT INTO videoJuego(nombre, precio, genero, rating, plataforma, conectividad, espacioDisco)
-- VALUES ('FIFA 22', 54.99, 'Deportes', 4.6, 'PS5', 'Online', 80.0);

-- INSERT INTO videoJuego(nombre, precio, genero, rating, plataforma, conectividad, espacioDisco)
-- VALUES ('Grand Theft Auto V', 39.99, 'Acción', 4.9, 'PC', 'Offline - Online', 100.0);

-- INSERT INTO videoJuego(nombre, precio, genero, rating, plataforma, conectividad, espacioDisco)
-- VALUES ('The Legend of Zelda: Breath of the Wild', 49.99, 'Aventura', 4.8, 'Nintendo Switch', 'Offline', 30.0);

-- INSERT INTO videoJuego(nombre, precio, genero, rating, plataforma, conectividad, espacioDisco)
-- VALUES ('Overwatch', 39.99, 'Shooter', 4.7, 'Xbox Series X', 'Online', 60.0);

-- INSERT INTO videoJuego(nombre, precio, genero, rating, plataforma, conectividad, espacioDisco)
-- VALUES ('Red Dead Redemption 2', 44.99, 'Acción-Aventura', 4.9, 'PS4', 'Offline', 120.0);

-- INSERT INTO videoJuego(nombre, precio, genero, rating, plataforma, conectividad, espacioDisco)
-- VALUES ('League of Legends', 0.00, 'MOBA', 4.8, 'PC', 'Online', 20.0);

-- INSERT INTO videoJuego(nombre, precio, genero, rating, plataforma, conectividad, espacioDisco)
-- VALUES ('Fortnite', 0.00, 'Battle Royale', 4.7, 'Mobile', 'Online', 10.0);


Select videoJuego.nombre as "Nombre juego" from videoJuego where videoJuego.conectividad = "Online"
and videoJuego.genero = "Shooter";

Select videoJuego.nombre, videoJuego.precio from videoJuego where videoJuego.precio < 40.0;

DELETE FROM videoJuego where videoJuego.nombre = "League of Legends";

UPDATE videoJuego SET genero = "Aventura" where nombre = "The Witcher 3: Wild Hunt";

Select * from videoJuego;

