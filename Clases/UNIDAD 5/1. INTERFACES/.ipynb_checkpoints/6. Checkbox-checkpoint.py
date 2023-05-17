import tkinter as tk

# Función para mostrar las selecciones de los checkboxes
def mostrar_selecciones():
    selecciones = []
    if opcion1.get():
        selecciones.append("Opción 1")
    if opcion2.get():
        selecciones.append("Opción 2")
    if opcion3.get():
        selecciones.append("Opción 3")

    etiqueta.config(text="Selecciones: " + ", ".join(selecciones))

# Crear ventana
ventana = tk.Tk()
ventana.title("Selección de opciones")
ventana.geometry("300x200")

# Crear etiqueta
etiqueta = tk.Label(ventana, text="Selecciona opciones")
etiqueta.pack()

# Crear variables para almacenar las selecciones
opcion1 = tk.BooleanVar()
opcion2 = tk.BooleanVar()
opcion3 = tk.BooleanVar()

# Crear checkboxes
checkbox1 = tk.Checkbutton(ventana, text="Opción 1", variable=opcion1, command=mostrar_selecciones)
checkbox1.pack()

checkbox2 = tk.Checkbutton(ventana, text="Opción 2", variable=opcion2, command=mostrar_selecciones)
checkbox2.pack()

checkbox3 = tk.Checkbutton(ventana, text="Opción 3", variable=opcion3, command=mostrar_selecciones)
checkbox3.pack()

# Iniciar bucle principal de la ventana
ventana.mainloop()
