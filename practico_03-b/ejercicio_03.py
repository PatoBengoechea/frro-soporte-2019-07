# Implementar la funcion borrar_persona, que elimina un registro en la tabla Persona.
# Devuelve un booleano en base a si encontro el registro y lo borro o no.

from ejercicio_01 import Persona



from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

Base = declarative_base()

engine = create_engine('sqlite:///socios.db', echo=True)
Base.metadata.create_all(bind=engine)
Session = sessionmaker(bind=engine)

session = Session()



def borrar_persona(id_persona):

    users = session.query(Persona)
    x = False

    for user in users:
        if user.idPersona == id_persona:
            print('Socio id: %s, nombre: %s' % (user.idPersona, user.nombre))

            x = True
        else:
            pass

    return x


borrar_persona(1)

#
# @reset_tabla
# def pruebas():
#     assert borrar_persona(agregar_persona('juan perez', datetime.datetime(1988, 5, 15), 32165498, 180))
#     assert borrar_persona(12345) is False
#
# if __name__ == '__main__':
#     pruebas()




#link util https://kite.com/python/docs/sqlalchemy.orm.query.Query.delete
