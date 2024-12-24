              #Exo2 Vérification de la température
Temp = int(input("Entrez la température : "))
if (Temp <0):
    print("il fait tres froid !")
else:
    if(Temp<10) and (Temp>0):
        print("il fait froid !")
    else:
        if(Temp>10):
            print("il fait frais !")
print("Soyez prudent")