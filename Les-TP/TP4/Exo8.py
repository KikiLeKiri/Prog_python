mon_dico = {
    "Prénom": "Kilian",
    "Nom": "ROHFRITSCH",
    "Promo": "2022-2023",
    "Groupe": "RT111",
}
print("Votre nom est", mon_dico["Nom"], "prénom est ",mon_dico["Prénom"], "vous faites partie de la promo", mon_dico["Promo"], "dans le groupe ",mon_dico["Groupe"])

print ("Les clées du dico sont : ")
for elt in mon_dico.keys():
    print("-", elt)

print ("Les valeurs du dictionnaire sont : ")
for element in mon_dico.values():
    print ("-", element)

print ("Les tuplets du dictionnaire sont : ")
for tuplets in mon_dico.items():
    print ("-", tuplets)

dico_voisin = {
    "Prénom": "Valentin",
    "Nom": "TORRES",
    "Promo": "2022-2023",
    "Groupe": "RT112",
}

binome = {
    "id1" : mon_dico,
    "id2" : dico_voisin,
}

print ("Les étudiants formants le binôme sont : ")
print ("- L'étudiant", binome["id1"]["Nom"], binome["id1"]["Prénom"],"du groupe", binome["id1"]["Groupe"])
print ("- L'étudiant", binome["id2"]["Nom"], binome["id2"]["Prénom"],"du groupe", binome["id2"]["Groupe"])