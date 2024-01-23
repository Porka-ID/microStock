from db import Database
class ObjectStocked(Database):
    def __init__(self, name, qty):
        super().__init__()
        self.name = name
        self.qty = qty
        self.type = None

    def getParticularStock(self):
        query = {"name": self.type}
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
            docs = {}
        finally:
            return docs 


class Drink(ObjectStocked):
    def __init__(self):
        self.type = 'Drink'

    def setInfos(self, infos):
        self.infos = infos

    


class Food(ObjectStocked):
    def __init__(self):
        self.type = 'Food'

    def setInfos(self, infos):
        self.infos = infos
    