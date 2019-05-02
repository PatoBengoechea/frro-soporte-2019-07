# Implementar la funcion agregar_persona, que inserte un registro en la tabla Persona
# y devuelva los datos ingresados el id del nuevo registro.

import datetime

from ejercicio_01 import reset_tabla

import mysql.connector

mydata = mysql.connector.connect(
    host="localhost",
    user="root",
    passwd="2458L.a.m",
    database="practica3"
)

mycurr = mydata.cursor()

def agregar_persona(nombre, nacimiento, dni, altura):
    sql = "INSERT INTO persona(Nombre, FechaNacimiento, Dni, Altura) VALUES (%s, %s, %s, %s)"
    val = (nombre, nacimiento, dni, altura)
    print(val)
    mycurr.execute(sql,val)
    mydata.commit()
    print(mycurr.rowcount, "registro cargado")
    return mycurr.lastrowid





@reset_tabla
def pruebas():
    id_juan = agregar_persona('juan perez', datetime.datetime(1988, 5, 15), 32165498, 180)
    id_marcela = agregar_persona('marcela gonzalez', datetime.datetime(1980, 1, 25), 12164492, 195)
    assert (id_juan == 1)
    assert (id_marcela < id_juan) == False

if __name__ == '__main__':
    pruebas()

