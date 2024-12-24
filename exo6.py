                     #exo6 : Séparation des dinars et des centimes
NOMBRE = float(input("Le nombre = "))
Partie_entiere = int(NOMBRE)
partie_decimale = int((NOMBRE - Partie_entiere)*100)
if(partie_decimale <50):
    partie_decimale = partie_decimale+1

print("partie entiere = ",Partie_entiere)
print("partie decimale = ",partie_decimale)
