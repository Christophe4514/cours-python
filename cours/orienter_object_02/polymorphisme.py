from typing import Self


class Vehicule:
    def avance(self):
        print("Le vehicule démarre")

class Voiture(Vehicule):
    def avance(self):
        # self.avance()
        super().avance()
        print("La voiture roule")
    
class Avion(Vehicule):
    def avance(self):
        # self.avance()
        super().avance()
        print("L'avion vol")
    
v = Voiture()
a = Avion()
a.avance()
v.avance()