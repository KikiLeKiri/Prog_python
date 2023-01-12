
#La fonction à appliquer à la liste
def carre(x):
    return x ** 2

#La liste d'entrée
liste = [1, 2, 3, 4, 5]

# Appliquer la fonction à chaque élément de la liste
resultat = map(carre, liste)

# Afficher le résultat
print(list(resultat))
