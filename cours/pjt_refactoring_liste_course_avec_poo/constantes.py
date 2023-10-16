import os

""""Endroit ou on doit saauvegarder notre liste:
    
    var data

    __file__ return le chemin du script actuel

    os.path.abspath permet de recuperer un chemin absolut

    os.path.dirname permet de reccuperer le dossier de ce chemin
"""

CUR_DIR = os.path.dirname(os.path.abspath(__file__))
DATA_DIR = os.path.join(CUR_DIR, "data")

# print(DATA_DIR)