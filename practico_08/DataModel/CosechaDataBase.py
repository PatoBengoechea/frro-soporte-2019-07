from DataModel.Database import Database
from Model.Cosecha import Cosecha
from Model.User import User
from Model.Venta import Venta
from bson import ObjectId
from datetime import date


class CosechaData:
    def getCosechas(self, productor):
        db = Database()
        cursor = db.main()
        cosechas = []
        try:
            data = cursor.cosecha.find({"productor" : productor})
            for i in data:
                ventas = []
                id = i["_id"]
                ventasJSON = cursor.ventas.find({"cosecha":ObjectId(id)})
                for ven in ventasJSON:
                    v = Venta()
                    v.fecha = ven["fecha"]
                    v.cantidad = ven["cantidad"]
                    v.monto = ven["monto"]
                    ventas.append(v)
                nc = Cosecha(id, i["cereal"], i["cantidadProduccion"], i["cantidadParcial"], i["inicio"], i["fin"], i["productor"], ventas)
                nc.id = id
                productorJSON = cursor.usuario.find_one({"user": productor})
                productorObject = User()
                productorObject.parse(productorJSON)
                nc.productor = productorObject
                cosechas.append(nc)
            return cosechas
        except NameError:
            print(NameError)
            return None


    def addCosecha(self, cosecha):
        db = Database()
        cursor = db.main()
        newCosecha = {
            'id': cosecha.id,
            'cereal' : cosecha.cereal,
            'cantidadProduccion' : cosecha.cantidadProduccion,
            'cantidadParcial' : cosecha.cantidadProduccion,
            'inicio' : cosecha.inicio,
            'fin' : cosecha.fin,
            'productor' : cosecha.productor
        }
        print(newCosecha)
        try:
            cursor.cosecha.insert_one(newCosecha)
            print("OK")
            return True
        except:
            print("wrong")
            return False

    def getLast(self):
        db = Database()
        cursor = db.main()
        r =cursor.cosecha.find()
        return r

#borrar
a = CosechaData()
b = a.getLast()
array = []
for i in b:
    array.append(i)
print(array[-1]['id'])

