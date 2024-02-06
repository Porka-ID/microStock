from cat import *
from db import * 
import time
class Application:
    def __init__(self):
        self.types = "('Drink';'Food')"
        self.db = DatabaseItem()

    def treatResponse(self):
        match self.response:
            case 1:
                self.addStock()
            case 2: 
                self.suppressStock()
            case 3: 
                print("Afficher la liste d'un type de stock")
            case 4: 
                print("Afficher le stock d'un produit")
            case 5:
                self.getStock()

    def waitToRestart(self):
        self.wantToRestart = True
        while self.wantToRestart:
            restart = input("Voulez-vous revenir au menu principal ? (y/n) :")
            match restart:
                case "y":
                    self.prompt()
                case _:
                    self.wantToRestart = False

    def getStock(self):
        self.getStocks = self.db.getAll()
        if self.getStocks:
            print("Voici la liste des élements dans votre stock :")
            for doc in self.getStocks:
                print("___________")
                print(f"Nom du produit : {doc['name']}")
                print(f"Type du produit : {doc['type']}")
                print(f"Quantité du produit : {doc['qty']}")
                print(f"Infos du produit :{doc['infos']}")
            print("___________")
        else:
            print("Il n'y a pas de stock")
        self.waitToRestart()

    def addRealStock(self, object):
        object.name = input("Nom du produit : ")
        self.alreadyExist = object.data.getItemStock(object.name)
        if self.alreadyExist:
            print("Produit déja existant")
            self.choiceUpdate = input("Voulez-vous ajouter/retirer une quantité ? (y/n) : ")
            match self.choiceUpdate:
                case 'y':
                    object.qty = int(input("Entrer la quantité à ajouter :"))
                    object.infos = self.alreadyExist['infos']
                    self.enterInfos = True
                    object.addToStock()
                    print(object)
                    
                case _:
                    print("no !")
        else:
            object.qty = int(input("Entrer la quantité déja présente dans le stock : "))
            object.infos = {}
            self.enterInfos = True
            while self.enterInfos:
                self.wantToStop = input("Rajouter une nouvelle infos ? (y/n) : ")
                if self.wantToStop == "n":
                    self.enterInfos = False
                    break
                self.keyTable = input("Clé de l'infos : ")
                self.info = input("Infos lié : ")
                object.infos[self.keyTable] = self.info
                
            object.addToStock()
        self.waitToRestart()

    def addStock(self):
        self.choiceType = input(f"Type du produit {self.types} : " )
        match self.choiceType:
            case 'Food':
                self.newFoodItem = Food()
                self.addRealStock(self.newFoodItem)
            case 'Drink':
                self.newDrinkItem = Drink()
                self.addRealStock(self.newDrinkItem)

    def suppressStock(self):
        result = True
        while result:
            self.choiceName = input("Nom du produit à supprimer : ")
            if self.db.getItemStock(self.choiceName):
                self.sureSuppress = input(f"Etes-vous sur de vouloir supprimer {self.choiceName} (y/n) : ")
                match self.sureSuppress:
                    case "y":
                        resultQuery = self.db.deleteStock({"name": self.choiceName})
                        if resultQuery:
                            result = False
                    case _:
                        self.wantToQuit = input("Voulez-vous ne pas supprimer d'element ? (y/n) : ")
                        match self.wantToQuit:
                            case "y":
                                result = False
            else:
                print("Vous essayez de supprimer quelque chose qui n'existe pas")
                self.wantToQuit = input("Voulez-vous ne pas supprimer d'element ? (y/n) : ")
                match self.wantToQuit:
                    case "y":
                        result = False
            
            self.waitToRestart()
            


    def prompt(self):
        self.prompTxt = "Bonjour et bienvenue sur GereTonStockCLI !\nTout d'abord, quelle action souhaites-tu faire ?\n[1] - Ajouter du stock\n[2] - Enlever du stock\n[3] - Afficher la liste d'un stock en particulier\n[4] - Afficher le stock d'un produit\n[5] - Afficher l'entiereté du stock\n"
        self.response = int(input(self.prompTxt)) or 0
        print("__________________________")
        self.treatResponse()

if __name__ == "__main__":
    newApp = Application()
    newApp.prompt()