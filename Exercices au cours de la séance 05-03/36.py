class Personne:
    def __init__(self, nom, age):
        self.nom = nom
        self._age = age 

    @property
    def age(self):
        return self._age

    @age.setter
    def age(self, valeur):
        if valeur < 0 or valeur > 120:
            raise ValueError("Âge irréaliste")
        self._age = valeur

    def afficher_infos(self):
        return f"Nom: {self.nom}, Âge: {self.age}"

class Etudiant(Personne):
    def __init__(self, nom, age, cne):
        super().__init__(nom, age)
        self.cne = cne

    def afficher_infos(self):
        return f"[Étudiant] {super().afficher_infos()}, CNE: {self.cne}"

class Salarie(Personne):
    def __init__(self, nom, age, salaire):
        super().__init__(nom, age)
        self.salaire = salaire
    def afficher_infos(self):
        return f"[Salarié] {super().afficher_infos()}, Salaire: {self.salaire} DH"

class Doctorant(Etudiant, Salarie):
    def __init__(self, nom, age, cne, salaire, sujet_these):
        Etudiant.__init__(self, nom, age, cne)
        Salarie.__init__(self, nom, age, salaire)
        self.sujet_these = sujet_these

    def afficher_infos(self):
        return (f"[Doctorant] {Personne.afficher_infos(self)}, "
                f"CNE: {self.cne}, Salaire: {self.salaire} DH, "
                f"Thèse: {self.sujet_these}")

etud = Etudiant("Marouane", 21, "D13456")
prof = Salarie("Redouane", 45, 12000)
doc = Doctorant("Safouane", 21, "G9988", 5000, "Intelligence Artificielle")

print(etud.afficher_infos())
print(prof.afficher_infos())
print(doc.afficher_infos())