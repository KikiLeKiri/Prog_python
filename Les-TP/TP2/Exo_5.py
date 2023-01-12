Nb_entier = int(input("Entrer un nombre entier :"))
if Nb_entier % 2 == 0 and Nb_entier > 0 :
    print("Le nombre est pair et positif")

if Nb_entier % 2 == 1 and Nb_entier > 0 :
    print("Le nombre est impair et positif")

if Nb_entier == 0 :
    print (" Le nombre est zéro et est pair")

if Nb_entier % 2 == 0 and Nb_entier < 0 :
    print("Le nombre est pair et négatif")

if Nb_entier % 2 == 1 and Nb_entier < 0 :
    print("Le nombre est impair et négatif")