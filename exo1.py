          #Exo1 Système d'achat de billets

Nom = input ("Entrez votre nom s'il vous plait : ")
if(Nom == "VIP")or (Nom == "vip"):{
    print("Profitez de vos billets gratuit ")
}
else:
    Billet = int(input ("Combien de billets voulez_vous achetez ? "))
    Billet = Billet * 15.50
    print("Cela vous coute :",Billet,"\nProfitez de vos tickets",Nom)


