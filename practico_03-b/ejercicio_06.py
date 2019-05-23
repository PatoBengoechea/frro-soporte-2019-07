# Implementar la funcion crear_tabla_peso, que cree una tabla PersonaPeso con:
# - IdPersona: Int() (Clave Foranea Persona)
# - Fecha: Date()
# - Peso: Int()

# Implementar la funcion borrar_tabla, que borra la tabla creada anteriormente.

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


def crear_tabla_peso():
    ____tablename__ = 'tabla_peso'
    IdPersona = Column(Integer, ForeignKey("Persona.IdPersona"))
    Fecha = Column(Date)
    Peso = Column(Integer)


def borrar_tabla_peso():
    Base.metadata.drop_all(bind=engine, tables=[tabla_peso.__table__])


# no modificar
def reset_tabla(func):
    def func_wrapper():
        crear_tabla()
        crear_tabla_peso()
        func()
        borrar_tabla_peso()
        borrar_tabla()
    return func_wrapper
