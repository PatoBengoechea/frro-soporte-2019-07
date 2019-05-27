# Implementar la funcion agregar_peso, que inserte un registro en la tabla PersonaPeso.
# Debe validar:
# - que el ID de la persona ingresada existe (reutilizando las funciones ya implementadas).
# - que no existe de esa persona un registro de fecha posterior al que queremos ingresar.

# Debe devolver:
# - ID del peso registrado.
# - False en caso de no cumplir con alguna validacion.

import datetime
from ejercicio_06 import Peso
from ejercicio_04 import buscar_persona


from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import create_engine, Column, Integer, DateTime, ForeignKey
from sqlalchemy.orm import sessionmaker, relationship


Base = declarative_base()

engine = create_engine('sqlite:///socios.db', echo=True)
Base.metadata.create_all(bind=engine)
Session = sessionmaker(bind=engine)

session = Session()


def agregar_peso(id, fecha, peso):

    user = buscar_persona(id)
    aux= False

    if user == False:
        print('El usuario no existe')
        return False
    else:
        pesos = session.query(Peso)
        for p in pesos:
            if p.fecha >= fecha:
                print('Existe una fecha posterior de peso')
                print('No se actualizaron registros')
                aux = True
                return False

        if aux == False:

            npeso = Peso()

            npeso.fecha = fecha
            npeso.peso = peso
            npeso.id_persona = id

            session.add(npeso)
            session.commit()

            obj = session.query(Peso).order_by(Peso.idPeso.desc()).first()
            return obj.idPeso

        else:
            pass






agregar_peso(1, datetime.datetime(2019, 8, 15), 71)

'''
@reset_tabla
def pruebas():
    id_juan = agregar_persona('juan perez', datetime.datetime(1988, 5, 15), 32165498, 180)
    assert agregar_peso(id_juan, datetime.datetime(2018, 5, 26), 80) > 0
    # id incorrecto
    assert agregar_peso(200, datetime.datetime(1988, 5, 15), 80) == False
    # registro previo al 2018-05-26
    assert agregar_peso(id_juan, datetime.datetime(2018, 5, 16), 80) == False

if __name__ == '__main__':
    pruebas()
'''
