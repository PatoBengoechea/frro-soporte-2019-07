from DataModel.CosechaDataBase import  CosechaData
from Model.Cosecha import Cosecha


class CosechaController:

    def createCocecha(self, id, cereal, cantidad, inicio, fin, productor ):
        dbCosecha = CosechaData()
        emptyArray = [] #pruebaJuanchi
        nuevaCosecha = Cosecha(id, cereal, cantidad, cantidad, inicio, fin, productor, emptyArray)
        response = dbCosecha.addCosecha(nuevaCosecha)
        if(response):
            return nuevaCosecha
        else:
            return False


    def getCocecha(self, productorActual):
        dbCosecha = CosechaData()
        cosechas = dbCosecha.getCosechas(productorActual)
        if(cosechas != None):
            return cosechas
        else:
            return None

    def idSetter(self):
        a = CosechaData()
        b = a.getLast()
        array = []
        for i in b:
            array.append(i)
        id = array[-1]['id'] + 1
        return id
