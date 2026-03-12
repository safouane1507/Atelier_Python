class Personne:
    compteur_instances = 0

    def __init__(self, nom, age):
        self.nom = nom
        self.age = age
        Personne.compteur_instances += 1

    @classmethod
    def creer_depuis_string(cls, donnees):
        """Méthode d'usine pour créer depuis une chaîne"""
        nom, age = donnees.split('-')
        return cls(nom, int(age))

    @classmethod
    def get_nombre_instances(cls):
        """Retourne le nombre d'instances créées"""
        return cls.compteur_instances

# Utilisation
p1 = Personne.creer_depuis_string("Alice-25")
print(Personne.get_nombre_instances())  # Affiche : 1