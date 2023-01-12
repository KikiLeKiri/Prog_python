Prenom1 = ""
Nom1 = ""
Prenom2 = ""
Nom2 = ""

Prenom1 = input("Entrez le premier prénom : ")
Nom1 = input("Entrez le premier nom : ")
Prenom2 = input("Entrez le deuxième prénom : ")
Nom2 = input("Entrez le deuxième nom : ")

if Nom1 < Nom2:
    print(Prenom1.capitalize(), Nom1.upper())
    print(Prenom2.capitalize(), Nom2.upper())
elif Nom2 < Nom1:
    print(Prenom2.capitalize(), Nom2.upper())
    print(Prenom1.capitalize(), Nom1.upper())
elif Nom1 == Nom2:
    if Prenom1 < Prenom2:
        print(Prenom1.capitalize(), Nom1.upper())
        print(Prenom2.capitalize(), Nom2.upper())
    else:
        print(Prenom2.capitalize(), Nom2.upper())
        print(Prenom1.capitalize(), Nom1.upper())