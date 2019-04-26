# Implementar la funcion agregar_peso, que inserte un registro en la tabla PersonaPeso.
# Debe validar:
# - que el ID de la persona ingresada existe (reutilizando las funciones ya implementadas).
# - que no existe de esa persona un registro de fecha posterior al que queremos ingresar.

# Debe devolver:
# - ID del peso registrado.
# - False en caso de no cumplir con alguna validacion.

import datetime

from ejercicio_02 import agregar_persona
from ejercicio_06 import reset_tabla
from ejercicio_04 import buscar_persona

import mysql.connector

mydb = mysql.connector.connect(
    host = 'localhost',
    user = 'root',
    passwd = '2458L.a.m',
    database = 'practica3'
)

mycur = mydb.cursor()

def buscar_personaPeso(id_persona):
    sql = "SELECT * FROM personaPeso WHERE idPersona = %s"
    val = (id_persona, )
    mycur.execute(sql, val)
    myresult = mycur.fetchall()

    if myresult == []:
        return False
    else:
        return myresult[0]

def control_fecha(fecha):
    mycur.execute("SELECT max(fecha) FROM personaPeso;")
    result = mycur.fetchall()
    if result[0][0] == None:
        return True
    elif result[0][0] > fecha.date():
        return False
    else:
        return True


def agregar_peso(id_persona, fecha, peso):
    if buscar_persona(id_persona) == False:
        print("La persona no existe")
        pass
    else:
        if control_fecha(fecha):
            sql = "INSERT INTO personaPeso(idPersona, fecha, peso) VALUES (%s, %s, %s)"
            val = (id_persona, fecha, peso)
            mycur.execute(sql,val)
            print(mycur.rowcount, "Registro Cargado")
            mydb.commit()
        else:
            print("Ya exite un registro posterior cargado.")


@reset_tabla
def pruebas():
    id_juan = agregar_persona('juan perez', datetime.datetime(1988, 5, 15), 32165498, 180)
    assert agregar_peso(id_juan, datetime.datetime(2018, 5, 26), 80) > 0
    # id incorrecto
    assert agregar_peso(200, datetime.datetime(1988, 5, 15), 80) == False
    # registro previo al 2018-05-26
    assert agregar_peso(id_juan, datetime.datetime(2018, 5, 16), 80) == False

if __name__ == '__main__':
    pruebas()
