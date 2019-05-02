# Implementar la funcion crear_tabla, que cree una tabla Persona con:
# - IdPersona: Int() (autoincremental)
# - Nombre: Char(30)
# - FechaNacimiento: Date()
# - DNI: Int()
# - Altura: Int()

# Implementar la funcion borrar_tabla, que borra la tabla creada anteriormente.
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




def crear_tabla():

    Base.metadata.create_all(engine)


def borrar_tabla():
    Persona.__table__.drop()

# no modificar
def reset_tabla(func):
    def func_wrapper():
        crear_tabla()
        func()
        borrar_tabla()
    return func_wrapper


crear_tabla()
