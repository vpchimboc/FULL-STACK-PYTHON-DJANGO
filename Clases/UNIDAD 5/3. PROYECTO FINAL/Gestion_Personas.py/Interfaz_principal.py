from tkinter import*
from tkinter import messagebox
from tkinter import simpledialog
from turtle import textinput
from BD_Conectar import*
import tkinter as tk
from tkinter import ttk
ventana=Tk()
#Conexion a la BD
con=BD_Conectar()
def conectar():
    con.conexion
    agregarDatosTabla(tabla)
#METODOS 
def salir():
    valor=messagebox.askquestion("Atención","Desea Salir de la aplicación?")
    if valor=='yes':
        messagebox.showinfo("Bye!","Gracias por usar nuestro Sistema, vuelva pronto!!")
        exit()
    print(valor)

# Agregar datos a la tabla
def agregarDatosTabla(tabla):
    cont=1
    lista=con.listarTodos()
    if len(lista)>0:
        for persona in lista:
            tabla.insert("", tk.END, text=str(cont), values=(persona[0], persona[1], persona[2]))

def borra_campos():
    txt_id.set("")
    minombre.set("")
    txt_apellido.set("")
    txt_direccion.set("")
    txt_contra.set("")
    comentario.delete("1.0","end")
    print("Campos borrados!!")

def crear_registro():
    id=txt_id.get()
    nombre=minombre.get()
    apellido=txt_apellido.get()
    direccion=txt_direccion.get()
    clave=txt_contra.get()
    texto=comentario.get("1.0","end")
    if id=='':
        if nombre!='' and apellido!='' and direccion!='':
            con.insertar(nombre,apellido,direccion,clave,texto)
            messagebox.showinfo("Informacion","Se ha creado el registro")
        else: messagebox.showinfo("Informacion","Campos incompletos no se puede crear el registro!!")
    else: messagebox.showinfo("Informacion","Registro existente no se puede crear de nuevo!!")
    agregarDatosTabla(tabla)
#LEER REGISTROS

def leer_registro():
    
    id=simpledialog.askinteger("Leer", "Ingrese el ID:",parent=miFrame)
    listaRegistros=con.listar(id)
    for registro in listaRegistros:
        txt_id.set(registro[0])
        minombre.set(registro[1])
        txt_apellido.set(registro[2])
        txt_direccion.set(registro[3])
        txt_contra.set(registro[4])
        comentario.insert(INSERT,(registro[5]))
        print("ID:",registro[0],"Nombre:",registro[1],"Apellido:",registro[2],"Direccion:",registro[3],"Password:",registro[4],"Comentario:",registro[5])
    return id
#ACTUALIZAR REGISTRO
def actualizar_registro():
    id=txt_id.get()
    nombre=minombre.get()
    apellido=txt_apellido.get()
    direccion=txt_direccion.get()
    clave=txt_contra.get()
    texto=comentario.get("1.0","end")
    
    
    if id!='':
        valor=messagebox.askokcancel("Atención","Desea actualizar a la persona: "+nombre+" "+apellido)
        if valor==True:
            con.actualizar(nombre,apellido,direccion,clave,texto,id)
            messagebox.showinfo("Informacion","El registro ha sido actualizado con éxito!!")
            print("Datos Actualizados!!")
        else:
            print("No se actualiza!!")
    else:
        messagebox.showinfo("Informacion","No hay datos para actualizar!!")

#ELIMINAR REGISTRO
def eliminar_registro():
    id=txt_id.get()
    nombre=minombre.get()
    apellido=txt_apellido.get()
    if id!='':
        valor=messagebox.askokcancel("Atención","Desea eliminar a la persona: "+nombre+" "+apellido)
        if valor==True:
            con.eleminar(id)
            messagebox.showinfo("Informacion","El registro ha sido eliminado con éxito!!")
            borra_campos()
        else:
            print("No elimina")
    else:messagebox.showinfo("Informacion","No hay datos para eliminar!!")
#Ventanas Emergentes
def infoAditional():
    messagebox.showinfo("Informacion","Version System V.1.2")
    "Mensaje de Advertencia"
    #messagebox.showwarning("Adevertencia","Licencia caducada")
    "Mensaje de Error"
    #messagebox.showerror("Error","Error de conexión")
    "Ventana Emergente de Confirmación"
    #valor=messagebox.askquestion("Atención","Desea eliminar una persona")
    #valor=messagebox.askokcancel("Atención","Desea Salir de la aplicación")
def informacion():
    messagebox.showinfo("Informacion","Proyecto de Gestion de Personas")
#-----------------------------
#VARIABLES DE LOS CAMPOS
txt_id=StringVar()
minombre=StringVar()
txt_apellido=StringVar()
txt_direccion=StringVar()
txt_contra=StringVar()


ventana.geometry("500x600")

#Menu
barraMenu=Menu(ventana)
ventana.config(menu=barraMenu,width=300,height=300)
menuBd=Menu(barraMenu,tearoff=0)
menuBorrar=Menu(barraMenu,tearoff=0)
menuCrud=Menu(barraMenu,tearoff=0)
menuAyuda=Menu(barraMenu,tearoff=0)

barraMenu.add_cascade(label="BBDD", menu=menuBd)
barraMenu.add_cascade(label="Borrar", menu=menuBorrar)
barraMenu.add_cascade(label="Crud", menu=menuCrud)
barraMenu.add_cascade(label="Ayuda", menu=menuAyuda)

#Sub_Menus BBDD
menuBd.add_command(label="Conectar",command=conectar)
menuBd.add_command(label="Salir",command=salir)

#Sub_Menus Borrar
menuBorrar.add_command(label="Borrar Campos",command=borra_campos)

#Sub_Menus CRUD
menuCrud.add_command(label="Crear",command=crear_registro)
menuCrud.add_command(label="Leer",command=leer_registro)
menuCrud.add_command(label="Actualizar",command=actualizar_registro)
menuCrud.add_command(label="Eliminar",command=eliminar_registro)


#Sub_Menus Ayuda
menuAyuda.add_command(label="Licencia",command=infoAditional)
menuAyuda.add_command(label="Acerca de...",command=informacion)

#Titulo
lbl_titulo=Label(ventana,text="Sistema de Administración de Personas")
lbl_titulo.config(fg="Blue")
lbl_titulo.pack()
#Frame
miFrame=Frame(ventana,width=500,height=400)
miFrame.place(x=10,y=10)
#Labels
lbl_id=Label(miFrame,textvariable=txt_id)
lbl_name=Label(miFrame,text="Nombre:")
lbl_name.grid(row=0,column=0,pady=10)
lbl_last_name=Label(miFrame,text="Apellido:")
lbl_last_name.grid(row=1,column=0,pady=10)
lbl_direction=Label(miFrame,text="Direccion:")
lbl_direction.grid(row=2,column=0,pady=10)
lbl_password=Label(miFrame,text="Password:")
lbl_password.grid(row=3,column=0,pady=10)
lbl_comentario=Label(miFrame,text="Comentario:")
lbl_comentario.grid(row=4,column=0,pady=10)

#Cajas de texto
nombre=Entry(miFrame,textvariable=minombre)
nombre.grid(row=0,column=1)
apellido=Entry(miFrame,textvariable=txt_apellido)
apellido.grid(row=1,column=1)
direccion=Entry(miFrame,textvariable=txt_direccion)
direccion.grid(row=2,column=1)
contra=Entry(miFrame,textvariable=txt_contra)
contra.grid(row=3,column=1)


#Area de texto
comentario=Text(miFrame,width=13,height=5)
comentario.grid(row=4,column=1,pady=5)



#Boton
def codigoBoton():
    minombre.set("Veronica")
    print(minombre.get())
#Boton 


#Panel de controles "FRAME"

frame2=Frame(ventana,width=500,height=60,bg="red")
frame2.place(x=10,y=10)




#Botones


btnCrear=Button(frame2,text="Crear",command=crear_registro)
btnCrear.grid(row=0,column=0,padx=5,pady=20)

btnLeer=Button(frame2,text="Leer",command=leer_registro)
btnLeer.grid(row=0,column=1,padx=5)

btnActualizar=Button(frame2,text="Actualizar",command=actualizar_registro)
btnActualizar.grid(row=0,column=2,padx=5)

btnEliminar=Button(frame2,text="Eliminar",command=eliminar_registro)
btnEliminar.grid(row=0,column=3,padx=5)

#Frame
miFrame1=Frame(ventana,width=500,height=400)
miFrame1.pack()
miFrame1.place(x=10,y=10)
# Crear tabla
tabla = ttk.Treeview(miFrame1)

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

# Mostrar tabla
tabla.pack()


#Mostrar ventana
ventana.mainloop()
