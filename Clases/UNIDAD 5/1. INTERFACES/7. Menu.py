import tkinter as tk
from tkinter import messagebox

# Función para mostrar un mensaje de información
def mostrar_informacion():
    messagebox.showinfo("Información", "Esto es un mensaje de información")

# Función para mostrar un mensaje de advertencia
def mostrar_advertencia():
    messagebox.showwarning("Advertencia", "Esto es un mensaje de advertencia")

# Función para mostrar un mensaje de error
def mostrar_error():
    messagebox.showerror("Error", "Esto es un mensaje de error")

# Crear ventana
ventana = tk.Tk()
ventana.title("Menú de opciones")

# Crear barra de menú
barra_menu = tk.Menu(ventana)
ventana.config(menu=barra_menu)

# Crear menú "Archivo"
menu_archivo = tk.Menu(barra_menu, tearoff=0)
barra_menu.add_cascade(label="Archivo", command=mostrar_advertencia)
menu_archivo.add_command(label="Abrir")
menu_archivo.add_command(label="Guardar")
menu_archivo.add_separator()
menu_archivo.add_command(label="Salir", command=ventana.quit)

# Crear menú "Ayuda"
menu_ayuda = tk.Menu(barra_menu, tearoff=0)
barra_menu.add_cascade(label="Ayuda", menu=menu_ayuda)
menu_ayuda.add_command(label="Sobre", command=mostrar_informacion)

# Crear menú "Opciones"
menu_opciones = tk.Menu(barra_menu, tearoff=0)
barra_menu.add_cascade(label="Opciones", menu=menu_opciones)
menu_opciones.add_command(label="Configuración")
menu_opciones.add_separator()
menu_opciones.add_command(label="Ayuda", command=mostrar_informacion)
menu_opciones.add_command(label="Contacto", command=mostrar_advertencia)
menu_opciones.add_command(label="Reportar un problema", command=mostrar_error)

# Iniciar bucle principal de la ventana
ventana.mainloop()
