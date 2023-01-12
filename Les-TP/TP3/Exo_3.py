import random 
x = random.randint(0,100)
print(x)
Devine = int(input("Trouver le chiffre compris entre 0 et 100 : "))
compteur = 0
while x != Devine :
    if Devine < x : 
        print("Trop petit !")
        compteur+=1
        int(input("Trouver le chiffre compris entre 0 et 100 : "))
    if Devine > x :
        compteur+=1
        print("Trop Grand !")
        int(input("Trouver le chiffre compris entre 0 et 100 : "))
    else :
        print ("Gagné !")
        break
print("Vous vous êtes trompé",compteur,"fois")