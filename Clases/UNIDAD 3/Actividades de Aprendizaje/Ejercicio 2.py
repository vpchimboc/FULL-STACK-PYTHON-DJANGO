"""
Desarrollar un programa que permita gestionar las calificaciones de un grupo de estudiantes en una lista de cursos.

El programa deberá utilizar dos clases: Estudiante y Curso. La clase Estudiante deberá tener los siguientes atributos:

nombre: el nombre del estudiante.
calificaciones: un diccionario que contiene las calificaciones del estudiante en cada curso.

La clase Estudiante deberá tener los siguientes métodos:

agregar_calificacion(curso, calificacion): agrega una calificación para el curso especificado.
obtener_promedio(): calcula el promedio de calificaciones del estudiante.

La clase Curso deberá tener los siguientes atributos:

nombre: el nombre del curso.
estudiantes: una lista de objetos Estudiante.

La clase Curso deberá tener los siguientes métodos:

agregar_estudiante(estudiante): agrega un objeto Estudiante a la lista de estudiantes.
obtener_promedios(): calcula el promedio de calificaciones de cada estudiante en el curso y los retorna en una lista ordenada por su promedio.

El programa deberá permitir al usuario realizar las siguientes acciones:

Agregar estudiantes a un curso.
Agregar calificaciones a un estudiante.
Calcular el promedio de calificaciones de cada estudiante y mostrar una lista ordenada por su promedio.

El programa deberá mostrar un menú al usuario con las diferentes opciones, y permitirle elegir la opción deseada ingresando un número.
"""

class Estudiante:
    def __init__(self, nombre):
        self.nombre = nombre
        self.calificaciones = {}

    def agregar_calificacion(self, curso, calificacion):
        self.calificaciones[curso] = calificacion

    def obtener_promedio(self):
        if len(self.calificaciones) == 0:
            return 0
        return sum(self.calificaciones.values()) / len(self.calificaciones)


class Curso:
    def __init__(self, nombre):
        self.nombre = nombre
        self.estudiantes = []

    def agregar_estudiante(self, estudiante):
        self.estudiantes.append(estudiante)

    def obtener_promedios(self):
        promedios = []
        for estudiante in self.estudiantes:
            promedio = estudiante.obtener_promedio()
            promedios.append((estudiante.nombre, promedio))
        promedios.sort(key=lambda x: x[1], reverse=True)
        return promedios


cursos = {}

while True:
    print("1. Agregar estudiante a un curso")
    print("2. Agregar calificación a un estudiante")
    print("3. Calcular promedio de calificaciones de cada estudiante y mostrar lista ordenada")
    print("4. Salir")

    opcion = input("Ingrese una opción: ")

    if opcion == "1":
        nombre_curso = input("Ingrese el nombre del curso: ")
        nombre_estudiante = input("Ingrese el nombre del estudiante: ")

        if nombre_curso not in cursos:
            cursos[nombre_curso] = Curso(nombre_curso)

        estudiante = Estudiante(nombre_estudiante)
        cursos[nombre_curso].agregar_estudiante(estudiante)

    elif opcion == "2":
        nombre_curso = input("Ingrese el nombre del curso: ")
        nombre_estudiante = input("Ingrese el nombre del estudiante: ")
        calificacion = float(input("Ingrese la calificación: "))

        curso = cursos[nombre_curso]
        for estudiante in curso.estudiantes:
            if estudiante.nombre == nombre_estudiante:
                estudiante.agregar_calificacion(nombre_curso, calificacion)

    elif opcion == "3":
        nombre_curso = input("Ingrese el nombre del curso: ")
        curso = cursos[nombre_curso]
        promedios = curso.obtener_promedios()

        print(f"Promedio de calificaciones para el curso {nombre_curso}:")
        for estudiante, promedio in promedios:
            print(f"{estudiante}: {promedio}")

    elif opcion == "4":
        break

    else:
        print("Opción inválida")