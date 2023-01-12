##########################  EXO :  A 

x = int(input("Entrez un entier : "))
s = 0
for i in range(x):
    s += x
    x -= 1
print(s)

########################### EXO : B

val = 0
while val != 100 :
    val = int(input("Entrez une valeur : "))


########################### EXO C

inf10 = 0
sup10_inf15 = 0
sup15 = 0
for i in range (0,10):
    value = float(input("Entrer une valeur comprise entre 0 et 20 : "))
    while (value > 20) or (value< 0):
        value = float(input("Erreur Entrer une valeur comprise entre 0 et 20 : "))
    if value < 10:
        inf10 += 1
    elif (value >= 10) and (value < 15):
        sup10_inf15 += 1
    elif value >= 15:
        sup15 += 1
print("Nombre de valeur inférieur a 10 :",inf10)
print("Nombre de valeur supérieur ou égale a 10 et inférieur a 15 :",sup10_inf15)
print("Nombre de valeur supérieur ou égale a 15 : ",sup15)


############################### EXO D

value = int(input("Entrer une valeur Supérieur a 1 : "))
if value > 1:
    i = 0
    somme = 0
    while somme < value:
        i += 1
        somme += i+1
    print("Le plus grand nombre N est : ",i)
