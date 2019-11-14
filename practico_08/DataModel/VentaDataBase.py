from DataModel.Database import Database
from Model.Cosecha import Cosecha
from Model.User import User
from Model.Venta import Venta
from bson import ObjectId
from datetime import date

class VentaDataBase:

    def addVenta(self, cosecha, precioUnitario, cantidad):
        db = Database()
        cursor = db.main()
        monto = precioUnitario*cantidad
        try:
            newVenta = {
                'cosecha': cosecha,
                'fecha': date.today().strftime("%d/%m/%y"),
                'cantidad': cantidad,
                'monto': monto
            }
            cursor.ventas.insert_one(newVenta)
            #print('Venta Agregada')
            return True
        except NameError:
            print(NameError)
            return False


    def getVentas(self, cosecha):
        db = Database()
        cursor = db.main()
        try:
            ventasJSON = cursor.ventas.find({"cosecha": cosecha})
            ventas = []
            for v in ventasJSON:
                ven = Venta()
                ven.cantidad = v['cantidad']
                ven.monto = v['monto']
                ven.fecha = v['fecha']
                ventas.append(ven)
            return ventas
        except NameError:
            print(NameError)
            return None

