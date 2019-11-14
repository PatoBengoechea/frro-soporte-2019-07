from DataModel.Database import Database
from Model.User import User

class UserData:

    def createUser(self, name, surname, user, password, wallet):
        db = Database()
        cursor = db.main()
        newUser = {
            'name': name,
            'surname': surname,
            'user': user,
            'password': password,
            'wallet': wallet
        }
        try:
            cursor.usuario.insert_one(newUser)
            return True
        except:
            return False




    def getUser(self, user, password):

        #Hacer try catch, que pasa si no encuentra un usuario?
        db = Database()
        cursor = db.main()
        logUserJSON = cursor.usuario.find_one({"user": user, "password": password})
        if logUserJSON != None:
            logUserModel = User()
            logUserModel.parse(logUserJSON)
            return logUserModel
        else:
            return None
