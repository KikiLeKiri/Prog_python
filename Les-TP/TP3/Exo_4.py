n = int(input("Entrez un nombre : "))
Choix = int(input("Choisisez la boucle que vous voulez : 1 pour FOR et 2 pour WHILE : "))
x = 1
if Choix == 1 :
    for i in range(1,n+1):
        x = x*i
    print(x)
else: 
    while n > 1:
        x = n * x
        n -=1
    print(x)

