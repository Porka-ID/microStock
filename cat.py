from typing import Any
from db import *
class ObjectStocked:
    def __init__(self, name, type, qty, infos):
        self.data = DatabaseItem()
        self.name = name
        self.type = type
        self.qty = qty
        self.infos = infos

    def addToStock(self):
        if self.name and self.qty and self.infos:
            self.data.insertStock({"name": self.name, "type": self.type, "qty": self.qty, "infos": self.infos})


class Drink(ObjectStocked):
    def __init__(self, name, qty, infos):
        super().__init__(name, "Drink", qty, infos)

    def 

        


class Food(ObjectStocked):
    def __init__(self, name, qty, infos):
        super().__init__(name, "Food", qty, infos)
        

if __name__ == "__main__":
    newF = Food("Chicken", 1, {"Nutriment": "100ml de "}).addToStock()