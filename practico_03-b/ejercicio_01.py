# Implementar la funcion crear_tabla, que cree una tabla Persona con:
# - IdPersona: Int() (autoincremental)
# - Nombre: Char(30)
# - FechaNacimiento: Date()
# - DNI: Int()
# - Altura: Int()

# Implementar la funcion borrar_tabla, que borra la tabla creada anteriormente.

from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import create_engine, Column, Integer, String, DateTime
from sqlalchemy.orm import sessionmaker

import datetime

Base = declarative_base()

class Persona(Base):

    __tablename__='persona'

    idPersona = Column('idPersona', Integer, primary_key=True, autoincrement=True)
    nombre = Column('nombre', String(30))
    fechaNacimiento = Column('fechaNacimiento', DateTime)
    dni = Column('dni', Integer)
    altura = Column('Altura', Integer)


engine = create_engine('sqlite:///socios.db', echo=True)
Base.metadata.create_all(bind=engine)
Session = sessionmaker(bind=engine)

session = Session()



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


'''
#>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>Carga de datos<<<<<<<<<<<<<<<<<<<<<>>>>
soc1 = Persona()
soc1.dni = 39246898
soc1.nombre = 'Juan'
soc1.altura = 1
soc1.fechaNacimiento = datetime.datetime(1995, 12, 1)

session.add(soc1)
session.commit()

'''

