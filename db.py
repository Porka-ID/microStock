import pymongo
from cat import *
class Database:
    def __init__(self) -> None:
        self.client = pymongo.MongoClient("mongodb+srv://porkadev:Louann2507@cluster0.k32ytub.mongodb.net/")
        self.db = self.client["DBStock"]
        self.col = self.db["Stock"]

    def getParticularStock(self, name):
        query = {"name": name}
        docs = self.col.find(query)
        try:
            docs = docs[0]
            match docs['type']:
                case "Drink":
                    newObj = Drink()
                    newObj.name = docs['name']
                    newObj.type = docs['type']
                    newObj.infos = docs['infos'] or {}
                    newObj.qty = docs['qty']
                case "Food":
                    newObj = Food()
                    newObj.name = docs['name']
                    newObj.type = docs['type']
                    newObj.infos = docs['infos'] or {}
                    newObj.qty = docs['qty']
        except: 
            docs = False
        return docs 

    def insertStock(self, name, type, infos, qty):
        
        docs = self.getParticularStock(name)
        if docs:
            docs['qty'] = docs['qty'] + int(qty)
            newLine = {"$set": {'qty': docs['qty']} }
            self.col.update_one({'name': docs['name']}, newLine )
        else: 
            newLine = {'name': name, 'type': type, 'qty': qty, 'infos': infos}
            self.col.insert_one(newLine)

    def dropStock(self, name, type):
        docs = self.getParticularStock(name)
        if docs: 
            self.col.delete_one({'name': name, 'type': type})
        else:
            print("Le document n'existe pas")

    def getAllStock(self):
        finded = self.col.find()
        docs = []
        for doc in finded:
            docs.append(doc)
        
        return docs
