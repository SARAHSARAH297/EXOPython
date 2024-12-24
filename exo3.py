               #exo3 Calcul de remise

Montant = int(input("Entrez le montant totale d'un achat = "))
Article = int(input("Entrez le nombre d'article = "))
Jour = str(input("quel jour on est ?? = "))
# la 1ere lettre de Samedi et Dimanche doivent etre en majuscule
if(Jour =="Samedi") or (Jour =="Dimanche"):
    remise= Montant *0.20
    N_Montant = Montant -remise
else:
    remise= Montant *0.10
    N_Montant = Montant -remise
if(Article > 5):
    remise=Montant*0.05
    N_Montant = N_Montant -remise


print("Le prix totale apres remise = ",N_Montant)
    

