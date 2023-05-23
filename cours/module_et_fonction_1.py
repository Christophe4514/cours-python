# https://github.com/DocstringFr/la-formation-complete-python/tree/master/chp-003_quelques-modules-et-fonctions
# random pour generer des nombres alleatoirs et os pour les fichies du système
import random
import os
from pprint import pprint
from typing import Callable

# module random
# 1 la fonction randint() qui permet de recuperer un nombre alleatoire
alea_1 = random.randint(0, 5)
# print(alea_1)

# 2 la fonction uniforme() qui retourne un allea mais décimal contrairement à randint() qui retourne des entiers

alea_2 = random.uniform(0, 2)
# print(alea_2)

# 3 randrange() similaire à randint() sauf qu'elle ne permet de lui donner un seul argument pour afficher des entiers compris entre 0 et le nombre paaser en argument exclut
# on peut aussi lui donner un pas randrnge(0, 101, 10) alea compris entre 0 et 102 exclut avec pas de 10
alea_3 = random.randrange(4)
alea_3 = random.randrange(0, 40, 10)
# print(alea_3)

# exercice

a = random.randint(0, 5)
b = random.randint(0, 4)
if (a > b):
    print("Le nombre {0} est plus grand que le nombre {1}.".format(a, b))
elif (a < b):
    print("Le nombre {0} est plus grand que le nombre {1}.".format(b, a))
else:
    print("Le nombre {} et le nombre {} sont égaux.".format(a, b))

# module os pour creer et supprimer des dossier
chemin = "Users/Enabel62/OneDrive/Documents/python/cours"
dossier = os.path.join(chemin, "dossier", "test")
if not os.path.exists(dossier):
    os.makedirs(dossier)
# os.makedirs(dossier, exist_ok=True) #possibilité si on ne veut pas utiliser le if
# print(dossier)
if os.path.exists(dossier):
    os.removedirs(dossier)
# print(dossier)
# pour creer le dossier on va utiliser la fonction makedirs() qui peut creer plusieurs structures de dossier qui n'existe
# c'est pas le cas pour la fonction mkdir()

# fonction dir() et la fonction help()
# pprint() nous permet d'afficher de façon asser lisibles les elements d'une liste par exemple 
# avec un seul element par ligne et par ordre alphab
pprint(dir(random))
# permet d'affiche toute les fonction du module random
help(random.randint)
# nous affiche l'aide sur une fonction, pas besoin de print pour l'utiliser, 
# pas de parenthese apres randint puisqu'on ne veut pas appeler la fonction

# 
# fonctions collable : appellable
# retourne True ou False si la fonction est collable ou pas
print(callable(os.name))
print(os.name)