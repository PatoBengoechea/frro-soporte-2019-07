# Implementar la funcion agregar_persona, que inserte un registro en la tabla Persona
# y devuelva los datos ingresados el id del nuevo registro.

import datetime

#from practico_03.ejercicio_01 import reset_tabla

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


def agregar_persona(nombre, nacimiento, dni, altura):
    per = Persona()
    per.Nombre =nombre
    per.FechaNacimiento = nacimiento
    per.Dni = dni
    per.Altura = altura
    session.add(per)
    session.commit()


#@reset_tabla
#def pruebas():
 #   id_juan = agregar_persona('juan perez', datetime.datetime(1988, 5, 15), 32165498, 180)
 #   id_marcela = agregar_persona('marcela gonzalez', datetime.datetime(1980, 1, 25), 12164492, 195)
  #  assert id_juan > 0
  #  assert id_marcela > id_juan

#if __name__ == '__main__':
#    pruebas()

agregar_persona('Patricio', '1995-11-1', 99999, 185)
