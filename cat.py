from db import Database
class ObjectStocked(Database):
    def __init__(self, name, qty):
        self.name = name
        self.qty = qty
    
    def getStock(self):
        

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
    