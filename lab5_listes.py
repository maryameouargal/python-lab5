# etape 1

#Instancie une liste initiale
etudiants = ["Alice", "Bob", "Charlie"]
print(etudiants) 

#Ajoute un élément à la fin avec append()
etudiants.append("Diana")
print(etudiants) 

#Insère à une position précise avec insert()
etudiants.insert(1, "Eve")
print(etudiants)  

#Supprime par valeur avec remove() (enlève la première occurrence
etudiants.remove("Bob")
print(etudiants)  

#Retire et récupère le dernier élément avec pop()
dernier = etudiants.pop()
print(dernier)   
print(etudiants) 

#etape 2 

# Index positif
print(etudiants[0])
print(etudiants[2]) 

# Index négatif
print(etudiants[-1]) 
print(etudiants[-2]) 

# Étape 3

notes = [12, 15, 9, 18, 14, 16]

print(notes[1:4])   
print(notes[:3])    
print(notes[3:])    
print(notes[::2])   
print(notes[::-1])  

# Étape 4 

classe = [
    ["Alice", 20, 15.5],
    ["Eve", 19, 14.0],
    ["Charlie", 21, 16.5]
]

# Ajoute un étudiant via append()
classe.append(["Diana", 22, 13.0])
print(classe)

# Parcours avec for et enumerate() pour afficher
print("\n=== Liste des étudiants ===")
for index, (nom, age, note) in enumerate(classe, start=1):
    print(f"Étudiant {index} : {nom} ({age} ans) - note {note}")
    
    
# Étape 5 

# Accès à la troisième ligne (index 2) et à son âge (index 1)
age_charlie = classe[2][1]
print(age_charlie) # 21

# Modification de la note de Charlie
classe[2][2] = 17.0 # met à jour la note de Charlie