# voir la syntaxe
# configurer vs et pycharme pour les anotations 
# gerer le code avec la bibliothèque MyPy

# Spécification du type :

def adds(a: int,b: int) -> int: # type: ignore
    return a + b 

# si on veut ajouter les valeurs par defaut :
def adds(a: int = 5 ,b: int = 6) -> int:
    return a + b 

nom: str = "your"