            #exo5 : Déterminer le coureur le plus rapide
print("Coureur 1:")
NAME1 = str(input("NOM :"))
Time1 = float(input("Time in second :"))
print("Coureur 2:")
NAME2 = str(input("NOM :"))
Time2 = float(input("Time in second :"))

if(Time1<Time2):
    print(NAME1," est plus rapide")
else:
    if(Time1>Time2):
     print(NAME2," est plus rapide")
    else:
       print("Les deux coureurs ",NAME2,"et",NAME1," ont le meme temps")

       
