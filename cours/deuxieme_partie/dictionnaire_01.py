# DICTIONAIRE
dictionnaire = {"nom": "christophe",
                "proffession": "Ingénieur",
                "age": 21,
                "sexe": "M",
                "ville": "Kinshaa"}
print(dictionnaire)

dic = {
    0: {
        "Nom": "Wiz",
        "Profession": "Ingénieur",
        "Ville": "Kinshasa"
    },
    1: {
        "Nom": "Jos",
        "Profession": "Ingénieur",
        "Ville": "Kinshasa"
    },
    2: {
        "Nom": "2pac",
        "Profession": "Ingénieur",
        "Ville": "Kinshasa"
    },
}
# les clé des dic sont uniques

# 
# récupération d'une valeur associée à une clé, return erreur si clé n'est pas tourné
print(dic[0]["Profession"])
print(dic[1])
# ou 
print(dic.get(0)) # ceci return none si la clé n'est pas trouvé, permet aussi d'ajouter un 2eme argument au cas ou la clé n'exite pas
print(dic.get(3, "cet élément n'existe pas encore"))

# 
# exercice
films = {"Le Seigneur des Anneaux": 12,
         "Harry Potter": 9,
         "Blade Runner": 7.5}
 
prix = 0
for key in films:
    prix += films[key]
print(prix)

# modifier valeur d'une clé
# la valeur est mise à jour automatiquement puisque c'est un objet muable
dic[2]["Nom"] = "Quarter Back"
print(dic.get(2, "élément not found"))

# 
# ajout/suppression de clé
# ajout, si la clé existe ceci ne va pas créer une new mais update la val de l'ancienne
dic[3] = {"Nom": "Gloire Mahombi",
        "Profession": "Kiné",
        "Ville": "Kinshasa"}
print(dic.get(3))
del dic[3] # si clé existe pas, erreur
print(dic.get(3, "not found"))
# 
if 3 in dic:
    del dic[3]
    print("delete successfully !")