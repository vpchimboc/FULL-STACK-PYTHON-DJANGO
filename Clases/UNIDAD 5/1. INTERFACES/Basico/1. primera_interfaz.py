from tkinter import *
raiz=Tk()
raiz.title("Primera Ventana")
#raiz.config(width=300,height=300)
raiz.resizable(0,0)
def habilitar_frame():
    miFrame.pack()

def deshabilitar_frame():
    miFrame.pack_forget()
raiz.iconbitmap("imagen.ico")
raiz.geometry("600x350")
raiz.config(bg="blue")
###Frame
miFrame=Frame()
#miFrame.pack(side="top" ,anchor="center")
miFrame.pack(fill="both",expand=True)
miFrame.config(cursor="pirate",bg="red",width=300,height=300, relief="groove",bd=35)

botonEnvio=Button(miFrame,text="Enviar", command=deshabilitar_frame)
botonEnvio.pack()

raiz.mainloop()