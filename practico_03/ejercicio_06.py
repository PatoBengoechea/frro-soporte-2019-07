# Implementar la funcion crear_tabla_peso, que cree una tabla PersonaPeso con:
# - IdPersona: Int() (Clave Foranea Persona)
# - Fecha: Date()
# - Peso: Int()

# Implementar la funcion borrar_tabla, que borra la tabla creada anteriormente.

from ejercicio_01 import borrar_tabla, crear_tabla

import mysql.connector

mydb = mysql.connector.connect(
    host = 'localhost',
    user ='root',
    passwd = '2458L.a.m',
    database ='practica3'
)

mycur = mydb.cursor()

def crear_tabla_peso():
    mycur.execute( "CREATE TABLE personaPeso(" 
          "idPeso int PRIMARY KEY AUTO_INCREMENT," 
          "fecha date," 
          "peso int,"
          "idPersona int,"
          "FOREIGN KEY (idPersona) REFERENCES persona(id_persona));")


def borrar_tabla_peso():
    mycur.execute("DROP TABLE personaPeso")


# no modificar
def reset_tabla(func):
    def func_wrapper():
        crear_tabla()
        crear_tabla_peso()
        func()
        borrar_tabla_peso()
        borrar_tabla()
    return func_wrapper
