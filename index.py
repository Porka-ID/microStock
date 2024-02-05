from cat import *
from db import * 
class Application:
    def __init__(self):
        self.types = "('Drink';'Food')"

    def treatResponse(self):
        match self.response:
            case 1:
                self.addStock()
            case 2: 
                print("Suppression de stock")
            case 3: 
                print("Afficher la liste d'un type de stock")
            case 4: 
                print("Afficher le stock d'un produit")
            case 5:
                print("Afficher l'entiereté d'un stock")

    def addStock(self):
        self.choiceType = input(f"Type du produit {self.types} : " )
        match self.choiceType:
            case 'Food':
                self.newFoodItem = Food()
                self.newFoodItem.name = input("Nom du produit : ")
                self.alreadyExist = self.newFoodItem.data.getItemStock(self.newFoodItem.name)
                print(self.alreadyExist)
                if self.alreadyExist:
                    print("Produit déja existant")
                    self.choiceUpdate = input("Voulez-vous modifier l'élément ? (y/n) : ")
                    match self.choiceUpdate:
                        case 'y':
                            self.newFoodItem.qty = int(input("Entrer la quanité à ajouter :"))
                            self.newFoodItem.infos = self.alreadyExist['infos']
                            self.enterInfos = True
                            self.newFoodItem.addToStock()
                            print(self.newFoodItem)
                            """
                            self.wantModifyInfos = input("Tu veux changer les infos ? (y/n)")
                            if self.wantModifyInfos == "n":
                                self.enterInfos = False
                            self.infos = {}
                            while self.enterInfos:
                                self.wantToStop = input("C'est tout ? (y/n) : ")
                                self.keyTable = input("Clé de l'infos : ")
                                self.infos = input("Infos lié : ")
                                self.infos[self.keyTable] = self.infos
                                if self.wantToStop == "y":
                                    self.enterInfos = False
                            
                            """
                            
                        case _:
                            print("no !")
                    
            case 'Drink':
                self.newDrinkItem = Drink()
                self.newDrinkItem.name = input("Nom du produit : ")
                self.alreadyExist = self.newDrinkItem.data.getItemStock(self.newDrinkItem.name)
                print(self.alreadyExist)
                if self.alreadyExist:
                    print("Produit déja existant")
                    self.choiceUpdate = input("Voulez-vous modifier l'élément ? (y/n) : ")
                    match self.choiceUpdate:
                        case 'y':
                            self.newDrinkItem.qty = int(input("Entrer la quanité à ajouter :"))
                            try:
                                self.newDrinkItem.infos = self.alreadyExist['infos']
                            except:
                                self.newDrinkItem.infos = {}
                            self.enterInfos = True
                            self.newDrinkItem.addToStock()
                            print(self.newDrinkItem)
                            """
                            self.wantModifyInfos = input("Tu veux changer les infos ? (y/n)")
                            if self.wantModifyInfos == "n":
                                self.enterInfos = False
                            self.infos = {}
                            while self.enterInfos:
                                self.wantToStop = input("C'est tout ? (y/n) : ")
                                self.keyTable = input("Clé de l'infos : ")
                                self.infos = input("Infos lié : ")
                                self.infos[self.keyTable] = self.infos
                                if self.wantToStop == "y":
                                    self.enterInfos = False
                            
                            """
                            
                        case _:
                            print("no !")

    

    def prompt(self):
        self.prompTxt = "Bonjour et bienvenue sur GereTonStockCLI !\nTout d'abord, quelle action souhaites-tu faire ?\n[1] - Ajouter du stock\n[2] - Enlever du stock\n[3] - Afficher la liste d'un stock en particulier\n[4] - Afficher le stock d'un produit\n[5] - Afficher l'entiereté du stock\n"
        self.response = int(input(self.prompTxt)) or 0
        print("__________________________")
        self.treatResponse()

if __name__ == "__main__":
    newApp = Application()
    newApp.prompt()