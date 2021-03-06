# Implementar la funcion crear_tabla_peso, que cree una tabla PersonaPeso con:
# - IdPersona: Int() (Clave Foranea Persona)
# - Fecha: Date()
# - Peso: Int()

# Implementar la funcion borrar_tabla, que borra la tabla creada anteriormente.

from ejercicio_01 import Persona

from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import create_engine, Column, Integer, DateTime, ForeignKey
from sqlalchemy.orm import sessionmaker, relationship

Base = declarative_base()

engine = create_engine('sqlite:///socios.db', echo=True)
Base.metadata.create_all(bind=engine)
Session = sessionmaker(bind=engine)

session = Session()

class Peso(Base):

    __tablename__='personaPeso'

    idPeso = Column('idPeso', Integer, primary_key=True, autoincrement=True)
    id_persona = Column(Integer, ForeignKey(Persona.idPersona))
    fecha = Column('fecha', DateTime)
    peso = Column('peso', Integer, nullable= False)


'''
def func_wrapper():
    crear_tabla()
    crear_tabla_peso()
    func()
    borrar_tabla_peso()
    borrar_tabla()
'''
def crear_tabla_peso():

    Base.metadata.create_all(engine)


def borrar_tabla_peso():

    Peso.__table__.drop(engine)



crear_tabla_peso()

'''
# no modificar
def reset_tabla(func):
    return func_wrapper
'''
