import sys
# exerice d'application 01
# https://github.com/DocstringFr/la-formation-complete-python/tree/master/prj-003_la-liste-de-courses/02-solution

# sys.exit()
# liste_de_courses = []
# print("Choisisser parmis les 5 options suivantes : ")
# print("1. Ajouter un élément")
# print("2. Retirer un élément")
# print("3. Afficher la liste")
# print("4. Vider la liste")
# print("5. Quitter")
# option = input()
# while True:
    # if option == 1:
    #     element = input("inserer l'élément à ajouter : ")
    #     liste_de_courses.append(element)
    #     print(f"l'élément {element} à bien été ajouter à la liste")
    # elif option == 2:
    #     element = input("inserer l'élément à ajouter : ")
    #     liste_de_courses.remove(element)
    #     print(f"l'élément {element} à bien été rétiré à la liste")
    # elif option == 3:
    #     for i in range(liste_de_courses):
    #         if len(liste_de_courses) == 0:
    #             print("la liste est vide")
    #             print(f"les éléments de la liste son {i}")
    # elif option == 4:
    #     liste_de_courses.clear()
    #     print("la liste à été vidé avec succès")
    # elif option == 5:
    #     print("fin de programme")
    #     sys.exit()

# import sys
liste = []
menu = """Choisissez parmi les 5 options suivantes :
1: Ajouter un élément à la liste
2: Retirer un élément de la liste
3: Afficher la liste
4: Vider la liste
5: Quitter
? Votre choix : """
menu_choix = ["1", "2", "3", "4", "5"]
while True:
    user_choice = input(menu)
    if user_choice not in menu_choix:
        print("Veuillez choisir une option valide...")
        continue
    if user_choice == "1":  # Ajouter un élément
        item = input("Entrez le nom d'un élément à ajouter à la liste de courses : ")
        liste.append(item)
        print(f"L'élément {item} a bien été ajouté à la liste.")
    elif user_choice == "2":  # Retirer un élément
        item = input("Entrez le nom d'un élément à retirer de la liste de courses : ")
        if item in liste:
            liste.remove(item)
            print(f"L'élément {item} a bien été supprimé de la liste.")
        else:
            print(f"L'élément {item} n'est pas dans la liste.")
    elif user_choice == "3":  # Afficher la liste
        if liste:
            print("Voici le contenu de votre liste :")
            for i, item in enumerate(liste, 1):
                print(f"{i}. {item}")
        else:
            print("Votre liste ne contient aucun élément.")
    elif user_choice == "4":  # Vider la liste
        liste.clear()
        print("La liste a été vidée de son contenu.")
    elif user_choice == "5":  # Quitter
        print("À bientôt !")
        sys.exit()

    print("-" * 50)