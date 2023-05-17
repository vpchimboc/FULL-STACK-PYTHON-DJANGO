import tkinter as tk

# Función para mostrar el mensaje seleccionado
def mostrar_mensaje():
    mensaje = opciones.get()
    etiqueta.config(text="Has seleccionado: " + mensaje)

# Crear ventana
ventana = tk.Tk()
ventana.title("Selección de mensaje")
ventana.geometry("300x200")

# Crear etiqueta
etiqueta = tk.Label(ventana, text="Selecciona un mensaje")
etiqueta.pack()

# Crear variable para almacenar la selección
opciones = tk.StringVar()

# Crear radiobuttons
radio1 = tk.Radiobutton(ventana, text="Opción 1", variable=opciones, value="Opción 1", command=mostrar_mensaje)
radio1.pack()

radio2 = tk.Radiobutton(ventana, text="Opción 2", variable=opciones, value="Opción 2", command=mostrar_mensaje)
radio2.pack()

radio3 = tk.Radiobutton(ventana, text="Opción 3", variable=opciones, value="Opción 3", command=mostrar_mensaje)
radio3.pack()

# Iniciar bucle principal de la ventana
ventana.mainloop()
