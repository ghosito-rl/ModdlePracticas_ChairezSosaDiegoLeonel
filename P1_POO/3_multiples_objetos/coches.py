"""  
 Programación Orinetada a Objetos POO o OOP

CLASES .- es como un molde a traves del cual se puede instanciar un objeto dentro de las clases se definen los atributos (propiedades / caracteristicas) y los métodos (funciones o acciones)

OBJETOS O INSTANCIAS .- son parte de una clase los objetos o instacias pertenecen a una clase, es decir para interacturar con la clase o clases y hacer uso de los atributos y metodos es necesario crear un objeto o objetos.
"""

#Ejemplo 1 Crear una clase (un molde para crear mas objetos)llamada Coches y apartir de la clase crear 
#objetos o instancias (coche) con caracteristicas similares (marca,color,modelo,velocidad,potencia,asientos) 
#y con los operaciones de acelerar y frenar. Que los atributos y metodos sean publicos.
#Muestre el color de los coches
#Que los operaciones disminuyan o aumenten la velocidad segun sea el caso y hay jugar con los metodos e 
#imprimir la velocidad final

print("\033c")

class Coches:
    def __init__(self, marca, color, modelo, velocidad, caballaje, plazas):
        self.__marca = marca
        self.__color = color
        self.__modelo = modelo
        self.__velocidad = velocidad
        self.__caballaje = caballaje
        self.__plazas = plazas

    def acelerar(self):
        self.velocidad += 1
        print("Ahora la velocidad es: {self.velocidad}")      

    def frenar(self):
        self.velocidad -= 1
        print("Ahora la velocidad es: {self.velocidad}")   


coche1 = Coches("VW", "Blanco", "2022", 220, 150, 5)
coche2 = Coches("Nissan", "Azul", "2020", 180, 150, 6)

print(f"El coche es un {coche1._Coches__marca}, el color es {coche1._Coches__color} y su velocidad es {coche1.acelerar()}km/h")
print(f"El coche es un {coche2._Coches__marca}, el color es {coche2._Coches__color} y su velocidad es {coche2.acelerar()}km/h")

for i in range(1, 11):
    coche1.acelerar()
    coche2.acelerawqawr()