# Implementar la funcion agregar_peso, que inserte un registro en la tabla PersonaPeso.
# Debe validar:
# - que el ID de la persona ingresada existe (reutilizando las funciones ya implementadas).
# - que no existe de esa persona un registro de fecha posterior al que queremos ingresar.

# Debe devolver:
# - ID del peso registrado.
# - False en caso de no cumplir con alguna validacion.

import datetime

# from practico_03.ejercicio_02 import agregar_persona
# from practico_03.ejercicio_06 import reset_tabla

from ejercicio_04 import buscar_persona

from practico_03.ejercicio_01 import borrar_tabla, crear_tabla
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import create_engine, MetaData, Table, Column, Integer, String, Date, VARCHAR, ForeignKey
from sqlalchemy.orm import sessionmaker

Base = declarative_base()

class Persona(Base):
    __tablename__='Persona'
    IdPersona = Column(Integer, primary_key=True)
    Nombre = Column(VARCHAR(30))
    FechaNacimiento = Column(Date)
    Dni = Column(Integer)
    Altura = Column(Integer)


engine = create_engine('mysql://root:root@localhost:3306/soporte2019')
Base.metadata.bind = engine
DBSession = sessionmaker()
DBSession.bind = engine
session = DBSession()


def agregar_peso(id_persona, fecha, peso):
    user = buscar_persona(id_persona)



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
