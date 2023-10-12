fichier_a_lire = input("Entrez un fichier à ouvrir : ")

try:
    f = open(fichier_a_lire, "r")
    print(f.read())
except FileNotFoundError:
    print("Le fichier est introuvable.")
except UnicodeDecodeError:
    print("Impossible d'ouvrir le fichier.")
else:
    f.close()