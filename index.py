import pymongo
import cat
from cat import *
PROMPT = """Bonjour et bienvenue sur GereTonStockCLI !
Tout d'abord, quelle action souhaites-tu faire ?
[1] - Ajouter du stock
[2] - Enlever du stock
[3] - Afficher la liste d'un stock en particulier
[4] - Afficher l'entiereté du stock
"""

def fn_drawParticularStock():
    for doc in Drink().getParticularStock():
        print(doc)

def fn_drawStock():
    for doc in connectDB.getAllStock():
        print("Affichage du stock complet\n-----------------")
        print(f"Libéllé de l'article : {doc['name']}")
        print(f"Type de l'article : {doc['type']}")
        print(f"Infos diverses du produit :")
        try:
            for info, value in doc['infos'].items():
                print(f"{info} : {value}")
        except:
            pass
        print("-----------------")

def fn_prompt(pr):
    print(pr)
    response = input("Votre réponse : (1, 2, 3, 4)\n")
    match response:
        case "1":
            pass
        case "2":
            pass
        case "3":
            fn_drawParticularStock()
        case "4":
           fn_drawStock()
if __name__ == "__main__":
    
    fn_prompt(PROMPT)