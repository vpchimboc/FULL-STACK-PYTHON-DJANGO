import tkinter as tk

# Crear una ventana
ventana = tk.Tk()

# Configurar propiedades de la ventana
ventana.title("Mi Interfaz")
ventana.geometry("400x100")

# Función para manejar el botón
def saludar():
    nombre = entrada.get()
    etiqueta_saludo.config(text="¡Hola, " + nombre + "!")

# Crear etiqueta
etiqueta = tk.Label(ventana, text="Ingrese su nombre:")
etiqueta.pack()

# Crear campo de entrada de texto
entrada = tk.Entry(ventana)
entrada.pack()

# Crear botón
boton = tk.Button(ventana, text="Saludar", command=saludar)
boton.pack()

# Crear etiqueta para mostrar el saludo
etiqueta_saludo = tk.Label(ventana, text="")
etiqueta_saludo.pack()

# Iniciar el bucle principal de la ventana
ventana.mainloop()