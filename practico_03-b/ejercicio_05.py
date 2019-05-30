# Implementar la funcion actualizar_persona, que actualiza un registro de una persona basado en su id.
# Devuelve un booleano en base a si encontro el registro y lo actualizo o no.

import datetime

from ejercicio_01 import Persona
from ejercicio_04 import buscar_persona

from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import create_engine, MetaData, Table, Column, Integer, String, Date, VARCHAR
from sqlalchemy.orm import sessionmaker


Base = declarative_base()

engine = create_engine('sqlite:///socios.db', echo=True)
Base.metadata.create_all(bind=engine)
Session = sessionmaker(bind=engine)

session = Session()


def actualizar_persona(id_persona, nombre, nacimiento, dni, altura):
    aux = buscar_persona(id_persona)

    if aux == False:

        return False
    else:
        persona = session.query(Persona).filter(Persona.idPersona == id_persona).one()
        persona.nombre = nombre
        persona.nacimiento = nacimiento
        persona.dni = dni
        persona.altura = altura

        session.commit()

        return True

actualizar_persona(3, 'cacho', datetime.datetime(1995, 12, 1), 99999, 185)

'''
@reset_tabla
def pruebas():
    id_juan = agregar_persona('juan perez', datetime.datetime(1988, 5, 15), 32165498, 180)
    actualizar_persona(id_juan, 'juan carlos perez', datetime.datetime(1988, 4, 16), 32165497, 181)
    assert buscar_persona(id_juan) == (1, 'juan carlos perez', datetime.datetime(1988, 4, 16), 32165497, 181)
    assert actualizar_persona(123, 'nadie', datetime.datetime(1988, 4, 16), 12312312, 181) is False

if __name__ == '__main__':
    pruebas()
'''
