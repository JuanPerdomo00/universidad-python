-- Se trae toda la tabla de persona
SELECT * FROM persona

-- Se trae un congunto de consultas segun el id pasado, si no existe solo trae los que encuentre.
SELECT * FROM persona WHERE id_persona in (1,2)

-- Inserta datos a la base de datos persona. Con los campos en orden que se colocaron.
INSERT INTO persona(nombre, apellido, correo) VALUES('noe','ovideo','noe@email.com')
-- SELECT * FROM persona

-- Atualiza los  campos, expecificando donde el id sea un numero existente en la tabla.
UPDATE persona SET nombre = 'ximena', apellido = 'sanchez', correo = 'angie@paola.com' WHERE id_persona = 2

-- SELECT * FROM persona

-- Elimina una columna donde el id es 2
DELETE FROM persona WHERE id_persona = 2

-- SELECT * FROM persona
