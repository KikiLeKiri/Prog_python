liste = [1, 2, 3, 3, 4, 4, 4, 5, 5, 5, 5]

occurrences_max = 0

element_frequent = 0

for i in liste:
    occurrences = liste.count(i)
    if occurrences > occurrences_max:
        occurrences_max = occurrences
        element_frequent = i

print("L'élément le plus fréquent est", element_frequent, "avec", occurrences_max, "occurrences.")