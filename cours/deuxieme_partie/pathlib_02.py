# lire dans un fichier
from pathlib import Path
p = Path(r"C:\Users\Enabel62\OneDrive\Documents\python\cours-python\cours\deuxieme_partie")
# p.write_text("\n Live is my Babe")
# p.write_text("\n Elle est génial")
# print(p.read_text()) #lecture

# scanner un dossier
print(Path.home().iterdir()) #retourne un objet du type generateur
for f in Path.home().iterdir() :
    #print(f) #f est un objet de type path, on 
    # print(f.name) #on reccupère que les noms de dossiers
    print(f.is_dir()) # il est possible de reccuperer que des dossier avec is_dir()
    # print(f.is_file)

# glob
for f in p.glob("*.txt"): #on agit sur le dossier de façon non reccursif
    print(f.name)
for f in p.glob("*.json"):
    print(f.name)
for f in p.glob("*.png"):
    print(f.name)

for f in p.rglob("*.py"): #on agit de façon recursif
    print(f.name)

# 
# ajouter suffix à un nom de fichier
p = Path.home() / "image.png"
print(p)
p_1 = p.parent / p.stem #retourne \Users\Enabel62\image sans extenssion
p_1 = p.parent / (p.stem + "-lowres" + p.suffix) #ajoute un suffix au nom du fichier avant son extenssion
print(p_1)