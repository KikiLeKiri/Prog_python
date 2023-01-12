from time import sleep
Nombre = int(input("Entrez un nombre :"))
for i in range (0,Nombre):
    Nombre -=1
    print(Nombre)
    sleep(0.2)

while Nombre != 0 :
    Nombre -=1
    print(Nombre)
    sleep(0.2)