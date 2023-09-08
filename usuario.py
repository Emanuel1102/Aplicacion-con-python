class Usuario:
    def __init__ (self, nombre, apellido, nom_usuario, correo, contrasena):
        self.nombre = nombre
        self.apellido = apellido
        self.nom_usuario = nom_usuario
        self.correo = correo
        self.contrasena = contrasena
        
        
    def aLaColeccion(self):
        return{
            "nombre":self.nombre,
            "apellido":self.apellido,
            "nom_usuario":self.nom_usuario,
            "correo":self.correo,
            "contrasena":self.contrasena
        }  