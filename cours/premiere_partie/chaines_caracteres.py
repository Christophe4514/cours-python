# modification de la casse
# 4 methodes : upper, lower, tittle and capitalise
# 1. upper() and lower()
hello = "Bonjour"
hello = hello.upper()
# print(hello)
# print(hello.lower())

# cas de figure : upper plus pour afficher du text sur une page web et lower pour des expressions de recherche

# capitalise() : permet de mettre du majuscule au debut d'un mot ou d'une phrase
# title() met en majuscule la premiere lettre de chaque mot dans une phrase
nom = "malewa eza quelque chose ".capitalize()
nom = "malewa eza quelque chose ".title()
# print(nom)


#
# Remplacer des elements : replace()
nom = "bonjour".replace('jour', 'soir')
# print(nom)

nom = "bonjour tout le monde ".replace(" ", "")
# print(nom)

nom = "bonjour tout le monde ".replace("monde", "vonde")
# print(nom)

nom = "bonjour tout le monde ".replace(" ", "").replace("monde", "viande").replace(
    "jour", "soir").replace("toutle", " tous les ").replace("", " ")
# print(nom)
# strip(): par defaut si on ne lui passe rien, il enleve tous les espaces du début et de la fin de la chaine
# supprime les les lettres specifié en allant de gauche et de droite et en s'arretant lorsqu'il trouve un caractere non specifié 
wiz = " yeyo ".strip()
wiz = " ye  yo ".strip()
wiz = "  bonjour  ".strip(" ujor")
# on peut utiliser rstrip() ou lstrip() pour dire de quel coté on veut enlevé les caractéres
wiz = "  bonjour  ".rstrip(" ujor")
# sortie : " bon"
wiz = "  bonjour  ".lstrip(" ujor")
# sortie : "bonjour  "
# print(wiz)


# 
# Séparé et joinder avec split() et join
numb = "1, 2, 3, 4, 5".split(", ")
numb = ", ".join("1, 2, 3, 4, 5".split(", "))
numb = ".".join("1, 2, 3, 4, 5".split(", "))
date = "/".join(['12', '10', '2023'])
# date = "/".join([12, 10, 2023]) # donne une erreur, on utilise pas la methode join sur une liste mais sur des chaines
# print(date)

# 
# Remplir de zero avec zfill(), permet de remplacer avec des zero une chaine par des zero pour avoir une chaine de longueur fix
# zfill() ne marche que sur des chaines de caractère et non sur des nombre.
nombre = "555".zfill(4)
nombre = "25".zfill(4)
# print(nombre)
# for i in range(100):
#     print(i)

# for i in range(1000):
#     print(str(i).zfill(7))

# 
# methodes is...()
# 1 islower()
numb = "jsquare".islower()
numb = "Jsquare".islower()
numb = "Jsquare".isupper()
numb = "Jsquare".isalnum()
numb = "Jsquare".isascii()
numb = "234".isdigit()
# print(numb)

# 
# compter les occurrences
nom = "bonjour tout le monde".count("jour")
nom = "bonjour tout le monde".count("n")
# print(nom)

# trouver une chaine find() et index
# si la chaine n'est pas trouver find() retourne -1 mais index retourne une erreur
nom = "bonjour tout le monde".find("jour")
# nom = "bonjour tout le monde".index("vande")
# sortie erreur
nom = "bonjour tout le monde".find("jande") #-1
# print(nom)
nom = "bonjour le monde".rfind("monde") #lfind() n'existe pas
# print(nom)

# 
# chercher au debut et à la fin avec endswith() et startswith()
image = "monImage.pgn".endswith(".png")
image = "monImage.pgn".startswith("mon")
# print(image)

# exercices
lorem = """Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua.
		   Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat.
		   Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur.
		   Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum."""
lorem = lorem.count(".")
print(lorem)

chaine = "Pierre, Julien, Anne, Marie, Lucien"
 
chaine_liste = chaine.split(", ")
chaine_liste.sort()
chaine_en_ordre = ", ".join(chaine_liste)