class User:
    name = ""
    surname = ""
    user = ""
    password = ""
    wallet = ""

    def parse(self,data):
        self.user = data["user"]
        self.password = data["password"]
        self.name = data["name"]
        self.surname = data["surname"]
