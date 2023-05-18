import tkinter as tk
import sqlite3
from tkinter import ttk

class Estudiante:
    def __init__(self, nombre):
        self.nombre = nombre
        self.calificaciones = {}

    def agregar_calificacion(self, curso, calificacion):
        self.calificaciones[curso] = calificacion

    def obtener_promedio(self):
        if not self.calificaciones:
            return 0
        return sum(self.calificaciones.values()) / len(self.calificaciones)

class Curso:
    def __init__(self, nombre):
        self.nombre = nombre
        self.estudiantes = []

    def agregar_estudiante(self, estudiante):
        self.estudiantes.append(estudiante)

    def obtener_promedios(self):
        promedios = []
        for estudiante in self.estudiantes:
            promedio = estudiante.obtener_promedio()
            promedios.append((estudiante.nombre, promedio))
        promedios.sort(key=lambda x: x[1], reverse=True)
        return promedios

def crear_tabla():
    conexion = sqlite3.connect("calificaciones.db")
    cursor = conexion.cursor()
    cursor.execute("CREATE TABLE IF NOT EXISTS estudiantes (nombre TEXT, curso TEXT, calificacion REAL)")
    conexion.commit()
    conexion.close()

def agregar_estudiante_db(nombre):
    conexion = sqlite3.connect("calificaciones.db")
    cursor = conexion.cursor()
    cursor.execute("INSERT INTO estudiantes VALUES (?, '', 0)", (nombre,))
    conexion.commit()
    conexion.close()

def agregar_calificacion_db(nombre, curso, calificacion):
    conexion = sqlite3.connect("calificaciones.db")
    cursor = conexion.cursor()
    cursor.execute("UPDATE estudiantes SET curso=?, calificacion=? WHERE nombre=?", (curso, calificacion, nombre))
    conexion.commit()
    conexion.close()

def obtener_estudiantes_db():
    conexion = sqlite3.connect("calificaciones.db")
    cursor = conexion.cursor()
    cursor.execute("SELECT nombre FROM estudiantes")
    estudiantes = cursor.fetchall()
    conexion.close()
    return [estudiante[0] for estudiante in estudiantes]

def obtener_calificaciones_db(nombre):
    conexion = sqlite3.connect("calificaciones.db")
    cursor = conexion.cursor()
    cursor.execute("SELECT curso, calificacion FROM estudiantes WHERE nombre=?", (nombre,))
    calificaciones = cursor.fetchall()
    conexion.close()
    return calificaciones

def main():
    crear_tabla()

    cursos = []

    def agregar_estudiante():
        nombre = entry_nombre.get()

        if not nombre:
            lbl_mensaje["text"] = "Error: debe ingresar un nombre de estudiante."
            return

        estudiante = Estudiante(nombre)
        cursos[combo_cursos.current()].agregar_estudiante(estudiante)
        agregar_estudiante_db(nombre)

        lbl_mensaje["text"] = f"¡Estudiante '{nombre}' agregado al curso '{cursos[combo_cursos.current()].nombre}'!"

    def agregar_calificacion():
        nombre = entry_nombre.get()
        curso = cursos[combo_cursos.current()].nombre
        calificacion = float(entry_calificacion.get())

        if not nombre:
            lbl_mensaje["text"] = "Error: debe ingresar un nombre de estudiante."
            return

        if calificacion < 0 or calificacion > 100:
            lbl_mensaje["text"] = "Error: la calificación debe estar entre 0 y 100."
            return

        cursos[combo_cursos.current()].estudiantes[combo_estudiantes.current()].agregar_calificacion(curso, calificacion)
        agregar_calificacion_db(nombre, curso, calificacion)

        lbl_mensaje["text"] = f"¡Calificación '{calificacion}' agregada al estudiante '{nombre}' en el curso '{curso}'!"

    def mostrar_promedios():
        curso = cursos[combo_cursos.current()]
        promedios = curso.obtener_promedios()

        if not promedios:
            lbl_mensaje["text"] = "No hay estudiantes en el curso."
            return

        texto = "Promedios de calificaciones:\n"
        for estudiante, promedio in promedios:
            texto += f"Estudiante: {estudiante}, Promedio: {promedio:.2f}\n"
        lbl_mensaje["text"] = texto

    def actualizar_estudiantes():
        estudiantes = obtener_estudiantes_db()
        combo_estudiantes["values"] = estudiantes

    def actualizar_calificaciones():
        nombre = entry_nombre.get()
        calificaciones = obtener_calificaciones_db(nombre)
        combo_calificaciones["values"] = calificaciones

    def actualizar_cursos():
        combo_cursos["values"] = [curso.nombre for curso in cursos]

    def crear_curso():
        nombre_curso = entry_curso.get()
        cursos.append(Curso(nombre_curso))
        entry_curso.delete(0, tk.END)
        actualizar_cursos()

    ventana = tk.Tk()
    ventana.title("Gestión de Calificaciones")

    lbl_titulo = tk.Label(ventana, text="Gestión de Calificaciones", font=("Arial", 16))
    lbl_titulo.pack(pady=10)

    frame_cursos = tk.Frame(ventana)
    frame_cursos.pack()

    lbl_curso = tk.Label(frame_cursos, text="Curso:")
    lbl_curso.grid(row=0, column=0, padx=5, pady=5)

    entry_curso = tk.Entry(frame_cursos)
    entry_curso.grid(row=0, column=1, padx=5, pady=5)

    btn_crear_curso = tk.Button(frame_cursos, text="Crear Curso", command=crear_curso)
    btn_crear_curso.grid(row=0, column=2, padx=5, pady=5)

    combo_cursos = ttk.Combobox(frame_cursos, state="readonly")
    combo_cursos.grid(row=1, column=0, columnspan=2, padx=5, pady=5)
    combo_cursos["values"] = [curso.nombre for curso in cursos]

    frame_estudiantes = tk.Frame(ventana)
    frame_estudiantes.pack()

    lbl_nombre = tk.Label(frame_estudiantes, text="Nombre:")
    lbl_nombre.grid(row=0, column=0, padx=5, pady=5)

    entry_nombre = tk.Entry(frame_estudiantes)
    entry_nombre.grid(row=0, column=1, padx=5, pady=5)

    btn_agregar_estudiante = tk.Button(frame_estudiantes, text="Agregar Estudiante", command=agregar_estudiante)
    btn_agregar_estudiante.grid(row=0, column=2, padx=5, pady=5)

    combo_estudiantes = ttk.Combobox(frame_estudiantes, state="readonly")
    combo_estudiantes.grid(row=1, column=0, columnspan=2, padx=5, pady=5)
    combo_estudiantes["values"] = []

    frame_calificaciones = tk.Frame(ventana)
    frame_calificaciones.pack()

    lbl_calificacion = tk.Label(frame_calificaciones, text="Calificación:")
    lbl_calificacion.grid(row=0, column=0, padx=5, pady=5)

    entry_calificacion = tk.Entry(frame_calificaciones)
    entry_calificacion.grid(row=0, column=1, padx=5, pady=5)

    btn_agregar_calificacion = tk.Button(frame_calificaciones, text="Agregar Calificación", command=agregar_calificacion)
    btn_agregar_calificacion.grid(row=0, column=2, padx=5, pady=5)

    combo_calificaciones = ttk.Combobox(frame_calificaciones, state="readonly")
    combo_calificaciones.grid(row=1, column=0, columnspan=2, padx=5, pady=5)
    combo_calificaciones["values"] = []

    frame_acciones = tk.Frame(ventana)
    frame_acciones.pack(pady=10)

    btn_promedios = tk.Button(frame_acciones, text="Mostrar Promedios", command=mostrar_promedios)
    btn_promedios.pack()

    lbl_mensaje = tk.Label(ventana, text="")
    lbl_mensaje.pack()

    actualizar_estudiantes()
    ventana.mainloop()

if __name__ == "__main__":
    main()
