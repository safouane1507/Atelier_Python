class Personne:
    def __init__(self, nom, age):
        self.nom = nom
        self.age = age 

    def se_presenter(self):
        return f"Je suis {self.nom}, j'ai {self.age} ans"

    @property
    def age(self):
        return self._age

    @age.setter 
    def age(self, valeur):
        if not isinstance(valeur, int):
            raise TypeError("Entrez une valeur entière (INT)")
        if valeur < 0:
            raise ValueError("L'âge ne peut pas être inférieur à 0")
        if valeur > 140:
            raise ValueError("L'âge indiqué est irréaliste")
        self._age = valeur

personne1 = Personne("Safouane", 21)
personne2 = Personne("Redouane", 21)
personne3 = Personne("Marouane", 21)

print(f"Ancien âge : {personne1.age}")
personne1.age = 30  
print(f"Nouvel âge : {personne1.age}")

print(personne1.se_presenter())
print(personne2.se_presenter())
print(personne3.se_presenter())