"""
Desarrollar un programa que permita gestionar el historial clínico de pacientes en una clínica. El programa deberá utilizar dos clases: Paciente y Historial.

La clase Paciente deberá tener los siguientes atributos:

nombre: el nombre del paciente.
edad: la edad del paciente.
género: el género del paciente.
historial: un objeto de la clase Historial que contiene la información médica del paciente.
La clase Paciente deberá tener los siguientes métodos:

agregar_historial(sintomas, diagnostico, tratamiento): agrega una entrada al historial del paciente con la información médica especificada.
mostrar_historial(): muestra por pantalla todas las entradas del historial del paciente.
La clase Historial deberá tener los siguientes atributos:

entradas: una lista de diccionarios, donde cada diccionario representa una entrada del historial clínico del paciente y contiene la información médica de la misma.
La clase Historial deberá tener los siguientes métodos:

agregar_entrada(sintomas, diagnostico, tratamiento): agrega una nueva entrada al historial con la información médica especificada.
mostrar_entradas(): muestra por pantalla todas las entradas del historial clínico.
El programa deberá permitir al usuario realizar las siguientes acciones:

Agregar un nuevo paciente, ingresando su nombre, edad y género.
Agregar una nueva entrada al historial clínico de un paciente, ingresando su nombre, sintomas, diagnóstico y tratamiento.
Mostrar el historial clínico de un paciente.
Mostrar todas las entradas del historial clínico de todos los pacientes.
El programa deberá mostrar un menú al usuario con las diferentes opciones, y permitirle elegir la opción deseada ingresando un número.
"""

class Historial:
    def __init__(self):
        self.entradas = []

    def agregar_entrada(self, sintomas, diagnostico, tratamiento):
        entrada = {
            'sintomas': sintomas,
            'diagnostico': diagnostico,
            'tratamiento': tratamiento
        }
        self.entradas.append(entrada)

    def mostrar_entradas(self):
        for entrada in self.entradas:
            print('Síntomas:', entrada['sintomas'])
            print('Diagnóstico:', entrada['diagnostico'])
            print('Tratamiento:', entrada['tratamiento'])

class Paciente:
    def __init__(self, nombre, edad, genero):
        self.nombre = nombre
        self.edad = edad
        self.genero = genero
        self.historial = Historial()

    def agregar_historial(self, sintomas, diagnostico, tratamiento):
        self.historial.agregar_entrada(sintomas, diagnostico, tratamiento)

    def mostrar_historial(self):
        print('Historial clínico de', self.nombre)
        self.historial.mostrar_entradas()
class Paciente:
    def __init__(self, nombre, edad, genero):
        self.nombre = nombre
        self.edad = edad
        self.genero = genero
        self.historial = Historial()

    def agregar_historial(self, sintomas, diagnostico, tratamiento):
        self.historial.agregar_entrada(sintomas, diagnostico, tratamiento)

    def mostrar_historial(self):
        print('Historial clínico de', self.nombre)
        self.historial.mostrar_entradas()

pacientes = []

while True:
    print("Bienvenido al Sistema de Gestión de Pacientes")
    print('1. Agregar un nuevo paciente')
    print('2. Agregar una nueva entrada al historial clínico de un paciente')
    print('3. Mostrar el historial clínico de un paciente')
    print('4. Mostrar todas las entradas del historial clínico de todos los pacientes')
    print('5. Salir')
    opcion = int(input('Ingrese el número de la opción deseada: '))

    if opcion == 1:
        nombre = input('Ingrese el nombre del paciente: ')
        edad = int(input('Ingrese la edad del paciente: '))
        genero = input('Ingrese el género del paciente: ')
        paciente = Paciente(nombre, edad, genero)
        pacientes.append(paciente)

    elif opcion == 2:
        nombre = input('Ingrese el nombre del paciente: ')
        sintomas = input('Ingrese los síntomas: ')
        diagnostico = input('Ingrese el diagnóstico: ')
        tratamiento = input('Ingrese el tratamiento: ')
        for paciente in pacientes:
            if paciente.nombre == nombre:
                paciente.agregar_historial(sintomas, diagnostico, tratamiento)
                break
        else:
            print('Paciente no encontrado')

    elif opcion == 3:
        nombre = input('Ingrese el nombre del paciente: ')
        for paciente in pacientes:
            if paciente.nombre == nombre:
                paciente.mostrar_historial()
                break
        else:
            print('Paciente no encontrado')

    elif opcion == 4:
        for paciente in pacientes:
            paciente.mostrar_historial()

    elif opcion == 5:
        break

    else:
        print('Opción inválida')

