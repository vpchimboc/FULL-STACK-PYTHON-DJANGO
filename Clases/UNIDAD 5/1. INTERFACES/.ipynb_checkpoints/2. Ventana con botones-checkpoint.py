import tkinter as tk

def cambiar_texto():
    etiqueta.config(text="¡Hola Bienvenido al curso de python con Django!")

ventana = tk.Tk()
ventana.title("Interfaz con botones")
ventana.geometry("300x100")

etiqueta = tk.Label(ventana, text="Texto inicial")
etiqueta.pack()

boton = tk.Button(ventana, text="Cambiar texto", command=cambiar_texto)
boton.pack()

ventana.mainloop()
