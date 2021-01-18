import sqlite3

conexion = sqlite3.connect("Productos.db")
cursor = conexion.cursor()

##cursor.execute('''
##    CREATE TABLE PRODUCTOS(
##        CODIGO_P VARCHAR(20)PRIMARY KEY,
##        NOMBRE_P VARCHAR(20),
##        SECCION_P VARCHAR(20))
##''')

##productos= [
##    ('AR1', 'Leche', 'Lacteos'),
##    ('AR2', 'Facturas', 'Panaderia'),
##    ('AR3', 'Asado', 'Carniceria'),
##]
##
##
##cursor.executemany("INSERT INTO PRODUCTOS VALUES(?,?,?)", productos)
##cursor.execute("INSERT INTO PRODUCTOS VALUES ('AR5','Pollo','Carniceria')")

##cursor.execute('''
##    CREATE TABLE PRODUCTOS_ID(
##       ID INTEGER PRIMARY KEY AUTOINCREMENT,
##       NOMBRE VARCHAR(20),
##       PRECIO INTEGER,
##       SECCION VARCHAR(20))
##''')
##productos= [
##    ('Leche', 80, 'Lacteos'),
##    ('Facturas', 200, 'Panaderia'),
##    ('Asado', 500,'Carniceria'),
##]
##cursor.executemany("INSERT INTO PRODUCTOS_ID VALUES(NULL,?,?,?)", productos)
cursor.execute("SELECT * FROM PRODUCTOS")
productos = cursor.fetchall()
for pro in productos:
    print (pro[1])

conexion.commit()
conexion.close()