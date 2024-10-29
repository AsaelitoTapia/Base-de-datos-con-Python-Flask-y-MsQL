from flask import Flask, render_template, request, redirect, url_for
import os
import database as db

template_dir = os.path.dirname(os.path.abspath(os.path.dirname(__file__)))
template_dir = os.path.join(template_dir, 'src', 'templates')

app = Flask(__name__, template_folder="src/templates")

# Rutas de la aplicación
@app.route('/')
def home():
    cursor = db.database.cursor()
    cursor.execute("SELECT Alumno_ID, Nombre, Apellidos, Edad, Domicilio, Telefono, Correo_Electronico FROM alumnos")
    myresult = cursor.fetchall()
    # Convertir los datos a diccionario
    insertObject = []
    columnNames = [column[0] for column in cursor.description]
    for record in myresult:
        insertObject.append(dict(zip(columnNames, record)))
    cursor.close()
    return render_template('index.html', data=insertObject)

# Ruta para guardar usuarios en la bdd
@app.route('/user', methods=['POST'])
def addUser():
    nombre = request.form['nombre']
    apellidos = request.form['apellidos']
    edad = request.form['edad']
    domicilio = request.form['domicilio']
    telefono = request.form['telefono']
    correo = request.form['correo']

    if nombre and apellidos and edad and domicilio and telefono and correo:
        cursor = db.database.cursor()
        sql = "INSERT INTO alumnos (Nombre, Apellidos, Edad, Domicilio, Telefono, Correo_Electronico) VALUES (%s, %s, %s, %s, %s, %s)"
        data = (nombre, apellidos, edad, domicilio, telefono, correo)
        cursor.execute(sql, data)
        db.database.commit()
    return redirect(url_for('home'))

# Ruta para borrar un usuario
@app.route('/delete/<int:Alumno_ID>')
def delete(Alumno_ID):
    cursor = db.database.cursor()
    sql = "DELETE FROM alumnos WHERE Alumno_ID=%s"
    data = (Alumno_ID,)
    cursor.execute(sql, data)
    db.database.commit()
    return redirect(url_for('home'))

# Ruta para editar un usuario
@app.route('/edit/<int:alumno_id>', methods=['POST'])
def edit(alumno_id):
    nombre = request.form['nombre']
    apellidos = request.form['apellidos']
    edad = request.form['edad']
    domicilio = request.form['domicilio']
    telefono = request.form['telefono']
    correo = request.form['correo']

    if nombre and apellidos and edad and domicilio and telefono and correo:
        cursor = db.database.cursor()
        sql = "UPDATE alumnos SET Nombre = %s, Apellidos = %s, Edad = %s, Domicilio = %s, Telefono = %s, Correo_Electronico = %s WHERE Alumno_ID = %s"
        data = (nombre, apellidos, edad, domicilio, telefono, correo, alumno_id)
        cursor.execute(sql, data)
        db.database.commit()
    return redirect(url_for('home'))

if __name__ == '__main__':
    app.run(debug=True, port=5000)
