                   #exo14 : Mot encadré 
TEXTE = input("Veuillez entrer un mot : ")

i = len(TEXTE)
etoile = 30
vide = (etoile - i - 2) // 2 

print("*" * etoile)
print("*" + " " * vide + TEXTE + " " * (etoile - i - 2 - vide) + "*")
print("*" * etoile)



    
    

