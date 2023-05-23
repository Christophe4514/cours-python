# f string
nom = "paul"
# hello = f"Bonjour {nom}"
print(f"Bonjour {nom.upper()}")
a = 24
b = 54
print(f"la somme de a et b  donne {a + b}")

protocole = "https://"
nom_du_site = "docstring"
extension = "fr"
page = "glossaire"

# Modifiez le code à partir d'ici 
URL = f"{protocole}www.{nom_du_site}.{extension}/{page}/"
print(URL)

# methode format()
age = 25
print("j'ai {} ans".format(age)) #format() pour les versions < 3.6

# https://www.docstring.fr/blog/le-formatage-des-chaines-de-caracteres-avec-python/
# lien article sur utilisation f string et format()