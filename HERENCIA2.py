#PROFESIONAL HEREDA DE PERSONA
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
#crea instrancia profesional
class Profesional(Persona):
    def __init__(self,Nombre,Edad,Genero,Titulo):
        Persona.__init__(self,Nombre,Edad,Genero)
        self.Titulo= Titulo
    def getTitulo(self):
        return self.Titulo
#crea instancia profesional
class Empresa:
    def __init__(self,Nombre,Gerente):
        self.Nombre = Nombre
        self.Gerente = Gerente
        self.Empleados= []
    def getNombre(self):
        return self.Nombre
    def getGerente(self):
        return self.Gerente
    def setEmpleado(self,Persona):
        self.Empleados.append(Persona)
    def getEmpleados(self, indice):
        return  self.Empleados[indice]
#INSTANCIA
Pers01 = Persona("felipe",45,False)

#print(Pers01.getNombre())

print(Pers01.getNombre())
print((Pers01.getEdad()))
print(Pers01.getGenero())


Prof01= Profesional("LUISA",25,True,"ICG")
print(Prof01.getNombre())
print(Prof01.getTitulo())

Empr01 = Empresa ("icg",Prof01)
print((Empr01.getNombre()))
print(Empr01.getGerente().getNombre())
#agrega empleados
Empr01.setEmpleado(Pers01)
print(Empr01.getEmpleado(1).getNombre())
