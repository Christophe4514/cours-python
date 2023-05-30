# DICTIONAIRE
# https://www.docstring.fr/glossaire/dictionnaire/

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

# 
# bouclé sur un dic
# keys et values deux possibilités de bouclé sur les dictionnaires
# for cle in dictionnaire:
    # print(cle)
    # print(dictionnaire[cle]) //retourne les value assosié à la cle

# on peut aussi utiliser la methode dictionnaire.items(), ceci retourne un tuple de cle et valeur
# for cle, valeur in dictionaire.items():
    # print(cle, valeur)

# exemple
for cle, valeur in dic.items():
    print(cle, valeur)
    # print(dic.items())
print(dic.keys())
print(dic.values())

employes = {
            "id01": {"prenom": "Paul", "nom": "Dupont", "age": 32},
            "id02": {"prenom": "Julie", "nom": "Dupuit", "age": 25},
            "id03": {"prenom": "Patrick", "nom": "Ferrand", "age": 36}
            }
            
del employes["id03"]
employes["id02"]["age"] = 26
age_paul = employes["id01"]["age"]

# recap
"""
En théorie
d = {
    clé: valeur,
    clé: valeur,
    clé: valeur,
    ...
    clé: valeur
}
"""
# Dictionnaire vide
d = {}
print(d)
# Dictionnaire dont les clés ne sont que des chaînes de caractères
d = {
    'spam': 'eggs',
    'knights': 'lumberjack',
    'bacon': 'sausage'
}
print(d)
# Dictionnaire dont les clés sont des objets de différents types
d = {
    1: 'one',
    'deux': 2,
    (3, 4, 5): 'pas_de_soucis',
    9.9: 'nine_point_nine'
}
print(d)
"""Les dictionnaires que je viens de créer n'ont aucun sens, je voulais juste te montrer ce qu'il était possible de faire.
Vous pouvez aussi créer un dictionnaire grâce la fonction dict:"""
d = dict()  # {}
d = dict({
    'spam': 'eggs',
    'knights': 'lumberjack',
    'bacon': 'sausage'
})
print(d)
"""Une clé doit être unique, les doublons ne sont pas autorisés.
Si cela arrive, cela ne va pas créer d'erreur mais votre seconde clé écrasera la première."""
d = {
    'spam': 'eggs',
    'knights': 'lumberjack',  # 1ère clé 'knights'
    'bacon': 'sausage',
    'knights': 'ham'  # 2ème clé 'knights' qui va écraser la première
}
print(d)
# Une clé ne peut pas être un objet muable :
d = {
    ['spam']: 'eggs'  # TypeError: unhashable type: 'list'
}

d = {
    'spam': 'eggs',
    'knights': 'lumberjack',
    'bacon': 'sausage'    
}
d['spam']  # 'eggs'
# Si on essaie d'accéder à une clé inexistante avec les crochets, on a une erreur (KeyError)
# print(d['ham'])
d.get('spam')  # 'eggs'
# Avec get, si la clé n'existe pas, on récupère None
d.get('ham')  # None
# Ou la valeur par défaut que l'on passe en deuxième argument
d.get('ham', "Cette clé n'existe pas...")  # "Cette clé n'existe pas..."

d = {
    'spam': 'eggs',
    'knights': 'lumberjack',   
}
d['spam'] = 'ham' # Clé existe déjà, remplace la valeur
d['bacon'] = 'sausage' # Nouvelle clé, on créer la paire clé/valeur dans le dico

d = {
    'spam': 'ham',
    'knights': 'lumberjack',
    'bacon': 'sausage'
}
item = d.pop('knights') # 'lumberjack'

d = {
    'spam': 'ham',
    'knights': 'lumberjack',
    'bacon': 'sausage'
}
item = d.popitem() # ('bacon', 'sausage') OU ('spam', 'ham') OU ('knights': 'lumberjack')

d = {
    'spam': 'ham',
    'knights': 'lumberjack',
    'bacon': 'sausage'
}
d.clear() # {}

d = {
    'spam': 'ham',
    'knights': 'lumberjack',
    'bacon': 'sausage'
}
del d
print(d) # NameError: name 'd' is not defined


from collections import defaultdict
programming_languages = defaultdict(lambda: 'Python')
programming_languages['.js'] = 'JavaScript'
programming_languages['.php'] = 'PHP'
print(programming_languages['.js'])   # 'Javascript'
print(programming_languages['.php'])  # 'PHP'
print(programming_languages['.py'])   # 'Python' => Valeur par défaut


d = {
    'spam': 'ham',
    'knights': 'lumberjack',
    'bacon': 'sausage'
}
for key in d:
    print(key)


d = {
    'spam': 'ham',
    'knights': 'lumberjack',
    'bacon': 'sausage'
}
for key in d:
    print(key, d[key])


d = {
    'spam': 'ham',
    'knights': 'lumberjack',
    'bacon': 'sausage'
}
for key in d.keys():
    print(key)
keys = d.keys()
print(keys)


d = {
    'spam': 'ham',
    'knights': 'lumberjack',
    'bacon': 'sausage'
}
for value in d.values():
    print(value)


d = {
    'spam': 'ham',
    'knights': 'lumberjack',
    'bacon': 'sausage'
}
for key, value in d.items():
    print(key, value)


d = {
    'spam': 'ham',
    'knights': 'lumberjack',
    'bacon': 'sausage'
}
print('bacon' in d)  # True
print('ham' in d)    # False