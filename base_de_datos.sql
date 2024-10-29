-- Crear la base de datos
CREATE DATABASE institucion;

-- Usar la base de datos
USE institucion;

-- Crear la tabla 'alumnos'
CREATE TABLE alumnos (
    Alumno_ID INT AUTO_INCREMENT PRIMARY KEY,
    Nombre VARCHAR(50) NOT NULL,
    Apellidos VARCHAR(50) NOT NULL,
    Edad INT,
    Domicilio VARCHAR(100),
    Telefono VARCHAR(15),
    Correo_Electronico VARCHAR(50) UNIQUE
);
