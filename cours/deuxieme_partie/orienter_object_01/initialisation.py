# avec la methode __init__
# class Voiture:
#     voitures_crees = 0
#     def __init__(self, marque) -> None:
#         Voiture.voitures_crees += 1
#         self.marque = marque


# voiture_01 = Voiture("Bolide_Allemand V12")
# voiture_02 = Voiture("Hybride")
# voiture_03 = Voiture("4 Matic")
# print(f"nombre de voiture de l'usine: {Voiture.voitures_crees} :{voiture_01.marque} , {voiture_02.marque} , {voiture_03.marque}")


class Livres:
    def __init__(self, nom, nombre_de_pages, prix):
        self.nom = nom
        self.nombre_de_pages = nombre_de_pages
        self.prix = prix

livre_HP = Livres("Harry Potter", 300, 10.99)
livre_LOTR = Livres("Le Seigneur des Anneaux", 400, 13.99)

print(f"{livre_HP.nom} {livre_HP.nombre_de_pages} {livre_HP.prix}")
print(f"{livre_LOTR.nom} {livre_LOTR.nombre_de_pages} {livre_LOTR.prix}")



class Voiture:
    prix = 30000
    def __init__(self, prix):
        self.prix = prix
 
Peugeot = Voiture(prix=20000)
print(Peugeot.prix)