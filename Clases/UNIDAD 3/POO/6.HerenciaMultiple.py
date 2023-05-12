"""
La herencia múltiple en Python permite que una clase herede atributos y métodos de múltiples clases padre. Esto significa que una clase hija puede derivar características de dos o más clases padres.

La sintaxis para definir una clase hija con herencia múltiple en Python es la siguiente:

python
Copy code
class ClasePadre1:
    # Atributos y métodos de la ClasePadre1

class ClasePadre2:
    # Atributos y métodos de la ClasePadre2

class ClaseHija(ClasePadre1, ClasePadre2):
    # Atributos y métodos adicionales de la ClaseHija
"""
class Empleado:
    def __init__(self, nombre, salario):
        self.nombre = nombre
        self.salario = salario

    def obtener_informacion(self):
        return f"Nombre: {self.nombre}, Salario: {self.salario}"

    def trabajar(self):
        print("El empleado está trabajando.")

class Afiliado:
    def __init__(self, numero_afiliacion):
        self.numero_afiliacion = numero_afiliacion

    def obtener_informacion(self):
        return f"Número de afiliación: {self.numero_afiliacion}"

    def recibir_beneficios(self):
        print("El afiliado está recibiendo beneficios.")

class Gerente(Empleado, Afiliado):
    def __init__(self, nombre, salario, numero_afiliacion, departamento):
        Empleado.__init__(self, nombre, salario)
        Afiliado.__init__(self, numero_afiliacion)
        self.departamento = departamento

    def obtener_informacion(self):
        return f"Nombre: {self.nombre}, Salario: {self.salario}, Número de afiliación: {self.numero_afiliacion}, Departamento: {self.departamento}"

    def gestionar_equipo(self):
        print("El gerente está gestionando su equipo.")

# Crear una instancia de la clase Gerente
mi_gerente = Gerente("Juan Pérez", 5000, "G1234", "Ventas")

# Acceder a los métodos y atributos de las clases padres y de la clase hija
print(mi_gerente.obtener_informacion())  
mi_gerente.trabajar()  
mi_gerente.recibir_beneficios()  
mi_gerente.gestionar_equipo()  

