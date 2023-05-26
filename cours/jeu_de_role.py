import random
# exercice d'application 03

sante_ennemi = 50
sante_joueur = 50
nombre_de_position = 3
saut_de_tour = False

while True:
    # Jeu du joueur
    if saut_de_tour:
        print("Vous passez votre tour...")
        saut_de_tour = False
    else:
        choix_utilisateur = ""
        while choix_utilisateur not in ["1", "2"]:
            choix_utilisateur = input("Souhaitez-vous attaquer (1) ou utiliser une potion (2) ? ")

        if choix_utilisateur == "1":  # Attaque
            attaque = random.randint(5, 10)
            sante_ennemi -= attaque
            print(f"Vous avez infligé {attaque} points de dégats à l'ennemi ⚔️")
        elif choix_utilisateur == "2" and nombre_de_position > 0:  # Potion
            sante_position = random.randint(15, 50)
            sante_joueur += sante_position
            nombre_de_position -= 1
            saut_de_tour = True
            print(f"Vous récupérez {sante_position} points de vie ❤️ ({nombre_de_position} ? restantes)")
        else:
            print("Vous n'avez plus de potions...")
            continue

    
    if sante_ennemi <= 0:
        print("Tu as gagné ?")
        break

    # Attaque de l'ennemi
    enemy_attack = random.randint(5, 15)
    sante_joueur -= enemy_attack
    print(f"L'ennemi vous a infligé {enemy_attack} points de dégats ⚔️")

    if sante_joueur <= 0:
        print("Tu as perdu ?")
        break

    # Stats
    print(f"Il vous reste {sante_joueur} points de vie.")
    print(f"Il reste {sante_ennemi} points de vie à l'ennemi.")
    print("-" * 50)

print("Fin du jeu.")