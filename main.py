#PARA CREAR CLASE
class Persona:

    #constructor , perimero que se inicia
    def __init__(self):
        self.Nombre="adonay"
        self.Edad="12"
        self.Genero=False

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
Pers01 = Persona()
#print(Pers01.getNombre())
Pers01.setNombre("felipe")
Pers01.setEdad("15")
Pers01.setGenero("femenino")
print(Pers01.getNombre())
print((Pers01.getEdad()))
print(Pers01.getGenero())


'''
print(Pers01.Nombre)
Pers01.Nombre = "Felipe"
print(Pers01.Nombre)
'''