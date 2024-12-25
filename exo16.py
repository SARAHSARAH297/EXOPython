                          #exo16: Mutabilité dans les listes
TAB = [1,2,3,4,5]
index=0
while index != -1:
    index = int(input("veuillez entrer l'index (-1 pour quitter) : "))
    if index ==-1:
        break
    valeur = int(input("veuillez entrer la valeur : "))
    TAB[index]=valeur
    print(TAB)
    
