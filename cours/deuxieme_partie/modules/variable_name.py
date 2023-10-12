# La variable __name__ est une variable spéciale de Python dont la valeur est automatiquement
#  déterminée en fonction de la façon dont un script est exécuté.

# Si vous exécutez le script python directement la variable __name__ contiendra la chaîne de caractères "__main__".

# Pour vérifier par vous-même, vous pouvez ajouter la ligne print(__name__) dans un fichier python 
# et l'exécuter depuis le terminal comme ceci :

print(__name__)

# Si vous importez le script en tant que module, la variable __name__ sera égale au nom du module.

# Dans quel cas utiliser la variable __name__ ?

# On utilise souvent cette variable à l'intérieur de la structure conditionnelle suivante :
"""Module de test"""

def foo():
    """Fonction de test"""
    pass

if __name__ == "__main__":
    print("Ce code ne sera exécuté que si le script Python est exécuté directement.")
    print("Si le module est importé, ce code ne sera pas exécuté car la variable __name__ ne sera pas égale à '__main__' mais au nom du module (donc du fichier python).")

# On pourrait imaginer par exemple un module Python qui permette de convertir des images d'un format à un autre.

# Ce module contient des fonctions que l'on peut utiliser dans d'autres scripts Python, comme la fonction convert_image :

# /Users/Docstring/convert_utilities.py
"""Fonctions pour convertir des images"""

import sys

def convert_image(source, format="PNG"):
    """Cette fonction convertie le fichier envoyé au paramètre source au format indiqué par le paramètre format."""
    pass

if __name__ == "__main__":
    image_path = sys.argv[-2]
    format = sys.argv[-1]
    convert_image(source=image_path, format=format)
