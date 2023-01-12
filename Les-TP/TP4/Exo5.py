date = input("Entrez une date (au format JJMMAAAA) : ")
jour = int(date[0:2])
mois = int(date[2:4])
annee = int(date[4:8])

print(jour,mois,annee)

if mois < 1 or mois > 12:
    print("Date invalide ! Veuillez saisir un mois correct.")
elif mois in [1,3,5,7,8,10,12] and jour < 1 or jour > 31:
    print("Date invalide ! Veuillez saisir un jour correct.")
elif mois in [4,6,9,11] and jour < 1 or jour > 30:
    print("Date invalide ! Veuillez saisir un jour correct.")
elif mois == 2 and jour < 1 or jour > 29:
    print("Date invalide ! Veuillez corriger votre saisie.")
elif mois == 2 and jour == 29 and annee % 4 != 0:
    print("Date invalide ! Veuillez corriger votre saisie.")
else:
    print("La date saisie est valide.")