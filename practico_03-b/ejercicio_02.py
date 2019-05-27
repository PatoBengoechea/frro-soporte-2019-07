# Implementar la funcion agregar_persona, que inserte un registro en la tabla Persona
# y devuelva los datos ingresados el id del nuevo registro.

import datetime

from ejercicio_01 import reset_tabla
from ejercicio_01 import Persona


from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

Base = declarative_base()

engine = create_engine('sqlite:///socios.db', echo=True)
Base.metadata.create_all(bind=engine)
Session = sessionmaker(bind=engine)

session = Session()


def agregar_persona(nombre, nacimiento, dni, altura):

    soc1 = Persona()

    soc1.dni = dni
    soc1.nombre = nombre
    soc1.altura = altura
    soc1.fechaNacimiento = nacimiento

    session.add(soc1)
    session.commit()

    obj = session.query(Persona).order_by(Persona.idPersona.desc()).first()

    print('Persona id: %s, Nombre: %s' % (obj.idPersona, obj.nombre))


#@reset_tabla
#def pruebas():
 #   id_juan = agregar_persona('juan perez', datetime.datetime(1988, 5, 15), 32165498, 180)
 #   id_marcela = agregar_persona('marcela gonzalez', datetime.datetime(1980, 1, 25), 12164492, 195)
  #  assert id_juan > 0
  #  assert id_marcela > id_juan

#if __name__ == '__main__':
#    pruebas()

agregar_persona('Patricio', datetime.datetime(1995, 8, 1), 11111, 185)
agregar_persona('Juan', datetime.datetime(1995, 12, 1), 99999, 164)
agregar_persona('Sofia', datetime.datetime(1995, 4, 15), 12121, 163)
