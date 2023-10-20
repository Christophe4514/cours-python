# dans quel cas l'utiliser: si on souhaite avoir une librairie qui ne pese pas trop sur le disque : poids faible (1800 ligne de code dont 40% de doc)
# utilisable sur des ordinateurs moins puissants et des rasbery: très simple pour l'utilisation
# c'est 100% python, donc pas besoin de serveur ou dependance externe

# 
# faut pas l'utiliser quand le projet commence à devenir important (grand)
# il ne permet pas non plus de créer des relations entre plusieurs modeles 

# python -m pip install tinydb /pour l'installer

from textwrap import indent
from tinydb import TinyDB, Query, where

# si on veut que apres voir creer le donnée on le sock en mémoir et apres l'utilisation il disparaisse, on peut utiliser:
# from tinydb.storages import MemoryStorage
# db = TinyDB(strorage=MemoryStorage)

db = TinyDB('data.json', indent=4)
# dans insert on passe un dictionnaire
db.insert({"name": "Patrick", "score": 0})

# on peut inserer dess données multiples :
"""db.insert_multiple([
    {"name": "Paul", "score": 3},
    {"name": "Oli", "score": 2000}
])"""

# chercher dans la base de donnée, importer Query et where

User = Query()
patrick = db.search(User.name == "Patrick")
patrick_unique = db.get(User.name == "Patrick")
# print(patrick_unique)

# mettre à jour et supprimer des elements 
db.update({"score": 10}, where('neme') == "Patrick")

# faire une modif sur tous les elements de la db
db.update({"roles": ["Junior"]})
db.update({"roles": ["Experte"]}, where("name") == "Oli")

# inserer ou mettre à jour des onnées si ils existent ou pas
db.upsert({"name": "Pierre", 
           "score":10, 
           "roles": ["Senior"]},
           where('name') =="Pierre"
          )

# supprimer
db.remove(where("score") == 0)
# db.truncate() #supprimer les donner mais garde la db

hight_score = db.search((where("score") > 2) & (where("name")== "Oli"))
print(hight_score)
print(db.count(User.name == "Patrick"))

print(len(db))
print(db.contains(User.name == "Patrick"))
