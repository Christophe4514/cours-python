#organiser des données 
#section 40/244
# Dans ce projet, on commence doucement à s'intéresser à un sujet très prisé des développeurs Python : la data-science.
# on va juste organiser les données contenu dans un fichier
## Le but est de lire un fichier et tous les noms qu'il contient
## trier cette liste de noms, et ré-écrire la liste dans l'ordre alphabétique.

with open(r"C:\Users\Enabel62\OneDrive\Bureau\cours-python\cours\deuxieme_partie\prenoms.txt") as f:
    lines = f.read().splitlines()

prenoms = []
for line in lines:
    prenoms.extend(line.split())

fichier_prenoms_final = [prenom.strip(",. ") for prenom in prenoms]

with open(r"C:\Users\Enabel62\OneDrive\Bureau\cours-python\cours\deuxieme_partie\fichier_prenoms_final.txt", "w") as f:
    f.write("\n".join(sorted(fichier_prenoms_final)))