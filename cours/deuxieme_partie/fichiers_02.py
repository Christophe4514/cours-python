# lire le contenu d'un fichier
chemin = r"C:\Users\Enabel62\OneDrive\Documents\python\cours-python\cours\deuxieme_partie\fichier.txt"

f = open(chemin, "r") #ovrir le fichier en mode read (lecture) avec l'attribut r
# print(f)
f.close() #il est toujours important de fermé un fichier après l'avoir ouvert pour évité d'avoir des problèmes
# il un moyen d'ouvrir et de fermé le fichier après utilisation sans utiliser la fonction close()
with open(chemin, "r", encoding='utf-8') as f:
    # pass
    #contenu = f.read() #affiche le contenu du fichier tel que ecri
    contenu = f.read().splitlines() #reccupère le text dans un tableau avec chaque ligne comme element mais sans le \n
    #contenu = f.readlines() #reccupère le text dans un tableau avec chaque ligne comme element mais avec le \n
    #contenu = repr(f.read()) #affiche le contenu du fichier mais sans tenir compte des saut de ligne
    print(contenu)
# la fonction splitLines() marche sur toute les chaines de caractère, mm du text
# c'est la façon la plus conseillé pour l'utilisation des fichiers


# ecrire à l'interieur d'un fichier
text = "\nJean-christophe est un super dev full stack; \n"
# liste = ["Elie", "Don", "Marcel", 256, 345]
# with open(chemin, "w", encoding='utf-8') as f:
with open(chemin, "a", encoding='utf-8') as f:
    f.write("\nmerci Python pour tout!")
    f.write(text)
# mode "w" ecrase le contenu ancien, pour ajouter du text à c'qui etait avant on utilise le mode "a":append