class Personne:
    compteur_instances = 0

    def __init__(self, nom, age):
        self.nom = nom
        self.age = age
        Personne.compteur_instances += 1

    def __eq__(self, other):
        if isinstance(other, Personne):
            return self.nom == other.nom
        return False

    def __lt__(self, other):
        if isinstance(other, Personne):
            return self.age < other.age
        return NotImplemented

    @classmethod
    def creer_depuis_string(cls, donnees):
        nom, age = donnees.split('-')
        return cls(nom, int(age))


p1 = Personne("safouane", 21)
p2 = Personne("moreda", 22)
p3 = Personne("adnane", 19)

print(p1 == p2)
print(p1 == p3)

personnes = [p1, p2, p3]

personnes.sort()
for n in personnes:
    print(n.nom)