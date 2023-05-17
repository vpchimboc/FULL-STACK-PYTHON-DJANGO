import tkinter as tk
from tkinter import ttk

# Crear ventana
ventana = tk.Tk()
ventana.title("Tabla de Datos")

# Crear tabla
tabla = ttk.Treeview(ventana)

# Definir columnas
tabla["columns"] = ("Nombre", "Edad", "Email")

# Formato de las columnas
tabla.column("#0", width=0, stretch=tk.NO)  # Columna invisible
tabla.column("Nombre", anchor=tk.W, width=150)
tabla.column("Edad", anchor=tk.CENTER, width=70)
tabla.column("Email", anchor=tk.W, width=200)

# Encabezados de las columnas
tabla.heading("#0", text="")
tabla.heading("Nombre", text="Nombre")
tabla.heading("Edad", text="Edad")
tabla.heading("Email", text="Email")

# Agregar datos a la tabla
tabla.insert("", tk.END, text="1", values=("John Doe", 30, "johndoe@example.com"))
tabla.insert("", tk.END, text="2", values=("Jane Smith", 25, "janesmith@example.com"))

# Mostrar tabla
tabla.pack()

# Iniciar bucle principal de la ventana
ventana.mainloop()
