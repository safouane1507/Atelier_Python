n1 = float(input("Entrez le premier nombre : "))
n2 = float(input("Entrez le deuxieme nombre : "))

print("1: Addition | 2: Soustraction | 3: Multiplication | 4: Division")
op = input("Votre choix : ")

if op == "1":
    print(f"Resultat : {n1 + n2}")
elif op == "2":
    print(f"Resultat : {n1 - n2}")
elif op == "3":
    print(f"Resultat : {n1 * n2}")
elif op == "4":
    if n2 != 0:
        print(f"Resultat : {n1 / n2}")
    else:
        print("Erreur : Division par zero impossible.")
else:
    print("Operation non reconnue.")