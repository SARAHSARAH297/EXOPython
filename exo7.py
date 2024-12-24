          #Exercice sur les années bissextiles

ANNEE = int(input("veuillez saisir une année :"))
if((ANNEE % 4)==0)and((ANNEE % 100)!=0) :
    print("l'année est bissextile")
else:
    if(((ANNEE % 100)==0)) and ((ANNEE % 400)==0):
        print("l'année est bissextile")
    else:
        print("l'année n'est pas bissextile")


