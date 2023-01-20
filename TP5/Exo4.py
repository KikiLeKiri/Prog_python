def rendre_monnaie(prix_article, montant_versé):
    monnaie = montant_versé - prix_article
    cent = 0
    cinquante = 0
    dix = 0
    deux = 0
    un = 0
    
    if monnaie // 100 > 0:
        cent = monnaie // 100
        monnaie %= 100
    if monnaie // 50 > 0:
        cinquante = monnaie // 50
        monnaie %= 50
    if monnaie // 10 > 0:
        dix = monnaie // 10
        monnaie %= 10 
    if monnaie // 2 > 0:
        deux = monnaie // 2 
        monnaie %= 2 
    if monnaie // 1 > 0:
        un = monnaie // 1
        monnaie %= 1 
    print("Rendu :",cent,"pièces de 100€",cinquante,"pièces de 50€", dix, "pièces de 5€,", deux, "pièces de 2€ et", un, "pièce de 1€.")

rendre_monnaie(15, 586)
