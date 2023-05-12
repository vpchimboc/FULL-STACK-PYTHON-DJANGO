"""
desarrollar un programa para gestionar una biblioteca. Se necesita que el programa permita:

Agregar nuevos libros a la biblioteca.
Prestar y devolver libros.
Buscar libros por título y mostrar si están prestados o disponibles.
Para ello, deberás definir dos clases: Libro y Biblioteca. La clase Libro deberá tener los siguientes atributos:

titulo: el título del libro.
autor: el autor del libro.
prestado: un booleano que indica si el libro está prestado o no.
La clase Libro deberá tener los siguientes métodos:

describir_libro(): imprime por pantalla el título y el autor del libro.
prestar(): cambia el estado del atributo prestado a True si el libro está disponible para ser prestado, o imprime un mensaje de error si ya está prestado.
devolver(): cambia el estado del atributo prestado a False si el libro está prestado, o imprime un mensaje de error si no lo está.
La clase Biblioteca deberá tener el siguiente atributo:

libros: una lista de objetos Libro.
La clase Biblioteca deberá tener los siguientes métodos:

agregar_libro(libro): agrega un objeto Libro a la lista libros.
mostrar_libros(): imprime por pantalla los títulos de los libros que están disponibles para ser prestados.
buscar_libro(titulo): busca un objeto Libro por título y retorna el objeto si lo encuentra, o None si no lo encuentra.
A continuación, deberás crear un programa que utilice estas clases y permita al usuario realizar las siguientes acciones:

Agregar nuevos libros a la biblioteca.
Prestar y devolver libros.
Buscar libros por título y mostrar si están prestados o disponibles.
El programa deberá mostrar un menú al usuario con las diferentes opciones, y permitirle elegir la opción deseada ingresando un número.
"""

class Libro:
    def __init__(self, titulo, autor):
        self.titulo = titulo
        self.autor = autor
        self.prestado = False

    def describir_libro(self):
        print(f"{self.titulo} - {self.autor}")

    def prestar(self):
        if self.prestado:
            print("Lo siento, este libro ya está prestado.")
        else:
            self.prestado = True
            print("Libro prestado correctamente.")

    def devolver(self):
        if self.prestado:
            self.prestado = False
            print("Libro devuelto correctamente.")
        else:
            print("Lo siento, este libro no está prestado.")

class Biblioteca:
    def __init__(self):
        self.libros = []

    def agregar_libro(self, libro):
        self.libros.append(libro)

    def mostrar_libros(self):
        libros_disponibles = [libro for libro in self.libros if not libro.prestado]
        if libros_disponibles:
            print("Libros disponibles:")
            for libro in libros_disponibles:
                libro.describir_libro()
        else:
            print("Lo siento, no hay libros disponibles en este momento.")

    def buscar_libro(self, titulo):
        for libro in self.libros:
            if libro.titulo == titulo:
                return libro
        return None

# Creamos una biblioteca vacía
biblioteca = Biblioteca()

while True:
    print("\nMenu:")
    print("1. Agregar un nuevo libro")
    print("2. Prestar un libro")
    print("3. Devolver un libro")
    print("4. Buscar un libro")
    print("5. Mostrar libros disponibles")
    print("6. Salir")

    opcion = input("Ingrese el número de la opción deseada: ")

    if opcion == "1":
        titulo = input("Ingrese el título del libro: ")
        autor = input("Ingrese el autor del libro: ")
        libro = Libro(titulo, autor)
        biblioteca.agregar_libro(libro)
        print(f"{titulo} de {autor} ha sido agregado a la biblioteca.")

    elif opcion == "2":
        titulo = input("Ingrese el título del libro a prestar: ")
        libro = biblioteca.buscar_libro(titulo)
        if libro:
            libro.prestar()
        else:
            print("Lo siento, este libro no está en la biblioteca.")

    elif opcion == "3":
        titulo = input("Ingrese el título del libro a devolver: ")
        libro = biblioteca.buscar_libro(titulo)
        if libro:
            libro.devolver()
        else:
            print("Lo siento, este libro no está en la biblioteca.")

    elif opcion == "4":
        titulo = input("Ingrese el título del libro a buscar: ")
        libro = biblioteca.buscar_libro(titulo)
        if libro:
            if libro.prestado:
                print(f"{titulo} está prestado.")
            else:
                print(f"{titulo} está disponible para ser prestado.")
        else:
            print("Lo siento, este libro no está en la biblioteca.")

    elif opcion == "5":
        biblioteca.mostrar_libros()

    elif opcion == "6":
        print("¡Gracias por usar la biblioteca!")
        break

    else:
        print("Opción inválida, por favor ingrese un número del 1 al 6.")