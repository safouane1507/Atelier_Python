class Vehicule:
    def __init__(self, marque, vitesse):
        self._marque = marque
        self.vitesse = vitesse
    def accelerer(self):
        print(f"{self._marque} accelere")
    def freiner(self):
        print(f"{self._marque} Freine")

class Voiture(Vehicule):
    def __init__(self, marque, vitesse, nbr_portes):
        super().__init__(marque, vitesse)
        self.nbr_portes = nbr_portes

    def klaxonner(self):
        print(f"{self.marque} klaxonne")

unevoiture = Voiture("kangoo",0,8)
unevoiture.accelerer
unevoiture.freiner
unevoiture.klaxonner
