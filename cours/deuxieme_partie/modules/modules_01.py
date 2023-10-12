# LES MODULES SONT DES FICHIERS PYTHON QUI CONTIENNENT DES VARIABLES, 
# CLASSES OU INSTRUCTIONS POUVANT ÊTRE IMPORTÉES ET EXÉCUTÉ DANS UN AUTRE FICHIER.

# Explicit is better than implicit
# En Python, un module est un fichier contenant des définitions de fonctions, de classes et de variables, ainsi que des instructions exécutables.

# En d'autres termes, c'est une manière d'organiser le code de manière logique et cohérente.

# Le nom du module est dérivé du nom du fichier (sans l'extension .py).

# Par exemple, un fichier nommé calcul.py correspondrait au module calcul.

# Voici un exemple simple de module en Python :
# :::python
# /mon_projet/salutations.py
def dire_bonjour():
    return "Bonjour !"

def dire_bonsoir():
    return "Bonsoir !"

# L'utilisation de modules en Python se fait grâce à l'instruction import.

# Cette instruction permet d'importer un module et d'utiliser les fonctions, classes et variables qu'il définit.

# Voici comment on pourrait utiliser le module salutations défini précédemment :

# :::python
# importation du module salutations
import salutations

# utilisation des fonctions définies dans le module
print(salutations.dire_bonjour())  # affiche "Bonjour !"
print(salutations.dire_bonsoir())  # affiche "Bonsoir !"

# Il est également possible d'importer uniquement certaines fonctions ou classes d'un module, en utilisant la syntaxe from ... import ...

# :::python
# importation de la fonction dire_bonjour du module salutations
from salutations import dire_bonjour

# utilisation de la fonction
print(dire_bonjour())  # affiche "Bonjour !"
