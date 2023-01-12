# Demande le nombre d'étudiants à l'utilisateur
nombreEtudiants = int(input("Donnez le nombre d'etudiants : "))
moyenne = 0.0

# déclaration d’une liste vide qui va contenir autant de notes que d'étudiants
notes = []
for i in range (nombreEtudiants):
    moyenneEtudiant = float(input("Entrez les moyennes de chaque étudiant : "))
    if moyenneEtudiant < 0 or moyenneEtudiant > 20 :
        print("Entrez une valeur comprise entre 0 et 20")
        moyenneEtudiant = float(input("Entrez les moyennes de chaque étudiant : "))
        print ("Note étudiant ",moyenneEtudiant[i], " : ",moyenneEtudiant )
    moyenne = moyenne + moyenneEtudiant / nombreEtudiants
    notes.append(moyenneEtudiant)
print ("Moyenne de classe : ", moyenne)
ecartMoyenne = moyenneEtudiant - moyenne
print ("Numéro de l'étuiant | note | écart à la moyenne")
print (notes, " | ", notes[i], " | ", ecartMoyenne)





