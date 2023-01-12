value = int(input("Entrer une valeur Supérieur a 1 : "))
if value > 1:
    i = 0
    somme = 0
    while somme < value:
        i += 1
        somme += i+1
    print("Le plus grand nombre N est : ",i)



