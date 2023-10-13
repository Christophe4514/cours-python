# par exemple vous creez une app pour gerer un inventaire d'une librairie
# en generant des ISBN 
from faker import Faker

fake = Faker(locale="fr_FR") # pour la france, "en_US" pour USA

# utiliser la classe numerify qui urilise des symboles pour representer des lettres et chifres
#  "#" est remplacer par un nombre de 0-9
#  "%" 1-9

for _ in range(5):
    print(fake.numerify(text="%%%-%-%%%%-%%%%-%%%-##"))

# bothify pour des numéros de produits par exemple
#  "?" A-Z ou a-z
# "#" 0-9

for _ in range(5):
    print(fake.bothify(text="Product Number: ????-#######"))

for _ in range(5):
    print(fake.bothify(text="Immatriculation: ??-####-#%"))
