"""
La encapsulación nos permite agrupar datos 
y controlar su comportamiento en nuestra clase. 
También nos permite controlar el acceso a nuestros 
datos y prevenir modificaciones no autorizadas.

En Python, no hay modificadores de acceso estrictos como en otros 
lenguajes de programación (por ejemplo, "private" o "public"). 
Sin embargo, se utiliza una convención de nomenclatura para indicar 
la intención de encapsulamiento. Los atributos y métodos que comienzan 
con un guion bajo (_) se consideran "privados" y se supone que no 
deben ser accedidos directamente desde fuera de la clase. Sin embargo, 
esta convención se basa en la buena práctica y no impide el acceso directo a los atributos o métodos.
"""
class Persona:
    def __init__(self, nombre, edad):
        self._nombre = nombre
        self._edad = edad

    def obtener_nombre(self):
        return self._nombre

    def establecer_nombre(self, nuevo_nombre):
        self._nombre = nuevo_nombre

    def obtener_edad(self):
        return self._edad

    def establecer_edad(self, nueva_edad):
        if nueva_edad >= 0:
            self._edad = nueva_edad
        else:
            print("La edad debe ser un valor positivo.")

# Crear una instancia de la clase Persona
persona = Persona("Juan", 25)

# Acceder a los atributos a través de los métodos públicos
print(persona.obtener_nombre())  # Salida: Juan
print(persona.obtener_edad())  # Salida: 25

# Intentar acceder directamente a los atributos "privados"
print(persona._nombre)  # Aunque es posible, se considera una convención no hacerlo

# Establecer nuevos valores para los atributos a través de los métodos públicos
persona.establecer_nombre("Pedro")
persona.establecer_edad(30)

# Acceder a los atributos actualizados
print(persona.obtener_nombre())  # Salida: Pedro
print(persona.obtener_edad())  # Salida: 30

# Intentar establecer un valor no válido para la edad
persona.establecer_edad(-5) 
