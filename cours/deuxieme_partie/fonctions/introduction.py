# Pour créer une fonction, on utilise le mot clé def :
def foo():
    print("La fonction s'exécute")


# Il suffit ensuite d'utiliser le nom de la fonction suivie de parenthèses pour exécuter le code qu'elle contient :
def foo():
    print("La fonction s'exécute")

foo()

# Une fonction peut posséder un ou plusieurs paramètres :
def somme(a, b):
    print(a + b)

somme(10, 5)

# On peut retourner une valeur dans une fonction grâce au mot clé return.

def somme(a, b):
    return a + b
    print(a + b)#ne sera jamais exécuter

somme(10, 5)

# La valeur retournée par une fonction peut être récupérée dans une variable lors de l'appel de la fonction :
def somme(a, b):
    return a + b

resultat = somme(10, 5)
print(resultat)

# Espaces global et local
# Quand vous définissez une fonction, vous définissez un espace local à la fonction.

a = 5
 
def foo():
    a = 10
    print(a)
 
foo()
print(a)

# ☝️ Dans ce code, on crée une variable a dans la fonction qui est donc différente de la variable a 
# définie dans l'espace globale.

# Ce script affichera donc 10 (la valeur de a dans la fonction foo que l'on appelle) puis 5 (la valeur de a 
# dans l'espace global, qui n'a donc pas été modifiée).

def saluer(nom):
    print("Bonjour", nom)
    
saluer("Patrick")

###
def multiplicateur_mot(mult=5, mot=""):
	for i in range(mult):
          print(mot)

mot_multiplie = multiplicateur_mot(mot="Bonjour")

#####
def addition(a, b):
    c = a + b
    return c

resultat = addition(5, 10)
print(resultat)