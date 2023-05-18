import tkinter as tk
import sqlite3

class Producto:
    def __init__(self, nombre, precio, cantidad):
        self.nombre = nombre
        self.precio = precio
        self.cantidad = cantidad

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

def crear_tabla():
    conexion = sqlite3.connect("tienda.db")
    cursor = conexion.cursor()
    cursor.execute("CREATE TABLE IF NOT EXISTS productos (nombre TEXT, precio REAL, cantidad INTEGER)")
    conexion.commit()
    conexion.close()

def agregar_producto_db(nombre, precio, cantidad):
    conexion = sqlite3.connect("tienda.db")
    cursor = conexion.cursor()
    cursor.execute("INSERT INTO productos VALUES (?, ?, ?)", (nombre, precio, cantidad))
    conexion.commit()
    conexion.close()

def obtener_productos_db():
    conexion = sqlite3.connect("tienda.db")
    cursor = conexion.cursor()
    cursor.execute("SELECT * FROM productos")
    productos = cursor.fetchall()
    conexion.close()
    return productos

def main():
    crear_tabla()

    tienda = Tienda("Mi Tienda")

    productos_db = obtener_productos_db()
    for producto_db in productos_db:
        nombre, precio, cantidad = producto_db
        producto = Producto(nombre, precio, cantidad)
        tienda.agregar_producto(producto)

    def agregar_producto():
        nombre = entry_nombre.get()
        precio = float(entry_precio.get())
        cantidad = int(entry_cantidad.get())

        if precio < 0 or cantidad < 0:
            lbl_mensaje["text"] = "Error: el precio y la cantidad deben ser valores positivos."
            return

        producto = Producto(nombre, precio, cantidad)
        tienda.agregar_producto(producto)
        agregar_producto_db(nombre, precio, cantidad)

        lbl_mensaje["text"] = "¡Producto agregado exitosamente!"

    def buscar_producto():
        nombre = entry_nombre.get()
        producto = tienda.buscar_producto(nombre)

        if producto:
            lbl_mensaje["text"] = f"Información del producto:\nNombre: {producto.nombre}\nPrecio: {producto.precio}\nCantidad: {producto.cantidad}"
        else:
            lbl_mensaje["text"] = "El producto no se encontró en la tienda."

    def mostrar_productos():
        texto = "Productos en la tienda:\n"
        for producto in tienda.productos:
            texto += f"Nombre: {producto.nombre}, Precio: {producto.precio}, Cantidad: {producto.cantidad}\n"
        lbl_mensaje["text"] = texto

    ventana = tk.Tk()
    ventana.title("Gestión de Tienda")

    lbl_titulo = tk.Label(ventana, text="Gestión de Tienda", font=("Arial", 16))
    lbl_titulo.pack(pady=10)

    frame_agregar = tk.Frame(ventana)
    frame_agregar.pack()

    lbl_nombre = tk.Label(frame_agregar, text="Nombre:")
    lbl_nombre.grid(row=0, column=0, padx=5, pady=5)

    entry_nombre = tk.Entry(frame_agregar)
    entry_nombre.grid(row=0, column=1, padx=5, pady=5)

    lbl_precio = tk.Label(frame_agregar, text="Precio:")
    lbl_precio.grid(row=1, column=0, padx=5, pady=5)

    entry_precio = tk.Entry(frame_agregar)
    entry_precio.grid(row=1, column=1, padx=5, pady=5)

    lbl_cantidad = tk.Label(frame_agregar, text="Cantidad:")
    lbl_cantidad.grid(row=2, column=0, padx=5, pady=5)

    entry_cantidad = tk.Entry(frame_agregar)
    entry_cantidad.grid(row=2, column=1, padx=5, pady=5)

    btn_agregar = tk.Button(frame_agregar, text="Agregar Producto", command=agregar_producto)
    btn_agregar.grid(row=3, column=0, columnspan=2, padx=5, pady=5)

    frame_buscar = tk.Frame(ventana)
    frame_buscar.pack()

    lbl_nombre_buscar = tk.Label(frame_buscar, text="Nombre:")
    lbl_nombre_buscar.grid(row=0, column=0, padx=5, pady=5)

    entry_nombre_buscar = tk.Entry(frame_buscar)
    entry_nombre_buscar.grid(row=0, column=1, padx=5, pady=5)

    btn_buscar = tk.Button(frame_buscar, text="Buscar Producto", command=buscar_producto)
    btn_buscar.grid(row=1, column=0, columnspan=2, padx=5, pady=5)

    btn_mostrar = tk.Button(ventana, text="Mostrar Productos", command=mostrar_productos)
    btn_mostrar.pack(pady=10)

    lbl_mensaje = tk.Label(ventana, text="")
    lbl_mensaje.pack()

    ventana.mainloop()

if __name__ == "__main__":
    main()
