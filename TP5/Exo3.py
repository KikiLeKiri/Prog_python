Entree = input('Veuillez entrer une chaine de caractères : ')
palindrome='' 
for i in Entree.lower():
    if i.isalpha():
        palindrome += i

longueur = len(palindrome) 
i=0 

estPalindrome = True 
while i < longueur and estPalindrome : 
    if palindrome[i] != palindrome[-(i+1)]:
        estPalindrome = False 
        i += 1
    else:
        estPalindrome = True
        break


if estPalindrome:
    print("La chaîne",palindrome ,"est un palindrome !")
else:
    print("La chaîne",palindrome ,"n'est pas un palindrome.")