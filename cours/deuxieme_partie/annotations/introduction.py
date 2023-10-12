# Les annotations de type (Type Hinting) sont une nouveauté de la version 3.5 de Python.
# Dans cette partie, je vais vous parler de ces annotations qui nous permettent de spécifier le type des paramètres d'une fonction,
#ou encore le type d'une variable.
# Les annotations de type sont facultatives, on peut très bien s'en passer.

# # utilité

# supposons qu'on ait la fonction add :

def add(a, b):
    print(a + b)

add(10, 6)

# et que pendant l'appel de la fonction on passe le argumens suivents à la place
# des nombres :

#add("a", 8) #c'qui nous genere une erreur

# dans ce cas il faut utiliser les types hinting pour prevevnir ces problèmes 
# tq on peut definir le type de chaque param et le type de retour de la fonction si c'est pas un voir

def adds(a: int,b: int) -> int:
    return a + b 

adress = adds(10, 20)
print(adress)