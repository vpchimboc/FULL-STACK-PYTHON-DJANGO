import tkinter as tk

# Función para realizar la operación de la calculadora
def calcular(operador):
    num1 = float(entrada_num1.get())
    num2 = float(entrada_num2.get())

    if operador == "+":
        resultado = num1 + num2
    elif operador == "-":
        resultado = num1 - num2
    elif operador == "*":
        resultado = num1 * num2
    elif operador == "/":
        if num2 != 0:
            resultado = num1 / num2
        else:
            resultado = "Error: División por cero"
    else:
        resultado = "Error: Operador no válido"

    etiqueta_resultado.config(text="Resultado: " + str(resultado))

# Crear ventana
ventana = tk.Tk()
ventana.title("Calculadora")
ventana.geometry("300x200")

# Crear etiqueta y campo de entrada para el primer número
etiqueta_num1 = tk.Label(ventana, text="Primer número:")
etiqueta_num1.pack()

entrada_num1 = tk.Entry(ventana)
entrada_num1.pack()

# Crear etiqueta y campo de entrada para el segundo número
etiqueta_num2 = tk.Label(ventana, text="Segundo número:")
etiqueta_num2.pack()

entrada_num2 = tk.Entry(ventana)
entrada_num2.pack()

# Crear botones para las operaciones
boton_suma = tk.Button(ventana, text="+", command=lambda: calcular("+"))
boton_suma.pack(side=tk.LEFT)

boton_resta = tk.Button(ventana, text="-", command=lambda: calcular("-"))
boton_resta.pack(side=tk.LEFT)

boton_multiplicacion = tk.Button(ventana, text="*", command=lambda: calcular("*"))
boton_multiplicacion.pack(side=tk.LEFT)

boton_division = tk.Button(ventana, text="/", command=lambda: calcular("/"))
boton_division.pack(side=tk.LEFT)

# Crear etiqueta para mostrar el resultado
etiqueta_resultado = tk.Label(ventana, text="")
etiqueta_resultado.pack()

# Iniciar bucle principal de la ventana
ventana.mainloop()
