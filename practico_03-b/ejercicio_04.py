# Implementar la funcion buscar_persona, que devuelve el registro de una persona basado en su id.
# El return es una tupla que contiene sus campos: id, nombre, nacimiento, dni y altura.
# Si no encuentra ningun registro, devuelve False.

import datetime

# from practico_03.ejercicio_01 import reset_tabla
# from practico_03.ejercicio_02 import agregar_persona


from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import create_engine, MetaData, Table, Column, Integer, String, Date, VARCHAR
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


def buscar_persona(id_persona):
    user = session.query(Persona).filter(Persona.IdPersona == id_persona)
    print(user)
    return user


# @reset_tabla
# def pruebas():
#     juan = buscar_persona(agregar_persona('juan perez', datetime.datetime(1988, 5, 15), 32165498, 180))
#     assert juan == (1, 'juan perez', datetime.datetime(1988, 5, 15), 32165498, 180)
#     assert buscar_persona(12345) is False
#
# if __name__ == '__main__':
#     pruebas()

buscar_persona(2)
