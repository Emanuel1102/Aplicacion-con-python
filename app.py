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
        
        
@app.route("/validacion", methods=["POST"])        
def validacion():
    usuarios=bd["usuarios"]
    nom_usuarioAVlidar=request.form["nom_usuario-a-validar"]
    contrasenaAVlidar=request.form["contraseña-a-validar"]
    usuarioAVlidar=usuarios.find_one(
        {"nom_usuario":nom_usuarioAVlidar},
        {"contrasena":contrasenaAVlidar}
    )
    if usuarioAVlidar:
        return accedido()
    else:
        return notFound()
    
    
        
@app.route("/")
def accedido():
    usuarios=bd["usuarios"]
    listaDeUsuarios=usuarios.find()
    return render_template("usuarios-registrados.html",
                           usuarios=listaDeUsuarios)
    
@app.route("/actualizar/<string:nombre_usuario>", methods=["POST"])
def actualizar(nombre_usuario):
    usuarios=bd["usuarios"]
    nombreAActualizar=request.form["nombre-a-actualizar"]
    apellidoAActualizar=request.form["apellido-a-actualizar"]
    nom_usuarioAActualizar=request.form["nom_usuario-a-actualizar"]
    correoAActualizar=request.form["correo-a-actualizar"]
    contrasenaAActualizar=request.form["contraseña-a-actualizar"]
    if nombreAActualizar and apellidoAActualizar and nom_usuarioAActualizar and correoAActualizar and contrasenaAActualizar:
        usuarios.update_one({"nom_usuario":nombre_usuario},
                        {"$set":{
            "nombre":nombreAActualizar,
            "apellido":apellidoAActualizar,
            "nom_usuario":nom_usuarioAActualizar,
            "correo":correoAActualizar,
            "contrasena":contrasenaAActualizar
        }})
        Response=jsonify({"mensaje":"usuario" +nombre_usuario+ "actualizado correctamente"})
        return redirect(url_for("accedido"))
    else:
        return notFound()

            
            
@app.errorhandler(404)
def notFound(error=None):
    mensaje={
        "mensaje":"no encontrado"+request.url,
        "status":"404 Not Found"
    }
    Response=jsonify(mensaje)
    Response.status=404
    return Response



if __name__ == '__main__':
    app.run("127.0.0.1",5000, debug=True)