# Implementar la funcion actualizar_persona, que actualiza un registro de una persona basado en su id.
# Devuelve un booleano en base a si encontro el registro y lo actualizo o no.

import datetime

from ejercicio_01 import reset_tabla
from ejercicio_02 import agregar_persona
from ejercicio_04 import buscar_persona

import mysql.connector

mydb = mysql.connector.connect(
    host = 'localhost',
    user = 'root',
    passwd = '2458L.a.m',
    database = 'practica3'
)

mycur = mydb.cursor()


def actualizar_persona(id_persona, nombre, nacimiento, dni, altura):
    if buscar_persona(id_persona) == False:
        print("La Persona no existe")
    else:
        print("Registro actual: ")
        print(buscar_persona(id_persona))
        sql = "UPDATE persona SET nombre = %s, f_nac = %s, dni = %s, altura = %s WHERE idPersona = %s;"
        val = (nombre,nacimiento,dni, altura,id_persona)
        mycur.execute(sql, val)
        mydb.commit()
        print(mycur.rowcount, "registro actualizado")

        if mycur.rowcount == 0:
            return False
        else:
            return True
@reset_tabla
def pruebas():
    id_juan = agregar_persona('juan perez', datetime.datetime(1988, 5, 15), 32165498, 180)
    actualizar_persona(id_juan, 'juan carlos perez', datetime.datetime(1988, 4, 16), 32165497, 181)
    assert buscar_persona(id_juan) == (1, 'juan carlos perez', datetime.datetime(1988, 4, 16), 32165497, 181)
    assert actualizar_persona(123, 'nadie', datetime.datetime(1988, 4, 16), 12312312, 181) is False

if __name__ == '__main__':
    pruebas()
