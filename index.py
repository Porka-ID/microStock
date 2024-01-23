from cat import *
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
            case 'Drink':
                self.newDrinkItem = Drink()

    def prompt(self):
        self.prompTxt = "Bonjour et bienvenue sur GereTonStockCLI !\nTout d'abord, quelle action souhaites-tu faire ?\n[1] - Ajouter du stock\n[2] - Enlever du stock\n[3] - Afficher la liste d'un stock en particulier\n[4] - Afficher le stock d'un produit\n[5] - Afficher l'entiereté du stock\n"
        self.response = int(input(self.prompTxt)) or 0
        print("__________________________")
        self.treatResponse()

if __name__ == "__main__":
    newApp = Application()
    newApp.prompt()