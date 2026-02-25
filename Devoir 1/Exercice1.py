
age = int(input("Veuillez saisir votre âge : "))

if age < 0:
    print("Âge invalide.")
elif age <= 12:
    status = "Enfant"
elif age <= 17:
    status = "Adolescent" 
elif age <= 64:
    status = "Adulte" 
else:
    status = "Senior" 
print(f"Vous êtes dans la catégorie : {status}")