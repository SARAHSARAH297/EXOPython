                #exo9 : Longueur du nom Kingdom
LISTE = []
i = 0
while True:
    name = input("Nom de la ville = ")
    if name == "stop":
        break
    LISTE.append(name)
    i += 1
j=0
print("\n")
for j in range(i) :
    taille = len(LISTE[j])
    taille = taille * 1_000_000
    print("La population de la ville :", LISTE[j], "égale à :",taille)



