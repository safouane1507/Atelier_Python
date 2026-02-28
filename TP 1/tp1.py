donnees = [
("Sara", "Math", 12, "G1"),
("Sara", "Info", 14, "G1"),
("Ahmed", "Math", 9, "G2"),
("Adam", "Chimie", 18, "G1"),
("Sara", "Math", 11, "G1"),
("Bouchra", "Info", "abc", "G2"),
("", "Math", 10, "G1"),
("Yassine", "Info", 22, "G2"),
("Ahmed", "Info", 13, "G2"),
("Adam", "Math", None, "G1"),
("Sara", "Chimie", 16, "G1"),
("Adam", "Info", 7, "G1"),
("Ahmed", "Math", 9, "G2"),
("Hana", "Physique", 15, "G3"),
("Hana", "Math", 8, "G3"),
]

def valider (enregistrement):
    nom, matiere, note, group =enregistrement
    if not str(nom).strip() or not str(matiere).strip() or not str(group).strip():
        return (False,"saisir tous les donners")
    try:

        note_f = float(note)
    except (ValueError, TypeError):
        return (False,"donner un nombre")
    if not (0 <= note_f <= 20):
        return (False,"donner entre 0 et 20")
    return (True, "")
valider = []
erreurs = []
doublons_exact = set()
vus = []
for entry in donnees:
    if donnees.count(entry) > 1:
        doublons_exact.add(entry)
        est_valide, raison = valider(entry)
        if est_valide:
            valider.append(entry[0],entry[1], float(entry[2]), entry[3])
        else:
            erreurs.append({"valeur:": entry , "raison:": raison})

#partie2

matieres_dis = {enr[1] for enr in valider}
str_etudiants = {}
groupes_pedago = {}
for nom, matiere, note, groupe in valider:
    if nom not in str_etudiants:
        str_etudiants[nom] = {}
    if matiere not in str_etudiants[nom]:
        str_etudiants[nom][matiere] = []
    str_etudiants[nom][matiere].append(note)
    if groupe not in groupes_pedago:
        groupes_pedago[groupe] = set()
    groupes_pedago[groupe].add(nom)

#partie3
def somme_recursive(liste_notes):
    if not liste_notes:
        return 0
    return liste_notes[0] + somme_recursive(liste_notes[1:])
def calculer_moyenne(liste_notes):
    if not liste_notes:
        return 0
    return somme_recursive(liste_notes) / len(liste_notes)

moyennes_etudiants = {}
for etudiant, matieres in str_etudiants.items():
    toutes_notes = []
    moyennes_par_matiere = {}
    for mat, notes in matieres.items():
        moyennes_par_matiere[mat] = calculer_moyenne(notes)
        toutes_notes.extend(notes)
    
    moyennes_etudiants[etudiant] = {
        "generale": calculer_moyenne(toutes_notes), "par_matiere": moyennes_par_matiere}
    
#partie4

noti_err = { "doublons_saisie": [], "profils_incomplets": [], "groupes_faibles": [], "performances_instables": [] }
for etudiant, matieres in str_etudiants.items():
    toutes_notes_etud = []
    for mat, notes in matieres.items():
        toutes_notes_etud.extend(notes)
        if len(notes) > 1:
            noti_err["doublons_saisie"].append(f"{etudiant} a plusieurs notes en {mat}")

    if toutes_notes_etud and (max(toutes_notes_etud) - min(toutes_notes_etud) > 7):
        noti_err["performances_instables"].append(etudiant)

    
for etudiant, matieres in str_etudiants.items():
    if set(matieres.keys()) != matieres_dis:
        noti_err["profils_incomplets"].append(etudiant)


for gp, etudiants in groupes_pedago.items():
    moyennes_gp = [moyennes_etudiants[e]["generale"] for e in etudiants]
    if calculer_moyenne(moyennes_gp) < 10:
        noti_err["groupes_faibles"].append(gp)

print("Alerte !!!")
for type_alerte, liste in noti_err.items():
    print(f"{type_alerte} : {liste}")