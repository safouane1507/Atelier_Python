class Personne:
    def __init__(self, nom, age, email):
        self.nom = nom
        self.age = age
        self.email = email


personne1 = Personne('Safouane', 21, 'safouane@email.com')

print(f"Nom: {personne1.nom}")                
print(f"Âge: {personne1.age}")                
print(f"Email: {personne1.email}")            

personne1.nom = 'Safouane sqel'                
personne1.age += 1                            
personne1.email = 'safouane.1507@houtmail.fr'    

print(f"Nouveau nom: {personne1.nom}")       
print(f"Nouvel âge: {personne1.age}")         