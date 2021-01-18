import sqlite3

conexion = sqlite3.connect("Productos.db")

cursor = conexion.cursor()

##cursor.execute("SELECT * FROM PRODUCTOS WHERE SECCION_P= 'Panaderia'")
##
##productos = cursor.fetchall()
##print(productos)

#cursor.execute("UPDATE PRODUCTOS SET SECCION_P='PANADERIA' WHERE SECCION_P='Panaderia'")
#cursor.execute("UPDATE PRODUCTOS_ID SET PRECIO= 600 WHERE NOMBRE='Asado'")

#cursor.execute("DELETE FROM PRODUCTOS WHERE NOMBRE_P='Pollo'")

conexion.commit()
conexion.close()

