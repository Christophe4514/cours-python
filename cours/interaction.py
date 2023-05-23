# la fonction input pour interagir avec les utilisateurs
live = input("entrez votre nom : \n")
if (len(live) > 0):
    print("votre nom est : {}".format(live))
else:
    print("veiller introduire un vrai nom espece de p'tit malin")

nom = input("veiller inserer votre nom : ")
ville_de_naissance = input("entrez votre ville de naissance : ")
age = input("entrer votre age : ")
age = int(age)
print(nom + '\n' + ville_de_naissance)
print(age)
