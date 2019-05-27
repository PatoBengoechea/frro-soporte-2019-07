# Implementar la funcion buscar_persona, que devuelve el registro de una persona basado en su id.
# El return es una tupla que contiene sus campos: id, nombre, nacimiento, dni y altura.
# Si no encuentra ningun registro, devuelve False.


from ejercicio_01 import Persona


from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

Base = declarative_base()

engine = create_engine('sqlite:///socios.db', echo=True)
Base.metadata.create_all(bind=engine)
Session = sessionmaker(bind=engine)

session = Session()


def buscar_persona(id_persona):

    x = False
    users = session.query(Persona)
    for user in users:
        if user.idPersona == id_persona:
            x = True
            return (user.idPersona, user.nombre, user.dni, user.fechaNacimiento, user.altura)
        else:
            pass
    if x == False:
        return False
    else:
        pass



# @reset_tabla
# def pruebas():
#     juan = buscar_persona(agregar_persona('juan perez', datetime.datetime(1988, 5, 15), 32165498, 180))
#     assert juan == (1, 'juan perez', datetime.datetime(1988, 5, 15), 32165498, 180)
#     assert buscar_persona(12345) is False
#
# if __name__ == '__main__':
#     pruebas()



assert (buscar_persona(7) == False)

