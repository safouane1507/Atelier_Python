mot_de_passe_correct = "12345678" 
tentative = ""

while tentative != mot_de_passe_correct:
    tentative = input("Entrez le mot de passe : ")
    if tentative != mot_de_passe_correct:
        print("Mot de passe incorrect. Reessayez.")

print(" Bienvenue !") 