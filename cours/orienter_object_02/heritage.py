projets = ["pr_GameOfThrones", "HarryPotter", "pr_Avengers"]

class Utilisateur:
    def __init__(self, nom, prenom) -> None:
        self.nom = nom
        self.prenom = prenom

    def __str__(self) -> str:
        return f"Utilisateur {self.nom} {self.prenom}"
    
    def afficher_projets(self):
        for projet in projets:
            print(projet)


#heritage : junior herite de la class utilisateur
class Junior(Utilisateur):
    def __init__(self, nom, prenom) -> None:
        super().__init__(nom, prenom)
        

paul = Junior("paul", "Durant")
paul.afficher_projets()
print(paul)