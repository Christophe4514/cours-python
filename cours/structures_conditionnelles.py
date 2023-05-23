# https://github.com/DocstringFr/la-formation-complete-python/tree/master/chp-002_les-structures-conditionnelles
# source pour les str. cond
# bloc d'instruction
age = 20
langage = "Python"

if age >= 18:
    print("Vous êtes majeur !")
    if langage == "Python":
        print("Vous pouvez rentrer")

print("Le script est terminé")

# stru cond avancées avec else
utilisateur = "root"
if utilisateur == "admin":
    print("Accès autorisé !")
elif utilisateur == "root":
    print("Accès autorisé !")
else:
    print("Accès refusé...")

# plusieur cond
age = 15
if age >= 18:
    print("Vous êtes majeur")
elif age < 18:
    print("Vous êtes mineur")

print((True and False) or True)

# https://www.docstring.fr/glossaire/structure-conditionnelle/