fin_loc = False
while fin_loc == False :
    heure_debut = int(input("Donnez l’heure de début de la location (un entier) :"))
    heure_fin = int(input("Donnez l’heure de fin de la location (un entier) :"))
    tarif_1 =0
    tarif_2 =0
    i = heure_debut
    if heure_debut < 0 or heure_fin > 24 :
        print("Les heures doivent être comprises entre 0 et 24 !\n")
    elif heure_debut == heure_fin:
        print("Attention ! L’heure de fin est identique à l’heure de début.\n")
    elif heure_fin < heure_debut:
        print("Attention ! Le début de la location est après la fin ... \n")
    else:
        for i in range(heure_debut,heure_fin):
            if (0<=i and i<=7) or (17<=i and i<=24):
                tarif_1 += 1
                i += 1
            elif (7<i and i<17):
                tarif_2 += 1
                i += 1
        total = tarif_1 + tarif_2*2
        print("Vous avez loué votre vélo pendant")
        if tarif_1 != 0:
            print(tarif_1," Heure(s) au tarif horaire de 1.0 euro(s)")
        if tarif_2 != 0:
            print(tarif_2," Heure(s) au tarif horaire de 2.0 euro(s)")
        print("Le montant total à payer est de ",total," euro (s).")
        fin_loc = True