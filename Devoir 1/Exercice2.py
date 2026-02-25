
contacts = []

while True: 
  
    print("\n Menu ")
    print("1. Ajouter un contact")
    print("2. Afficher tous les contacts")
    print("3. Quitter ")
    
    choix = input("Choisissez une option (1-3) : ")

    if choix == "1":
        nom = input("Entrez le nom du contact : ")
        contacts.append(nom) 
        print("Contact ajouté !")
        
    elif choix == "2":
        print("\n Liste des contacts :")
        
        for i, contact in enumerate(contacts, 1):
            print(f"{i}. {contact}")
            
    elif choix == "3":
        print("Au revoir !") 
        break
    else:
        print("Choix invalide, réessayez.")