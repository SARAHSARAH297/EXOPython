                #exo12 :Rectangle de hachages

largeur = int(input("LARGEUR = "))
hauteur = int(input("HAUTEUR = "))
i = 0

while i < hauteur:
    j = 0 
    while j < largeur:
        print("#", end="")  
        j += 1
    print() #saut de ligne 
    i += 1


