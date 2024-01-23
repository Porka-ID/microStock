import mdp 
import pymongo as pm 
class Database:
    def __init__(self):
        self.client = pm.MongoClient(mdp.password)
        self.db = self.client["DBStock"]

class DatabaseItem(Database): 
    def __init__(self):
        super().__init__()
        self.col = self.db["Stock"]
    
    def getItemStock(self, itemName):
        self.query = {"name": itemName}
        self.docs = self.col.find(self.query)
        try:
            self.docs = self.docs[0]
            print(self.docs)
        except Exception as e:
            print(e)


    def insertStock(self, tbl):
        pass

if __name__ ==  "__main__":
    newDB = DatabaseItem()
    newDB.getItemStock("Ice-Tea")