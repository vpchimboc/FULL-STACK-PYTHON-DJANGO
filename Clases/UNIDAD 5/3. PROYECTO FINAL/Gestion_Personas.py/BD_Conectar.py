import sqlite3


class BD_Conectar:
    #Crear conexion BD

    
    #Crear cursor
    #cursor=miConexion.cursor()
    id_recibe=0
    
    def __init__(self) -> None:
        pass

    def conexion(self):
        
        print("Si pase conectado")
        miConexion=sqlite3.connect("PrimerBase.sqlite")
        cursor=miConexion.cursor()
        cursor.execute(
        "CREATE TABLE IF NOT EXISTS PERSONA (ID INTEGER PRIMARY KEY AUTOINCREMENT, NOMBRE VARCHAR(25),APELLIDO VARCHAR(25), DIRECCION VARCHAR(45),PASSWORD VARCHAR(15),COMENTARIO VARCHAR(100))")
        miConexion.commit()
        miConexion.close()
        

    #miConexion.commit()
    #miConexion.close()

    #INSERTAR DATOS
    def insertar(self,nombre,apellido,direccion,clave,comentario):
        miConexion=sqlite3.connect("PrimerBase.sqlite")
        cursor=miConexion.cursor()

        datos=(nombre,apellido,direccion,clave,comentario)
        sql="INSERT INTO PERSONA VALUES(NULL,?,?,?,?,?)"
        cursor.execute(sql,datos)
        miConexion.commit()
        miConexion.close()
    #LISTAR REGISTROS
    def listar(self,id):
        id=str(id)
        miConexion=sqlite3.connect("PrimerBase.sqlite")
        cursor=miConexion.cursor()
        cursor.execute("SELECT* FROM PERSONA WHERE ID="+id+"")
        listaRegistros=cursor.fetchall()

        print("Datos listados")
        miConexion.commit()
        miConexion.close()
        return listaRegistros
   #LISTAR REGISTROS
    def listarTodos(self):
        miConexion=sqlite3.connect("PrimerBase.sqlite")
        cursor=miConexion.cursor()
        cursor.execute("SELECT* FROM PERSONA")
        listaRegistros=cursor.fetchall()
        print("Datos listados")
        miConexion.commit()
        miConexion.close()
        return listaRegistros
    #ACTUALIZAR REGISTRO
    def actualizar(self,nombre,apellido,direccion,clave,comentario,id):
        id=str(id)
        miConexion=sqlite3.connect("PrimerBase.sqlite")
        cursor=miConexion.cursor()
        
        cursor.execute("UPDATE PERSONA SET NOMBRE='"+nombre+"',APELLIDO='"+apellido+"',DIRECCION='"+direccion+"',PASSWORD='"+clave+"',COMENTARIO='"+comentario+"' WHERE ID="+id+"")
        print("El registro ha sido actualizas")
        miConexion.commit()
        miConexion.close()

    #ELIMAR REGISTRO
    def eleminar(self,id):
        id=str(id)
        miConexion=sqlite3.connect("PrimerBase.sqlite")
        cursor=miConexion.cursor()
        cursor.execute("DELETE FROM PERSONA WHERE ID="+id+"")
        print("El registro ha sido eliminado")
        miConexion.commit()
        miConexion.close()

"""

    cursor.execute(
        "CREATE TABLE PRODUCTOS (ID INTEGER PRIMARY KEY AUTOINCREMENT, NOMBRE VARCHAR(25),CANTIDAD INTEGER,OBSERVACION VARCHAR(45))")

    #cursor.execute("INSERT INTO PRODUCTOS VALUES(NULL,'PC',5,'No hay observacion')")
    productos=[
        ('PC',5,'No hay observacion'),
        ('Mouse',4,'No hay observacion'),
        ('Pantalla',8,'No hay observacion'),
        ('Flas',20,'No hay observacion')
    ]
    #cursor.executemany("INSERT INTO PRODUCTOS VALUES(NULL,?,?,?,?)",productos)
    #LEER la lista
    cursor.execute("Select* FROM PRODUCTOS")
    listaProductos=cursor.fetchall()

    for producto in listaProductos:
        print("ID:",producto[0],"Nombre:",producto[1],"Cantidad:",producto[2],"Observación:",producto[3])
    cursor.execute("UPDATE PRODUCTOS SET CANTIDAD=20 WHERE ID=1")
    cursor.execute("DELETE FROM PRODUCTOS WHERE ID=4")
    """
