# Mini-projet – Gestion simplifiée d'une classe (SANS NUMÉROS)

classe = [
    ["Alice", 20, 15.5],
    ["Bob", 19, 12.0],
    ["Charlie", 22, 16.0]
]

def ajouter_etudiant(classe):
    nom = input("Nom : ").strip()
    try:
        age = int(input("Age : "))
        note = float(input("Note : "))
    except ValueError:
        print("Saisie invalide.")
        return
    classe.append([nom, age, note])
    print(f"{nom} ajouté.")

def afficher_tableau(etudiants):
    """AFFICHAGE SANS NUMÉROS PERMANENTS"""
    print("\n" + "="*40)
    print(f"{'Nom':<12} {'Âge':<6} {'Note':<6}")
    print("-" * 40)
    for etudiant in etudiants:
        print(f"{etudiant[0]:<12} {etudiant[1]:<6} {etudiant[2]:<6.1f}")
    print("=" * 40)

def afficher_classe(classe):
    if not classe:
        print("La classe est vide.")
        return
    print(f"\n=== LISTE DES ÉTUDIANTS ({len(classe)} total) ===")
    afficher_tableau(classe)

def supprimer_etudiant(classe):
    if not classe:
        print("Rien à supprimer.")
        return
    
    afficher_classe(classe)
    
    nom_recherche = input("\nNom de l'étudiant à supprimer : ").strip().lower()
    
   
    resultats = []
    for i, etudiant in enumerate(classe):
        if etudiant[0].lower() == nom_recherche:
            resultats.append((i, etudiant))
    
    if not resultats:
        print("Aucun étudiant trouvé avec ce nom.")
        return
    elif len(resultats) == 1:
    
        index, etudiant = resultats[0]
        if confirmer_suppression(etudiant[0]):
            etudiant_supprime = classe.pop(index)
            print(f"{etudiant_supprime[0]} supprimé.")
    else:
        # Plusieurs étudiants avec le même nom
        print("\nPlusieurs étudiants trouvés :")
        for j, (index, etudiant) in enumerate(resultats, 1):
            print(f"{j}. {etudiant[0]} - {etudiant[1]} ans - note {etudiant[2]}")
        
        try:
            choix = int(input("Quel étudiant voulez-vous supprimer ? (numéro) : "))
            if 1 <= choix <= len(resultats):
                index, etudiant = resultats[choix-1]
                if confirmer_suppression(etudiant[0]):
                    etudiant_supprime = classe.pop(index)
                    print(f"{etudiant_supprime[0]} supprimé.")
            else:
                print("Choix invalide.")
        except ValueError:
            print("Saisie invalide.")

def mettre_a_jour_etudiant(classe):
    if not classe:
        print("Classe vide.")
        return
    
    
    afficher_classe(classe)
    
    nom_recherche = input("\nNom de l'étudiant à modifier : ").strip().lower()
    
   
    resultats = []
    for etudiant in classe:
        if etudiant[0].lower() == nom_recherche:
            resultats.append(etudiant)
    
    if not resultats:
        print("Aucun étudiant trouvé avec ce nom.")
        return
    elif len(resultats) == 1:
        
        etudiant = resultats[0]
        print(f"Modification de {etudiant[0]} :")
        
        nouveau_nom = input("Nouveau nom : ").strip()
        if nouveau_nom:
            etudiant[0] = nouveau_nom
        
        entree_age = input("Nouvel âge : ").strip()
        if entree_age:
            try:
                etudiant[1] = int(entree_age)
            except ValueError:
                print("(saisie invalide).")
        
        entree_note = input("Nouvelle note : ").strip()
        if entree_note:
            try:
                etudiant[2] = float(entree_note)
            except ValueError:
                print("(saisie invalide).")
    else:
        # Plusieurs étudiants avec le même nom
        print("\nPlusieurs étudiants trouvés :")
        for j, etudiant in enumerate(resultats, 1):
            print(f"{j}. {etudiant[0]} - {etudiant[1]} ans - note {etudiant[2]}")
        
        try:
            choix = int(input("Quel étudiant voulez-vous modifier ? (numéro) : "))
            if 1 <= choix <= len(resultats):
                etudiant = resultats[choix-1]
                print(f"Modification de {etudiant[0]} :")
                
                nouveau_nom = input("Nouveau nom : ").strip()
                if nouveau_nom:
                    etudiant[0] = nouveau_nom
                
                entree_age = input("Nouvel âge : ").strip()
                if entree_age:
                    try:
                        etudiant[1] = int(entree_age)
                    except ValueError:
                        print("Âge ignoré (saisie invalide).")
                
                entree_note = input("Nouvelle note : ").strip()
                if entree_note:
                    try:
                        etudiant[2] = float(entree_note)
                    except ValueError:
                        print("Note ignorée (saisie invalide).")
            else:
                print("Choix invalide.")
        except ValueError:
            print("Saisie invalide.")

def confirmer_suppression(nom):
    confirmation = input(f"Êtes-vous sûr de vouloir supprimer {nom} ? (o/n): ").strip().lower()
    return confirmation in ['o', 'oui', 'y', 'yes']

def rechercher_etudiant(classe):
    nom_recherche = input("Nom à rechercher: ").strip().lower()
    resultats = []
    
    for etudiant in classe:
        if nom_recherche in etudiant[0].lower():
            resultats.append(etudiant)
    
    if resultats:
        print(f"\n{len(resultats)} étudiant(s) trouvé(s):")
        afficher_tableau(resultats)
    else:
        print("Aucun étudiant trouvé.")

def afficher_statistiques(classe):
    if not classe:
        print("Pas de données.")
        return
    
    notes = [etudiant[2] for etudiant in classe]
    moyenne = sum(notes) / len(notes)
    meilleure = max(classe, key=lambda e: e[2])
    pire = min(classe, key=lambda e: e[2])
    
    print(f"\n=== STATISTIQUES ===")
    print(f"Moyenne des notes : {moyenne:.2f}")
    print(f"Meilleure note : {meilleure[2]} ({meilleure[0]})")
    print(f"Moins bonne note : {pire[2]} ({pire[0]})")

# Boucle principale
while True:
    print("\n" + "="*30)
    print("GESTION DE LA CLASSE")
    print("="*30)
    print("1. Afficher tous les étudiants")
    print("2. Ajouter un étudiant")
    print("3. Supprimer un étudiant")
    print("4. Modifier un étudiant")
    print("5. Statistiques")
    print("6. Rechercher un étudiant")
    print("q. Quitter")
    
    choix = input("Choisiez le numéro de l'option  : ").strip().lower()
    
    if choix == "1":
        afficher_classe(classe)
    elif choix == "2":
        ajouter_etudiant(classe)
    elif choix == "3":
        supprimer_etudiant(classe)
    elif choix == "4":
        mettre_a_jour_etudiant(classe)
    elif choix == "5":
        afficher_statistiques(classe)
    elif choix == "6":
        rechercher_etudiant(classe)
    elif choix == "q":
        print("Au revoir !")
        break
    else:
        print("Option inconnue.")