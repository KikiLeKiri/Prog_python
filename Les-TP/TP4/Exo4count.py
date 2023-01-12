liste = [1, 5, 2, 8, 2, 4, 2, 5, 2, 5, 9, 8, 2, 5, 9]

element_max = liste[0]
occurrences_max = 1

for i in range(len(liste)):
    occurrences = 1
    for j in range(i+1, len(liste)):
        if liste[i] == liste[j]:
            occurrences += 1
    if occurrences > occurrences_max:
        element_max = liste[i]
        occurrences_max = occurrences

print("L'élément le plus fréquent est : ", element_max)
print("Nombre d'occurrences : ", occurrences_max)