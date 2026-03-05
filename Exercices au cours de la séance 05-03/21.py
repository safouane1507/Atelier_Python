class Personne:
    def __init__(self,nom,age):
        self.nom = nom
        self.age = age
    def se_presenter(self):
        return f"Je suis {self.nom}, {self.age}"

Personne1 = Personne("Safouane",21)
print(Personne1.se_presenter())

Personne2 = Personne("Redouane",21)
print(Personne2.se_presenter())

Personne3 = Personne("Marouane",21)
print(Personne3.se_presenter())