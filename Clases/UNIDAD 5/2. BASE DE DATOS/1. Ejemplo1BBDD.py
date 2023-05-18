import sqlite3
#1.Crear la conexion
miConexion=sqlite3.connect("HistorialClinicoDBD")
#2. Crear el cursor
cursor=miConexion.cursor()
#3. Ejecutar Query
cursor.execute("CREATE TABLE PACIENTE(NOMBRE VARCHAR(50),EDAD INTEGER,DIRECCION VARCHAR(20))")
#4. Insertar Datos
cursor.execute("INSERT INTO PACIENTE VALUES ('Veronica',31,'CUENCA')")
miConexion.commit()
miConexion.close()