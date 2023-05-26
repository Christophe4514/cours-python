# une methode est une fonction qui appartient à un objet
# sorted(liste) //fonction
# liste.sort() //methode de l'object list
liste = [1, 7, 3, 4, 5, 10, 2]
rev = sorted(liste) # ecrase la liste de départ
liste.sort() #fait la mm chose sans avoir à ecraser la liste de départ
titre = "la maison est tombée"
titre = titre.title()
print(titre)
# len(), range(), sum(), max(), min()
mdp = input("Entrez un mot de passe (min 8 caractères) :")
mdp_trop_court = "VOTRE MOT DE PASSE EST TROP COURT"
mdp_moyen = "Votre mot de passe est trop court"
if len(mdp) == 0:
    print(mdp_trop_court)
elif len(mdp) <= 8:
    print(mdp_moyen)
elif mdp.isdigit():
    print("Votre mot de passe ne contient que des nombres.")
else:
    print("Inscription terminée.")