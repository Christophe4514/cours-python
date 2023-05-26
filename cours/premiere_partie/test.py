print("hello \n wiz! \n")
# les variables, comment ca marche

sac_a_dos = ['stylo', 'cahier', 'ordinateur', 'chargeur', 'airpod']
sac_a_dos = ['stylo', 'cahier', 'ordinateur', 'chargeur', 'airpod pro']

print(sac_a_dos)

prenom = "wiz"
autre_prenom = prenom
print(id(prenom))
print(id(autre_prenom))

nom = "okko"
autre_nom = "wizamo"
print(id(nom))
print(id(autre_nom))

# fonction et portée des variables

# def hello_live():
#     mon_prenom = "live"
#     print('Hello {}'.format(mon_prenom))

# print(mon_prenom) ne va pas marcher  par contre :
mon_prenom = "live"


def hello_live():
    print('Hello {}'.format(mon_prenom))


hello_live()

# les constates
PI = 3.14
code_couleur = '#ff043'

# concatenation
print(nom + ' ' + mon_prenom)
age = 24
mon_age = str(age)

print(mon_prenom + " j'ai {}".format(mon_age))
