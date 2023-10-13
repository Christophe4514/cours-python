# Dans les prochaines parties, je vais vous présenter un package qui permet de générer un 
# éventail très large de données aléatoires.
# Numéro de téléphone, prénoms, numéros de carte bancaire, d'adresses.
# Bref, un package très utile quand on commence à travailler sur des projets de plus grande 
# envergure et que l'on a besoin de remplir une base de données de test par exemple.

# pour utiliser faker il va faloir l'installer

from faker import Faker

# fake = Faker()
# on peut aussi ajouter une address :
fake = Faker(locale="fr_FR") # pour la france, "en_US" pour USA

print(fake.name())
print(fake.address())
print(fake.email())
print(fake.text())

