# Implementar la funcion crear_tabla, que cree una tabla Persona con:
# - IdPersona: Int() (autoincremental)
# - Nombre: Char(30)
# - FechaNacimiento: Date()
# - DNI: Int()
# - Altura: Int()

# Implementar la funcion borrar_tabla, que borra la tabla creada anteriormente.

import mysql.connector

mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    passwd="2458L.a.m",
    database="practica3"
)

mycursor = mydb.cursor()


def crear_tabla():
    mycursor.execute("CREATE TABLE persona ("
                     "IdPersona INT AUTO_INCREMENT PRIMARY KEY, "
                     "Nombre VARCHAR(30), "
                     "FechaNacimiento date, "
                     "DNI int, "
                     "Altura int)")


def borrar_tabla():

    mycursor.execute("DROP TABLE persona")

# no modificar
def reset_tabla(func):
    def func_wrapper():
        crear_tabla()
        func()
        borrar_tabla()
    return func_wrapper


#mydb.close()

