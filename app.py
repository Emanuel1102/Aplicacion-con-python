from flask import Flask, render_template, redirect, url_for, request, Response, jsonify
import modelo as baseDeDatos
from usuario import Usuario

bd = baseDeDatos.conexionBd()

app = Flask(__name__)

@app.route("/")
def inicio():
    return render_template("index.html")

@app.route("/registro", methods=["POST"])
def agregar():
    usuarios=bd["usuarios"]
    nombre = request.form["nombre"]
    apellido = request.form["apellido"]
    nom_usuario=request.form["nom_usuario"]
    correo=request.form["correo"]
    contrasena=request.form["contrasena"]
    if nombre and apellido and nom_usuario and correo and contrasena:
        nuevo_usuario= Usuario(nombre, apellido, nom_usuario, correo, contrasena)
        usuarios.insert_one(nuevo_usuario.aLaColeccion())
        Response=jsonify({
            "nombre":nombre,
            "apellido":apellido,
            "nom_usuario":nom_usuario,
            "correo":correo,
            "contrasena":contrasena
        })
        return redirect(url_for("inicio"))
        
            
if __name__ == '__main__':
    app.run("127.0.0.1",5000, debug=True)