import tkinter as tk

def calcular():
    num1 = float(entry_num1.get())
    num2 = float(entry_num2.get())

    if operacion.get() == "Suma":
        resultado = num1 + num2
    elif operacion.get() == "Resta":
        resultado = num1 - num2
    elif operacion.get() == "Multiplicación":
        resultado = num1 * num2
    elif operacion.get() == "División":
        resultado = num1 / num2
    else:
        resultado = "Error"

    label_resultado.config(text=f"Resultado: {resultado}")

ventana = tk.Tk()

# Crear campos de entrada
entry_num1 = tk.Entry(ventana)
entry_num1.pack()

entry_num2 = tk.Entry(ventana)
entry_num2.pack()

# Crear radio buttons
operacion = tk.StringVar()

radio_suma = tk.Radiobutton(ventana, text="Suma", variable=operacion, value="Suma")
radio_suma.pack()

radio_resta = tk.Radiobutton(ventana, text="Resta", variable=operacion, value="Resta")
radio_resta.pack()

radio_multiplicacion = tk.Radiobutton(ventana, text="Multiplicación", variable=operacion, value="Multiplicación")
radio_multiplicacion.pack()

radio_division = tk.Radiobutton(ventana, text="División", variable=operacion, value="División")
radio_division.pack()

# Crear botón de cálculo
boton_calcular = tk.Button(ventana, text="Calcular", command=calcular)
boton_calcular.pack()

# Crear etiqueta de resultado
label_resultado = tk.Label(ventana, text="Resultado:")
label_resultado.pack()

ventana.mainloop()