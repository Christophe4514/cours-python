from pprint import pprint
# https://github.com/DocstringFr/la-formation-complete-python/tree/master/chp-004_les-listes
# Les tuples, c'est quasiment la même chose que les listes. La différence principale, c'est qu'on ne peut ni ajouter ni enlever d'éléments à un tuple.
# defir un tuple
mon_tuple = (1, 2, 3)
mon_tuple = (250, "Python", True)
# il est possible de convertir un tuple en liste et vice-versa grâce aux fonctions list et tuple
mon_tuple = (1, 2, 3)
liste = list(mon_tuple)
mon_tuple = tuple(liste)
# https://www.docstring.fr/glossaire/tuple/

# listes : ajout et suppression
# ajout : liste.append() pour ajouter un seul element à la fois et liste.extend() pour ajouter plusieurs elements
liste = []
liste.append("gracia")
liste.extend(["paco", "christian"])
# pprint(liste)
# suppression : liste.remove() la methode ne supprime que la première occurence dans la liste
liste.remove("paco")
# print(liste)
# recherche : a partir des indices 
liste = [1, 2, [3, "Python", 4], 5, 6]
# print(liste[2][1])

# exercice
# Récupérez le premier et le dernier nombre contenus dans cette liste dans les variables 'nombre_premier' et 'nombre_dernier'.
nombres = [1, 2, 3, 4, 5, 4, 3, 2, 1]
nombre_premier = nombres[0]
nombre_dernier = nombres[-1]
 
# Récupérer l'élément 'Python' contenu dans la liste dans la variable 'langage'.
langages = ["Java", "Python", "C++"]
langage = langages[1]
 
# Changez la position de l'élément 'Python' dans la liste pour qu'il se retrouve à la fin de la liste (["Java", "C++", "Python"])
liste = ["Java", "Python", "C++"]
liste.remove("Python")
liste.append("Python")

# slices = tranches
users = ["util_1", "util_2", "util_3", "util_4"]
#print(users[2:3]) #borne sup exclu [:] on recupere la liste entiere
# print(users[:])
# users[::2] prendre les elements de liste avec le pas, 1/2 util
# print(users[::2])
#print(users[::-1]) #inverse l'ordre de la liste

# exercice
liste = ["Maxime", "Martine", "Christopher", "Carlos", "Michael", "Eric"]
trois_premiers = liste[:3]
# print(trois_premiers)
trois_derniers = liste[3:]
# print(trois_derniers)
milieu = liste[1:5]
# print(milieu)
premier_dernier = liste[::len(liste)-1]
# print(premier_dernier)

# autre methode
employes = ["Maxime", "Martine", "Christopher", "Carlos", "Michael", "Eric"]
marte = employes.index("Martine") 
marte = employes.count("Martine")
employes.sort() #trie la liste 
employes_trier = sorted(employes) #trie la liste et la retourne dans la liste trier
# print(employes)
employes.reverse() #renverse la liste 
# print(employes_trier)
print(employes)