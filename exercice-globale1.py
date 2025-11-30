# Exercice 1 : Tri et statistiques

classe = [
    ["Alice", 20, 15.5],
    ["Eve", 19, 14.0], 
    ["Charlie", 21, 16.5],
    ["Diana", 22, 13.0]
]

# 1. TRI PAR  DÉCROISSANTE
classe.sort(key=lambda ligne: ligne[2], reverse=True)

print("=== Classement par note décroissante ===")
for etudiant in classe:
    print(f"{etudiant[0]} - Note: {etudiant[2]}")

# 2. CALCUL DE LA MOYENNE
total_notes = 0
for etudiant in classe:
    total_notes += etudiant[2]  # etudiant[2] = la note

moyenne = total_notes / len(classe)
print(f"\nMoyenne de la classe: {moyenne:.2f}")

# Exercice 2 : Recherche

nom_recherche = input("Entrez un nom : ")
resultat = next((etudiant for etudiant in classe if etudiant[0].lower() == nom_recherche.lower()), None)

if resultat:
    print(f"Trouvé: {resultat[0]}, {resultat[1]} ans, note {resultat[2]}")
else:
    print("Non trouvé ")
    
# Exercice 3 : Copie superficielle vs profonde

print("Liste originale avant modification :")
print(classe)

# Copie superficielle
classe_copie = classe[:]  # ou classe.copy()

# Modification dans la copie
classe_copie[0][1] = 99 
print("\nAprès modification de classe_copie[0][1]  :")
print("Classe originale :", classe)
print("Classe copie     :", classe_copie)

# Exercice 4 

classe_dict = []
for etudiant in classe:
    dict_etudiant = {
        "nom": etudiant[0],
        "age": etudiant[1], 
        "note": etudiant[2]
    }
    classe_dict.append(dict_etudiant)

print("Liste de dictionnaires :")
print(classe_dict)
