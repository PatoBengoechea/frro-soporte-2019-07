# Implementar la funcion borrar_persona, que elimina un registro en la tabla Persona.
# Devuelve un booleano en base a si encontro el registro y lo borro o no.

import datetime

from ejercicio_01 import reset_tabla
from ejercicio_02 import agregar_persona

import mysql.connector

mydb = mysql.connector.connect(
    host ="localhost",
    user ="root",
    passwd ="2458L.a.m",
    database ="practica3"
)

mycurr = mydb.cursor()

def borrar_persona(id_persona):
    sql = "DELETE FROM persona WHERE IdPersona = %s"
    val = (id_persona, )
    mycurr.execute(sql, val)
    mydb.commit()

    if mycurr.rowcount == 0:
        return False
    else:
        return True


@reset_tabla
def pruebas():
    assert borrar_persona(agregar_persona('juan perez', datetime.datetime(1988, 5, 15), 32165498, 164))
    assert borrar_persona(12345) is False

if __name__ == '__main__':
    pruebas()
