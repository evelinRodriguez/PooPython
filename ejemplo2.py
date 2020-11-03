#PARA CREAR CLASE
class Persona:

    #constructor , perimero que se inicia
    def __init__(self,Nombre,Edad,Genero):
        self.Nombre= Nombre
        self.Edad= Edad
        self.Genero= Genero

#funcion necesita un parametro de entrada que nunca se pueda omitir
    def getNombre(self):
        return self.Nombre
    def setNombre(self,Nombre):
        self.Nombre = Nombre
    def getEdad(self):
        return self.Edad
    def setEdad(self,Edad):
        self.Edad = Edad
    def getGenero(self):
        return self.Genero
    def setGenero(self,Genero):
        self.Genero = Genero



#INSTANCIA
Pers01 = Persona("felipe",45,False)
#print(Pers01.getNombre())

print(Pers01.getNombre())
print((Pers01.getEdad()))
print(Pers01.getGenero())
