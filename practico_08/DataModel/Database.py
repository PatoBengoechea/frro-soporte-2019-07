from pymongo import MongoClient
from pymongo.errors import ConnectionFailure



class Database:

    def main(self):
        try:
            client = MongoClient("mongodb://admin:admin@cluster0-shard-00-00-geyoz.mongodb.net:27017,cluster0-shard-00-01-geyoz.mongodb.net:27017,cluster0-shard-00-02-geyoz.mongodb.net:27017/test?ssl=true&replicaSet=Cluster0-shard-0&authSource=admin&retryWrites=true&w=majority")

            #print("Connected Succesfully")
        except ConnectionFailure:
            print(ConnectionFailure)


        db = client['Finance']

        return db





