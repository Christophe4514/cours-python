import pathlib
from pathlib import Path
import shutil
# pathlib, module de manipilation des chemin des dossiers et fichier
# 1 problème de chemin
# p = pathlib.Path(r"C:\Users\Enabel62\OneDrive\Documents\python\cours-python\cours\deuxieme_partie")
# print(p.parent)
# print(pathlib.Path.cwd())

# concatener des chemins
# print(Path.joinpath(p, "list.json"))
# print(Path.joinpath(p, "list.json").suffix)
# print(Path.suffix("list.json"))

# reccuperer info sur chemin
# p = Path(r"C:\Users\Enabel62\OneDrive\Documents\python\cours-python\cours\deuxieme_partie\liste.json")
# print(p.name)
# print(p.stem)
# print(p.parts)
# print(p.exists)
# print(p.is_dir)
# print(p.is_file)
# print(p.parent)
# print(p.parent.parent)
# print(dir(p))

# creer et supprimer dossier et fichier
p = Path(r"C:\Users\Enabel62\OneDrive\Documents\python\cours-python\cours\deuxieme_partie")
p = p / "DossierTest"
# print(p)
p.mkdir(exist_ok=True)
# p = p / "1" / "2" / "3"
# p.mkdir() ne va pas marché pour creer les hierarchies ...
# il faut préciser Parent=True pour pouvoir creer cette hiérarchie
# p.mkdir(parents=True)
# p = p / "readme.txt"
# p.touch() #cree le fichier
# p.unlink() #retire le fichier
p.rmdir()
shutil.rmtree(p) #permet de supprimer une hiérarchie de dossier mm non vide
print(p)