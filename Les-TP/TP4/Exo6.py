liste = [5, 2, 4, 8, 1, 3]

def tri_selection(liste): 
    for i in range(0, len(liste)): 
        indice_min = i 
        for j in range( i + 1, len(liste)): 
            if liste[indice_min] > liste[j]: 
                indice_min = j 
        liste[i], liste[indice_min] = liste[indice_min], liste[i]
        print(liste)


print("Liste avant tri : ", liste) 
tri_selection(liste) 
print("Liste après tri : ", liste)

