from abc import ABC, abstractmethod
from dataclasses import dataclass

class Boisson(ABC):
    @abstractmethod
    def cout(self):
        pass

    @abstractmethod
    def description(self):
        pass

    def __add__(self, other):
        return BoissonCombinee(self, other)

class Cafe(Boisson):
    def cout(self):
        return 2.0

    def description(self):
        return "cafe simple"

class The(Boisson):
    def cout(self):
        return 1.5

    def description(self):
        return "The"

class DecorateurBoisson(Boisson):
    def __init__(self, boisson):
        self.boisson = boisson

    def cout(self):
        return self.boisson.cout()

    def description(self):
        return self.boisson.description()

class Lait(DecorateurBoisson):
    def cout(self):
        return self.boisson.cout() + 0.5

    def description(self):
        return self.boisson.description() + ", Lait"

class Sucre(DecorateurBoisson):
    def cout(self):
        return self.boisson.cout() + 0.2

    def description(self):
        return self.boisson.description() + ", Sucre"

class Caramel(DecorateurBoisson):
    def cout(self):
        return self.boisson.cout() + 0.8

    def description(self):
        return self.boisson.description() + ", Caramel"

class BoissonCombinee(Boisson):
    def __init__(self, b1, b2):
        self.b1 = b1
        self.b2 = b2

    def cout(self):
        return self.b1.cout() + self.b2.cout()

    def description(self):
        return self.b1.description() + " et " + self.b2.description()

@dataclass
class Client:
    nom: str
    numero: int
    points_fidelite: int = 0

class Commande:
    def __init__(self, client):
        self.client = client
        self.boissons = []

    def ajouter_boisson(self, boisson):
        self.boissons.append(boisson)

    def calculer_total(self):
        total = 0
        for b in self.boissons:
            total += b.cout()
        return total

    def afficher(self):
        print("Commande Client:", self.client.nom)
        for b in self.boissons:
            print("-", b.description(), ":", b.cout(), "€")
        print("Total:", self.calculer_total(), "€")

class CommandeSurPlace(Commande):
    def afficher(self):
        print("****** SUR PLACE ******")
        super().afficher()

class CommandeEmporter(Commande):
    def afficher(self):
        print("****** A EMPORTER ******")
        super().afficher()

class Fidelite:
    def ajouter_points(self, client, montant):
        points = int(montant) * 10
        client.points_fidelite += points

class CommandeFidele(Commande, Fidelite):
    def valider_commande(self):
        total = self.calculer_total()
        self.ajouter_points(self.client, total)

if __name__ == "__main__":
    client1 = Client("Safouane", 101, 0)
    
    b1 = Cafe()
    b1 = Lait(b1)
    b1 = Sucre(b1)

    b2 = The()
    b2 = Caramel(b2)

    b3 = b1 + b2

    cmd = CommandeFidele(client1)
    cmd.ajouter_boisson(b1)
    cmd.ajouter_boisson(b2)
    cmd.ajouter_boisson(b3)

    cmd.afficher()
    cmd.valider_commande()
    
    print("***Points de fidelite de", client1.nom, ":", client1.points_fidelite, "***")
