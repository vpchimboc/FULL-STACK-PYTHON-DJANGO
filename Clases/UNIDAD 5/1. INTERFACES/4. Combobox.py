import tkinter as tk
from tkinter import ttk

# Función para manejar la selección del combobox
def seleccionar_opcion():
    opcion_seleccionada = combo.get()
    etiqueta.config(text="Opción seleccionada: " + opcion_seleccionada)

# Crear ventana
ventana = tk.Tk()
ventana.title("Lista desplegable")
ventana.geometry("300x200")

# Crear etiqueta para mostrar el resultado de la selección
etiqueta = tk.Label(ventana, text="")
etiqueta.pack()

# Definir opciones de la lista desplegable
opciones = ["Opción 1", "Opción 2", "Opción 3", "Opción 4"]

# Crear combobox y asignar opciones
combo = ttk.Combobox(ventana, values=opciones)
combo.pack()

# Crear botón para seleccionar opción
boton_seleccionar = tk.Button(ventana, text="Seleccionar", command=seleccionar_opcion)
boton_seleccionar.pack()

# Iniciar bucle principal de la ventana
ventana.mainloop()