# Implementar la funcion borrar_persona, que elimina un registro en la tabla Persona.
# Devuelve un booleano en base a si encontro el registro y lo borro o no.

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


def borrar_persona(id_persona):
    user = session.query(Persona).filter(Persona.IdPersona == id_persona).delete(synchronize_session=False)
    session.commit()
    return user


#
# @reset_tabla
# def pruebas():
#     assert borrar_persona(agregar_persona('juan perez', datetime.datetime(1988, 5, 15), 32165498, 180))
#     assert borrar_persona(12345) is False
#
# if __name__ == '__main__':
#     pruebas()


print(borrar_persona(1))


#link util https://kite.com/python/docs/sqlalchemy.orm.query.Query.delete
