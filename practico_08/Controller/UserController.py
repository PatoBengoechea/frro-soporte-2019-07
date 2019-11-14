from DataModel.UserData import  UserData


class UserController:

    def createUser(self, name, surname, user, password, wallet):
        dbuser = UserData()
        message = dbuser.createUser(name, surname, user, password, wallet)
        return message


    def validateUser(self, user, password):
        dbUser = UserData()
        logUser = dbUser.getUser(user, password)
        return logUser


