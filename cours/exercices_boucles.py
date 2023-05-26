# 1 afficher 10 utilisateurs
for i in range(10):
    print(f"Utilisateur {i + 1}")

#2 afficher les lettre à l'interirur d'un lmot à l'inverse
mot = "christophe"
for lettre in reversed(mot):
    print(lettre)
mot = "Python"
for lettre in mot[::-1]:
    print(lettre)

# mot = "Python"

# for i in list(reversed(mot)) :
#    print (i)
# 3
# Le but de cet exercice est de modifier le script afin d'afficher l'index de chaque lettre du mot 'Python'.
mot = "Python"

for i in range(len(mot)):
    print(i)
# table de multiplication
nombre = 7
for i in range(11):
    print(f"{i} * {nombre} = {i * nombre} ")

# sortir d'une boucle infinie
i = 0

while i < 10:
    i+=1
    # pass c pass l'erreur

resultat = "Exercice réussi !"
print(resultat)

# sortir de la boucle avec le input
# Solution 1
continuer = "o"
while continuer == "o":
    print("On continue !")
    continuer = input("Voulez-vous continuer ? o/n ")

# Solution 2
continuer = "o"
while continuer == "o":
    print("On continue !")
    resultat = input("Voulez-vous continuer ? o/n ")
    if resultat != "o":
        break

# Solution 3 avec Python 3.8 uniquement
while (continuer := "o") == "o":
    print("On continue !")
    if (resultat := input("Voulez-vous continuer ? o/n ")) != "o":
        break

# comprehension de la liste
nombres = [1, 21, 5, 44, 4, 9, 5, 83, 29, 31, 25, 38]
nombres_pairs = [i for i in nombres if i % 2 == 0]
nombres_croissant = sorted(nombres)
print(nombres_pairs)
print(nombres_croissant)

# ---------------------------------------------------- #

nombres = range(-10, 10)
nombres_positifs = [i for i in nombres if i >= 0]
print(nombres_positifs)

# ---------------------------------------------------- #

nombres = range(5)
nombres_doubles = [i * 2 for i in nombres]
print(nombres_doubles)

# ---------------------------------------------------- #

nombres = range(10)
nombres_inverses = [i if i % 2 == 0 else -i for i in nombres]
print(nombres_inverses)

# 
nombres = range(51)
nombres_pairs = [i for i in nombres if i % 2 == 0]
print(nombres_pairs)
# ou 
for i in nombres:
    if i % 2 == 0:
        nombres_pairs.append(i)

# 
# liste de projet à réaliser pour son portfolio
# https://www.docstring.fr/blog/10-idees-de-projets-a-realiser-avec-django/