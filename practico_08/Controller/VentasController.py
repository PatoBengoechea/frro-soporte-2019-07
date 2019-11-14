from DataModel.VentaDataBase import VentaDataBase
from DataModel.CosechaDataBase import CosechaData
from Model.Venta import Venta

class VentasController:

    def addVenta(self, cosecha, precioUnitario, cantidad, cantDisp):
        if self.validaCantidad(cantidad, cantDisp):
            DB = VentaDataBase()
            try:
                DB.addVenta(cosecha, precioUnitario, cantidad)
                return True, 1
            except NameError:
                print(NameError)
                return False, 3
        else:
            return False, 2

    def getVentas(self, cosecha):
        db = VentaDataBase()
        return db.getVentas(cosecha)

    def validaCantidad(self, cantidad, cantDisp):
        if cantDisp >= cantidad:
            return True
        else:
            return False
