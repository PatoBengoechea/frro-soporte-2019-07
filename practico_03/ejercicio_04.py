# Implementar la funcion buscar_persona, que devuelve el registro de una persona basado en su id.
# El return es una tupla que contiene sus campos: id, nombre, nacimiento, dni y altura.
# Si no encuentra ningun registro, devuelve False.

import datetime

from practico_03.ejercicio_01 import reset_tabla
from practico_03.ejercicio_02 import agregar_persona

import mysql.connector

mydb = mysql.connector.connect(
    host = 'localhost',
    user = 'root',
    passwd = '2458L.a.m',
    database ='practica3'
)

mycurr = mydb.cursor()


def buscar_persona(id_persona):
    sql = "SELECT * FROM persona WHERE IdPersona = %s"
    val = (id_persona, )
    mycurr.execute(sql, val)
    myresult = mycurr.fetchall()

    if myresult == []:
        return False
    else:
        return myresult[0]



@reset_tabla
def pruebas():
    juan = buscar_persona(agregar_persona('juan perez', datetime.datetime(1988, 5, 15), 32165498, 180))
    assert juan == (1, 'juan perez', datetime.datetime(1988, 5, 15), 32165498, 180)
    assert buscar_persona(12345) is False

if __name__ == '__main__':
    pruebas()
