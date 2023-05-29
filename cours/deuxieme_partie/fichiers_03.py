import json
# lecture et ecriture dans un fichier json
# on peut y mettre des chaines de caractères et mm des listes, des fichiers de configuratione t mm des systèmes de BD

chemin = r"C:\Users\Enabel62\OneDrive\Documents\python\cours-python\cours\deuxieme_partie\fichier.json"
# ecriture
with open(chemin, "w", encoding='utf-8') as f:
    # json.dump("Bonjour", f)
    json.dump(list(range(10)), f, indent=4)

# lecture et ajout
with open(chemin, "r", encoding='utf-8') as f:
    lecture = json.load(f)
    print(lecture)
    # print(type(lecture))
liste = list(range(5))
lecture.append(liste)
with open(chemin, "w", encoding='utf-8') as f:
    # json.dump("Bonjour", f)
    json.dump(lecture, f, indent=4)
# on lit le fichier, on le réécrit, on lit à nouveau