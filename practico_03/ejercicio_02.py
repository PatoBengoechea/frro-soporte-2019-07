# Implementar la funcion agregar_persona, que inserte un registro en la tabla Persona
# y devuelva los datos ingresados el id del nuevo registro.

import datetime

import mysql.connector

from practico_03.ejercicio_01 import reset_tabla

mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    passwd="2458L.a.m",
    database="practica3"
)

mycursor = mydb.cursor()



def agregar_persona(nombre, nacimiento, dni, altura):

    sql = "INSERT INTO Persona (Nombre, FechaNacimiento, DNI, Altura) VALUES (%s, %s, %s, %s)"
    val = (nombre, nacimiento, dni, altura)
    mycursor.execute(sql, val)
    mydb.commit()
    print(mycursor.rowcount, "registro cargado")

    return 0


@reset_tabla
def pruebas():
    id_juan = agregar_persona('juan perez', datetime.datetime(1988, 5, 15), 32165498, 180)
    id_marcela = agregar_persona('marcela gonzalez', datetime.datetime(1980, 1, 25), 12164492, 195)
    assert id_juan == 0
    assert (id_marcela > id_juan) == False

if __name__ == '__main__':
    pruebas()
