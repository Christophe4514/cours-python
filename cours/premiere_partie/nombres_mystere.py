import random
from random import randint
# exercice d'applicatio 02

nombre_a_chercher = randint(0, 100)
tentatives_restantes = 5

print("*** Le jeu du nombre mystère ***")

# La boucle principale
while tentatives_restantes > 0:
    print(f"Il te reste {tentatives_restantes} essai{'s' if tentatives_restantes > 1 else ''}")

    # Récupération du Saisie de l'utilisateur
    choix_utilisateur = input("Devine le nombre : ")
    if not choix_utilisateur.isdigit():
        print("Veuillez entrer un nombre valide.")
        continue
    
    choix_utilisateur = int(choix_utilisateur)    

    if nombre_a_chercher > choix_utilisateur:  # Plus grand
        print(f"Le nombre mystère est plus grand que {choix_utilisateur}")
    elif nombre_a_chercher < choix_utilisateur:  # Plus petit
        print(f"Le nombre mystère est plus petit que {choix_utilisateur}")
    else:  # Égal (succès)
        break

    tentatives_restantes -= 1

# Décision
if tentatives_restantes == 0:
    print(f"Dommage ! Le nombre mystère était {nombre_a_chercher}, vous avez perdu")
else:
    print(f"Bravo ! Le nombre mystère était bien {nombre_a_chercher} !")
    print(f"Tu as trouvé le nombre en {6 - tentatives_restantes} essai")

print("Fin du jeu '_' .")