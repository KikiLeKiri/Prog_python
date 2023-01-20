total = 0
coeff_total = 0

for i in range(5):
    print("Veuillez entrer la note du module {} et le coefficient correspondant :".format(i+1))
    note, coeff = map(float, input().split())
    total += note * coeff
    coeff_total += coeff

moyenne = total/coeff_total

if moyenne > 10 and note > 8 :
    print("Admis")
else:
    print("Refusé")
print("La moyenne est de :", moyenne)

