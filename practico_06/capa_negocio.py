# Implementar los metodos de la capa de negocio de socios.

from practico_05.ejercicio_01 import Socio
from practico_05.ejercicio_02 import DatosSocio


class DniRepetido(Exception):
    pass


class LongitudInvalida(Exception):
    pass


class MaximoAlcanzado(Exception):
    pass


class NegocioSocio(object):

    MIN_CARACTERES = 3
    MAX_CARACTERES = 15
    MAX_SOCIOS = 200

    def __init__(self):
        self.datos = DatosSocio()

    def buscar(self, id_socio):
        """
        Devuelve la instancia del socio, dado su id.
        Devuelve None si no encuentra nada.
        :rtype: Socio
        """
        ds = DatosSocio()

        return ds.buscar(id_socio)

    def buscar_dni(self, dni_socio):
        """
        Devuelve la instancia del socio, dado su dni.
        Devuelve None si no encuentra nada.
        :rtype: Socio
        """
        ds = DatosSocio()

        return ds.buscar_dni(dni_socio)

    def todos(self):
        """
        Devuelve listado de todos los socios.
        :rtype: list
        """
        ds = DatosSocio()

        return ds.todos()

    def alta(self, socio):
        """
        Da de alta un socio.
        Se deben validar las 3 reglas de negocio primero.
        Si no validan, levantar la excepcion correspondiente.
        Devuelve True si el alta fue exitoso.
        :type socio: Socio
        :rtype: bool
        """
        neg = NegocioSocio()
        ds = DatosSocio()
        ds2 = ds.buscar_dni(socio.dni)
        if neg.regla_1(socio)==False:
            return False
        if neg.regla_2(socio)==False:
            return False
        if neg.regla_3(socio)==False:
            return False
        return True

    def baja(self, id_socio):
        """
        Borra el socio especificado por el id.
        Devuelve True si el borrado fue exitoso.
        :rtype: bool
        """

        ds = DatosSocio()

        return ds.baja(id_socio)

    def modificacion(self, socio):
        """
        Modifica un socio.
        Se debe validar la regla 2 primero.
        Si no valida, levantar la excepcion correspondiente.
        Devuelve True si la modificacion fue exitosa.
        :type socio: Socio
        :rtype: bool
        """
        neg = NegocioSocio
        ds = DatosSocio
        a=True
        try:
            if (len(socio.nombre)>neg.MAX_CARACTERES):
                a=False
            if (len(socio.nombre)<neg.MIN_CARACTERES):
                a=False
        except LongitudInvalida as error:
            print("La longitud es invalida por lo tanto no puede modificarse el socio")

        if a==True:
            ds.modificacion(socio)
        return False

    def regla_1(self, socio):
        """
        Validar que el DNI del socio es unico (que ya no este usado).
        :type socio: Socio
        :raise: DniRepetido
        :return: bool
        """
        ds = DatosSocio
        neg = NegocioSocio
        ds2 = DatosSocio.buscar_dni(socio.dni)
        try:
            if(socio.dni==ds2.dni):
                error = Exception
        except DniRepetido as error:
            print("El dni ya esta cargado al sistema")
            return False


        return True

    def regla_2(self, socio):
        """
        Validar que el nombre y el apellido del socio cuenten con mas de 3 caracteres pero menos de 15.
        :type socio: Socio
        :raise: LongitudInvalida
        :return: bool
        """
        ds = DatosSocio
        neg = NegocioSocio
        nom=len(socio.nombre)
        ape=len(socio.apellido)
        try:
            if(nom>neg.MAX_CARACTERES or nom<neg.MIN_CARACTERES or ape>neg.MAX_CARACTERES or ape<neg.MIN_CARACTERES):
                error = Exception
        except LongitudInvalida as error:
            print("Longitud invalida en nombre o apellido del socio")
            return False

        return True

    def regla_3(self):
        """
        Validar que no se esta excediendo la cantidad maxima de socios.
        :raise: MaximoAlcanzado
        :return: bool
        """
        ds = DatosSocio
        neg = NegocioSocio
        cant = len(ds.todos())

        try:
            if cant>neg.MAX_SOCIOS:
                error = Exception
        except MaximoAlcanzado as error:
            print("Se ha alcanzado el maximo permitido de socios")
            return False
        return True
