import time
# boucle for // permet de parcourir principalement les structures d'une données
# https://www.docstring.fr/glossaire/for/?utm_source=udemy&utm_campaign=for-loop-glossary
# synthaxe : 
# for element in liste:
#     print(element)

elements = [1, 2, 4, 5, "Toto", True, "Fixe"]
for element in elements:
    print(f"{element}")
# for i in [21, 23, "Huile de palme", "maracuja", "fire"]:
    # print(f"{i}")
# for j in range(100):
#     print("sale malde, apprend à respecter les gens ")
for i in range(3):
    print(i)

fruits = ['🍊', '🍋', '🍏', '🍒', '🥭']

for fruit in fruits:
    print(fruit)
else:
    print('Plus de fruits dans le panier')

prenom = "John"
for lettre in prenom:
    print(lettre)

for (pk, name) in [(1, "Patrick"), (2, "John"), (3, "Marie")]:
    print(pk, name)

# exercice
print(list(range(10)))
liste = []
while liste == True:
    print("Itération sur la liste")
# 

# boucle while
# while condition:
#     print()
# https://www.docstring.fr/glossaire/while/?utm_source=udemy&utm_campaign=while-loop-glossary
i = 0
while i < 10:
    print('Salut')
    i += 1

i = 0
while i < 3:
    print('Salut')
    i += 1
else:
    print('Au revoir')

continuer = "o"
while continuer == "o":
    mdp = input("entrer mdp : ")
    user_name = input("entrer user name : ")
    if mdp == "123456" and user_name == "Admin":
        print("vous etes connecté")
        continuer = "n"
    else:
        print("mdp et user name incorrect ...")
        continuer = input("reessayer o/n : ")

while True:
    print("Téléchargement de vidéo en cours")
    time.sleep(4)

# continue 
# https://www.docstring.fr/glossaire/continue/?utm_source=udemy&utm_campaign=continue-glossary

for fruit in fruits:
    if fruit == '🍒':
        print('Pas fan des cerises')
        continue

    print(fruit)

print('On passe à la suite')  

# break
# https://www.docstring.fr/glossaire/break/?utm_source=udemy&utm_campaign=break-glossary

fruits = ['🍊', '🍋', '🍏', '🍒', '🥭']
fruits_manges = 0

for fruit in fruits:
    print("Je mange des " + fruit)
    fruits_manges += 1
    if fruits_manges == 3:
        break

print("Je n'ai plus faim !")

i = 0
while True:
    print(i)
    i += 1
    if i == 10:
        continue