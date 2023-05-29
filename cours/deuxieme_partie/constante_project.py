import os
# creer des contances du projet qui vont nous permettre à acceder à différent dossier/fichier du projet
 #__file__ retourne le chemin du script actuel
#  realpah recupère le vrai chemin vers le fichier
SOURCE_FILLE = os.path.realpath(__file__)
# le fichier source est recuperé avec dirname et le route vers le dossier source encore avec dirname
SOURCE_DIR = os.path.dirname(SOURCE_FILLE)
ROOT_DIR = os.path.dirname(SOURCE_DIR)
# join permet de joindre des eventuelles elément avec le dossier data
DATA_DIR = os.path.join(SOURCE_DIR, "DATA")

# avec module path
from pathlib import Path

SOURCE_FILLE = Path(__file__).resolve() #qui va nous renvoyer le vrai fichier
SOURCE_DIR = SOURCE_FILLE.parent
ROOT_DIR = SOURCE_DIR.parent
DATA_DIR = SOURCE_DIR / "DATA"

# https://www.docstring.fr/blog/gerer-des-chemins-de-fichiers-avec-pathlib/