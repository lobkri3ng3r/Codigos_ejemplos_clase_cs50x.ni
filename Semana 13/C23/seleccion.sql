SELECT * FROM personas;
SELECT * FROM telefono;

SELECT * FROM personas
where id  IN (
SELECT idPersona from telefono
where numero = 123
);

SELECT idPersona from telefono
where numero = 123;

SELECT * FROM personas
where id  IN (1,2,3);
