################################################## Exercice 1

x = 1
y = 2
Temporaire = x
print("Avant permutation : ")
print("x :", x)
print("y :", y)


x = y 
y = Temporaire

print("Après permutation : ")
print("x :",x )
print("y :", Temporaire)

################################################### Exercice 2

age = int(input("Donnez votre âge : "))
annee = 2022 - age

print("Votre année de naissance est : ",annee)

#################################################### Exercice 3

a=input("Entrez la premiere  valeur : ")
b=input("Entrez la deuxieme  valeur : ")
c=input("Entrez la troisieme valeur : ")

print("Les valeurs entrées sont : a = " + a + ", b = " + b + " et c = " + c)
print("Permutation: a ==> b, b ==> c, c ==> a")
"""      *******************************************
         * Completez le programme a partir d'ici.
         *******************************************
"""
temp = b

b = a
a = c
c = temp


"""     *******************************************
         * Ne rien modifier apres cette ligne.
         *******************************************
"""

print("Les valeurs permutees sont : a = " + a + ", b = " + b + " et c = " + c)


################################################## Exercice 4

Base = 4
Fromage = 800.0
Eau = 2
Ail = 2
Pain = 400 
NbConvives = int(input("Combien de convives pour ce repas ?"))
Nouveau_fromage = (Fromage * NbConvives / Base)
Nouveau_eau = (Eau * NbConvives / Base)
Nouveau_ail = (Ail * NbConvives / Base)
Nouveau_Pain = (Pain * NbConvives / Base)

print("Pour faire une fondue fribourgoise pour", NbConvives," personnes, il vous faut :")
print("- ", Nouveau_fromage, "gr de fromage." )
print("- ", Nouveau_eau, "dl d'eau.")
print("- ", Nouveau_ail, "gousse(s) d'ail.")
print("- ", Nouveau_Pain, "gr de pain.")

#################################################### Exercice 5

