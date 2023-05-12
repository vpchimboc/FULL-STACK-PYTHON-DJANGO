"""
La herencia nos permite generar una jerarquía de clases 
en las que podemos compartir funcionamientos comunes y 
en el que existirá una clase padre también conocida como superclase
 y una o varias clases hijas conocidas como subclases.

En Python, la herencia se logra mediante 
la declaración de una clase hija (o subclase) 
que hereda atributos y métodos de una clase padre (o superclase).

La sintaxis básica para definir una clase hija 
que hereda de una clase padre en Python es la siguiente:
class ClasePadre:
    # Atributos y métodos de la clase padre

class ClaseHija(ClasePadre):
    # Atributos y métodos adicionales de la clase hija
"""
class Vehiculo:
    def __init__(self, marca, modelo):
        self.marca = marca
        self.modelo = modelo

    def obtener_informacion(self):
        return f"Marca: {self.marca}, Modelo: {self.modelo}"

class Coche(Vehiculo):
    def __init__(self, marca, modelo,color):
        super().__init__(marca, modelo)
        self.color=color

    def obtener_informacion(self):
        return f"Marca: {self.marca}, Modelo: {self.modelo}, Color: {self.color}"

    def conducir(self):
        print("El coche está en movimiento.")

class Motocicleta(Vehiculo):
    def __init__(self, marca, modelo, cilindrada):
        super().__init__(marca, modelo)
        self.cilindrada = cilindrada

    def obtener_informacion(self):
        return f"Marca: {self.marca}, Modelo: {self.modelo}, Cilindrada: {self.cilindrada} cc"

    def acelerar(self):
        print("La motocicleta está acelerando.")

# Crear instancias de las clases hijas
mi_coche = Coche("Ford", "Mustang", "Rojo")
mi_motocicleta = Motocicleta("Honda", "CBR", 600)

# Acceder a los métodos y atributos de la clase padre y de las clases hijas
print(mi_coche.obtener_informacion())  
mi_coche.conducir()  

print(mi_motocicleta.obtener_informacion())  
mi_motocicleta.acelerar()  

