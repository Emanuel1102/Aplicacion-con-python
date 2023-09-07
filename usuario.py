class Usuario:
    def __ini__ (self, nombre, apellido, nom_usuario, correo, contrasena):
        self.nombre = nombre
        self.apellido = apellido
        self.nom_usuario = nom_usuario
        self.correo = correo
        self.contasena = contrasena
        
        
    def aLaColeccion(self):
        return{
            "nombre":self.nombre,
            "apellido":self.apellido,
            "nom_usuario":self.nom_usuario,
            "correo":self.correo,
            "contrasena":self.contrasena
        }