# Implementar los metodos de la capa de datos de socios.


from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from ejercicio_01 import Base, Socio

engine = create_engine('sqlite:///socios.db', echo=True)
Base.metadata.create_all(bind=engine)
Session = sessionmaker(bind=engine)

session = Session()
Base.metadata.create_all(engine)


class DatosSocio(object):

    def __init__(self):
        engine = create_engine('sqlite:///socios.db')
        Base.metadata.bind = engine
        db_session = sessionmaker()
        db_session.bind = engine
        self.session = db_session()

    def buscar(self, id_socio):
        """
        Devuelve la instancia del socio, dado su id.
        Devuelve None si no encuentra nada.
        :rtype: Socio
        """

        socio = session.query(Socio).filter_by(id = id_socio).first()
        print(socio)
        return socio


    def buscar_dni(self, dni_socio):
        """
        Devuelve la instancia del socio, dado su dni.
        Devuelve None si no encuentra nada.
        :rtype: Socio
        """
        socio = session.query(Socio).filter_by(dni=dni_socio).first()
        print(socio)
        return socio

    def todos(self):
        """
        Devuelve listado de todos los socios en la base de datos.
        :rtype: list
        """
        socios = session.query(Socio)
        return socios

    def borrar_todos(self):
        """
        Borra todos los socios de la base de datos.
        Devuelve True si el borrado fue exitoso.
        :rtype: bool
        """
        socios = session.query(Socio).delete()

        return socios

    def alta(self, socio):
        """
        Devuelve el Socio luego de darlo de alta.
        :type socio: Socio
        :rtype: Socio
        """

        soc1 = Socio()

        soc1.dni = socio.dni
        soc1.nombre = socio.nombre
        soc1.apellido = socio.apellido

        session.add(soc1)
        session.commit()

        obj = session.query(Socio).order_by(Socio.id.desc()).first()
        return obj

    def baja(self, id_socio):
        """
        Borra el socio especificado por el id.
        Devuelve True si el borrado fue exitoso.
        :rtype: bool
        """
        socios = session.query(Socio).filter(Socio.id == id_socio).delete()
        print(socios)
        if socios == 0:
            a = False
        else :
            a = True
        print(a)
        return a

    def modificacion(self, socio):
        """
        Guarda un socio con sus datos modificados.
        Devuelve el Socio modificado.
        :type socio: Socio
        :rtype: Socio
        """
        aux = DatosSocio.buscar(socio.id)

        if aux == False:

            return False
        else:
            persona = session.query(Socio).filter(Socio.id == socio.id).one()
            persona.nombre = socio.nombre
            persona.apellido = socio.apellido
            persona.dni = socio.dni

            session.commit()

            return True
            return persona


DatosSocio.buscar_dni(Socio, 12345678)

def pruebas():
    # alta
    datos = DatosSocio()
    socio = datos.alta(Socio(dni=12345678, nombre='Juan', apellido='Perez'))
    assert socio.id > 0

    # baja
    assert datos.baja(socio.id) == True

    # buscar
    socio_2 = datos.alta(Socio(dni=12345679, nombre='Carlos', apellido='Perez'))
    assert datos.buscar(socio_2.id) == socio_2

    # buscar dni
    socio_2 = datos.alta(Socio(dni=12345679, nombre='Carlos', apellido='Perez'))
    assert datos.buscar(socio_2.dni) == socio_2

    # modificacion
    socio_3 = datos.alta(Socio(dni=12345680, nombre='Susana', apellido='Gimenez'))
    socio_3.nombre = 'Moria'
    socio_3.apellido = 'Casan'
    socio_3.dni = 13264587
    datos.modificacion(socio_3)
    socio_3_modificado = datos.buscar(socio_3.id)
    assert socio_3_modificado.id == socio_3.id
    assert socio_3_modificado.nombre == 'Moria'
    assert socio_3_modificado.apellido == 'Casan'
    assert socio_3_modificado.dni == 13264587

    # todos
    assert len(datos.todos()) == 2

    # borrar todos
    datos.borrar_todos()
    assert len(datos.todos()) == 0


if __name__ == '__main__':
    pruebas()

