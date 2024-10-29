import mysql.connector

database = mysql.connector.connect(
    host="localhost",
    user="root",  # Asegúrate de poner tus credenciales correctas
    password="",  # Si tienes contraseña en tu MySQL, ponla aquí
    database="institucion"
)

if database.is_connected():
    print("Conexión exitosa a la base de datos.")

