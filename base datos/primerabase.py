import sqlite3

conexion = sqlite3.connect("PrimeraBase.db")

cursor = conexion.cursor()
#cursor.execute("CREATE TABLE USUARIOS(NOMBRE VARCHAR(50), EDAD INTEGER, SEXO VARCHAR(50))")

#cursor.execute("INSERT INTO USUARIOS VALUES('Juan Ignacio Irigoin', 33, 'Masculino')")
#cursor.execute("INSERT INTO USUARIOS VALUES('Marisol Minoli', 31, 'Femenino')")

#cursor.execute("SELECT * FROM USUARIOS")
#usuario = cursor.fetchone()
#print(usuario)

#usuarios = [
#    ('Alberto Minoli', 67, 'Masculino'),
#    ('Ana Delgado', 50, 'Femenino'),
#    ('Estefania Gomez', 22, 'Femenino')
#]
#cursor.executemany("INSERT INTO USUARIOS VALUES(?,?,?)", usuarios)

cursor.execute("SELECT * FROM USUARIOS")
usuarios = cursor.fetchall()
for usuario in usuarios:
    print (usuario)

conexion.commit()
conexion.close()