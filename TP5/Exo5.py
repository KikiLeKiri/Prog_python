heures_travaillées = int(input("Saisissez le nombre d'heures travaillées : "))
salaire_horaire = float(input("Saisissez le salaire horaire : "))

if heures_travaillées <= 160:
    salaire_net = heures_travaillées * salaire_horaire
elif heures_travaillées > 160 and heures_travaillées <= 200:
    salaire_net = (160 * salaire_horaire) + ((heures_travaillées - 160)*salaire_horaire*1.25)
elif heures_travaillées > 200:
    salaire_net = (160 * salaire_horaire) + ((40)*salaire_horaire*1.25) + ((heures_travaillées - 200)*salaire_horaire*1.50)

print("Le salaire net à payer est de :", salaire_net, "euros.")