# Définition des variables
notes = []
moyenne = 0

# Demande à l'utilisateur le nombre d'étudiants
nb_etudiants = int(input("Entrez le nombre d'étudiants : "))

# Boucle qui demande à l'utilisateur les notes de chaque étudiant
for i in range(nb_etudiants):
    note = int(input("Entrez la note de l'étudiant n°" + str(i+1) + " : "))
    if note < 0 or note > 20 :
        print("Entrez une valeur comprise entre 0 et 20")
        note = float(input("Entrez les moyennes de chaque étudiant : "))
    notes.append(note)
    moyenne += note

# Calcul de la moyenne
moyenne = moyenne / nb_etudiants

# Affiche la moyenne
print("La moyenne de classe est :", moyenne)

# Boucle qui calcule et affiche l'écart à la moyenne pour chaque étudiant
for i in range(nb_etudiants):
    ecart = notes[i] - moyenne
    print("L'écart à la moyenne pour l'étudiant n°" + str(i+1) + " est :", ecart)