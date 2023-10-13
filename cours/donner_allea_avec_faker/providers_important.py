# toujour voir la doc
from unicodedata import category
from faker import Faker


fake = Faker(locale="fr_FR") # pour la france, "en_US" pour USA

for _ in range(10):
    # print(fake.job())
    # print(fake.file_path())
    # print(fake.file_path(depth=5)) #on definit une profondeur
    print(fake.file_path(depth=5, category='video')) #on definit une profondeur et la catégorie des fichiers
    print(fake.credit_card_number(), fake.credit_card_expire(), fake.credit_card_security_code())
    print(fake.rgb_color())
    print(fake.hex_color())