import pymongo
class Database:
    def __init__(self) -> None:
        self.client = pymongo.MongoClient("mongodb+srv://porkadev:Louann2507@cluster0.k32ytub.mongodb.net/")
        self.db = self.client["DBStock"]
        self.col = self.db["Stock"]

    def getParticularStock(self, name, type):
        query = {"name": name, "type": type}
        docs = self.col.find(query)
        try:
            docs = docs[0]
        except: 
            docs = False
        return docs 

    def insertStock(self, name, type, qty):
        
        docs = self.getParticularStock(name, type)
        if docs:
            docs['qty'] = docs['qty'] + int(qty)
            newLine = {"$set": {'qty': docs['qty']} }
            self.col.update_one({'name': docs['name']}, newLine )
        else: 
            newLine = {'name': name, 'type': type, 'qty': qty}
            self.col.insert_one(newLine)

    def dropStock(self, name, type):
        docs = self.getParticularStock(name, type)
        if docs: 
            self.col.delete_one({'name': name, 'type': type})
        else:
            print("Le document n'existe pas")