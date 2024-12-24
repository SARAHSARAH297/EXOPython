                 #exo10: Exercice : Vérification du palindrome
MOT = input("Veuillez entrer un mot : ")
j = len(MOT) 
is_palindrome = True 

for i in range(j // 2): 
    if MOT[i] != MOT[j - 1 - i]:  
        is_palindrome = False 
        break

if is_palindrome:
    print("Le mot est un palindrome")
else:
    print("Le mot n'est pas un palindrome")
