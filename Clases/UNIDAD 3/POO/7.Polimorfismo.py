"""
El polimorfismo es un concepto en programación 
orientada a objetos que se refiere a la capacidad 
de objetos de diferentes clases para responder 
al mismo mensaje o invocar el mismo método de manera distinta.
 En otras palabras, el polimorfismo permite que diferentes 
 objetos con comportamientos diferentes sean tratados de manera uniforme.
"""
class Vehiculo:
    def num_ruedas(self):
        print("METODO 1")

class Coche(Vehiculo):
    def num_ruedas(self):
        return 4

class Bicicleta(Vehiculo):
    def num_ruedas(self):
        return 2

# Crear instancias de las clases Coche y Bicicleta
mi_coche = Coche()
mi_bicicleta = Bicicleta()

print(mi_coche.num_ruedas())  
print(mi_bicicleta.num_ruedas())  