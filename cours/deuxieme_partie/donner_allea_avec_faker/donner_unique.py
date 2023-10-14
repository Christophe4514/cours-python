from faker import Faker


fake = Faker(locale="fr_FR") # pour la france, "en_US" pour USA

for _ in range(500):
    print(fake.unique.random_int())

# test avec assertion
numbers = [fake.unique.random_int()for _ in range(500)]
assert len(numbers) == len(set(numbers))

for _ in range(300):
    print(fake.unique.first_name())