AGE1 = int(input("Entrez svp l'age de la 1ere personne = "))
AGE2 = int(input("Entrez svp l'age de la 2eme personne = "))

if(AGE1 <AGE2):
    print("la 2eme personne avec l'age de", AGE2," ans est plus agée ")
else:
    if(AGE1 > AGE2):
     print("la 1ere personne avec l'age de", AGE1," ans est plus agée ")
    else:
        print("Les deux personnes ont le meme age : ",AGE1 ,"ans")



   