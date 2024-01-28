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
               
        except:
            self.docs = None
        

    def updateStock(self, tbl):
        tbl["qty"] = self.docs["qty"] + tbl["qty"]
        self.docs = tbl
        try:
            self.newLine = {"$set": self.docs}
            self.col.update_one({"name": tbl["name"]}, self.newLine )
            self.getItemStock(tbl["name"])
            print(tbl)
            if int(self.docs["qty"]) < 0:
                print("Vous tentez de supprimer du stock qui n'existe pas !")
            self.docs = None
            return
            
        except Exception as e:
            print(e)   
            
    def deleteStock(self, tbl):
        if tbl:
            self.col.delete_one({"name": tbl["name"]})


    def insertStock(self, tbl):
        if tbl and tbl["name"]:
            self.getItemStock(tbl["name"])
            if not self.docs:
                try:
                    self.col.insert_one(tbl)
                except Exception as e:
                    print(e)
            else:
                self.updateStock(tbl)
                
    
    def removeStock(self, tbl):
        tbl["qty"] = -tbl["qty"]
        self.insertStock(tbl)


if __name__ ==  "__main__":
    pass