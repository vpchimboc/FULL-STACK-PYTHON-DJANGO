"""
Desarrollar un programa que permita gestionar una tienda de productos. El programa deberá utilizar dos clases: Producto y Tienda.

La clase Producto deberá tener los siguientes atributos:

nombre: el nombre del producto.
precio: el precio del producto.
cantidad: la cantidad de unidades disponibles del producto.
La clase Producto deberá tener los siguientes métodos:

init(): el método constructor que recibe los valores iniciales de los atributos del producto.
mostrar_producto(): imprime por pantalla la información del producto, incluyendo su nombre, precio y cantidad.
La clase Tienda deberá tener los siguientes atributos:

nombre: el nombre de la tienda.
productos: una lista de objetos Producto.
La clase Tienda deberá tener los siguientes métodos:

agregar_producto(producto): agrega un objeto Producto a la lista de productos de la tienda.
buscar_producto(nombre): busca un objeto Producto por su nombre y retorna el objeto si lo encuentra, o None si no lo encuentra.
mostrar_productos(): imprime por pantalla la información de todos los productos de la tienda, utilizando el método mostrar_producto() de cada objeto Producto.
El programa deberá permitir al usuario realizar las siguientes acciones:

Agregar un nuevo producto a la tienda, ingresando su nombre, precio y cantidad.
Buscar un producto por su nombre y mostrar su información.
Mostrar la información de todos los productos de la tienda.
El programa deberá mostrar un menú al usuario con las diferentes opciones, y permitirle elegir la opción deseada ingresando un número. Además, el programa deberá validar que los valores ingresados por el usuario sean correctos (por ejemplo, que el precio sea un número positivo).
"""

class Producto:
    def __init__(self, nombre, precio, cantidad):
        self.nombre = nombre
        self.precio = precio
        self.cantidad = cantidad

    def mostrar_producto(self):
        print(f"Nombre: {self.nombre} - Precio: {self.precio} - Cantidad: {self.cantidad}")


class Tienda:
    def __init__(self, nombre):
        self.nombre = nombre
        self.productos = []

    def agregar_producto(self, producto):
        self.productos.append(producto)

    def buscar_producto(self, nombre):
        for producto in self.productos:
            if producto.nombre == nombre:
                return producto
        return None

    def mostrar_productos(self):
        for producto in self.productos:
            producto.mostrar_producto()


def validar_numero(valor):
    try:
        float(valor)
        return True
    except ValueError:
        return False


# Programa principal
tienda = Tienda("Mi Tienda")

while True:
    print("\n-- MENU --")
    print("1. Agregar un nuevo producto")
    print("2. Buscar un producto por nombre")
    print("3. Mostrar todos los productos")
    print("4. Salir")

    opcion = input("Ingrese una opcion: ")

    if opcion == "1":
        nombre = input("Ingrese el nombre del producto: ")
        while True:
            precio = input("Ingrese el precio del producto: ")
            if validar_numero(precio):
                precio = float(precio)
                if precio > 0:
                    break
            print("Error: el precio debe ser un número positivo")

        while True:
            cantidad = input("Ingrese la cantidad de unidades del producto: ")
            if cantidad.isdigit() and int(cantidad) > 0:
                cantidad = int(cantidad)
                break
            print("Error: la cantidad debe ser un número entero positivo")

        producto = Producto(nombre, precio, cantidad)
        tienda.agregar_producto(producto)
        print(f"\nSe ha agregado el producto {nombre} a la tienda.")

    elif opcion == "2":
        nombre = input("Ingrese el nombre del producto: ")
        producto = tienda.buscar_producto(nombre)
        if producto is not None:
            producto.mostrar_producto()
        else:
            print("No se ha encontrado ningún producto con ese nombre.")

    elif opcion == "3":
        print("\n-- Productos en la tienda --")
        tienda.mostrar_productos()

    elif opcion == "4":
        print("¡Hasta luego!")
        break

    else:
        print("Error: opción inválida. Por favor ingrese un número del 1 al 4.")
