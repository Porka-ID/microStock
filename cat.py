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
        print(self.name)
        print(self.qty)
        print(self.infos)
        if self.name and self.qty and self.infos:
            print("schéma relationnel")
            self.data.insertStock({"name": self.name, "type": self.type, "qty": self.qty, "infos": self.infos})


class Drink(ObjectStocked):
    def __init__(self, name=None, qty=None, infos={}):
        super().__init__(name, "Drink", qty, infos)

    def __setattr__(self, __name: str, __value: Any):
        super().__setattr__(__name, __value)
        


class Food(ObjectStocked):
    def __init__(self, name=None, qty=None, infos={}):
        super().__init__(name, "Food", qty, infos)

    def __setattr__(self, __name: str, __value: Any):
        super().__setattr__(__name, __value)
        

if __name__ == "__main__":
    newF = Food("Chicken", 1, {"Nutriment": "100ml de "}).addToStock()