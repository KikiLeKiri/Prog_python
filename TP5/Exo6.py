def tailleCHAINE(T): 
    longueur = 0
    while T[longueur] != 0: 
        longueur += 1
    return longueur 

def pourcentageVOYELLES(T):
    i = 0
    nb_voyelles = 0
    while T[i] != 0: 
        if(T[i] == 'a' or T[i] == 'e' or T[i] == 'i' or T[i] == 'o' or T[i] == 'u' or T[i] == 'y'):
            nb_voyelles += 1
        i += 1
    pourcentage = (nb_voyelles/tailleCHAINE(T))*100
    return pourcentage 

def est_sous_chaîne(T, sous_chaine):
    trouve = False
    i = 0
    while T[i] != 0 and trouve == False:
        j = 0
        k = i
        while j < len(sous_chaine) and T[k] == sous_chaine[j]:
            j = j + 1
            k = k + 1
        if j == len(sous_chaine):
            trouve = True
        else:
            i = i + 1
    if trouve == True:
        return i
    else:
        print("Wagon n'est pas une sous-chaîne de T")
        return -1

def nombreOccurences(T, sous_chaine):
    nb_occurrences = 0
    i = 0
    while T[i] != 0:
        j = 0
        k = i
        while j < len(sous_chaine) and T[k] == sous_chaine[j]:
            j = j + 1
            k = k + 1
        if j == len(sous_chaine):
            nb_occurrences = nb_occurrences + 1
            i = k
        else:
            i = i + 1
    return nb_occurrences

T = ['m', 'a', 'w', 'a', 'n', 'e', 's', 't', 'w', 'a', 'g', 'o', 'n','w','a', 0]
print("Taille Chaîne : ", tailleCHAINE(T))
print("Pourcentage de Voyelles : ", pourcentageVOYELLES(T))
print("Début de la première occurrence : ", est_sous_chaîne(T, 'wagon'))
print("Nombre d'occurrences : ", nombreOccurences(T, 'wagon'))