condition = ""

if condition == True:
    print("Es True")
elif condition == False:
    print("Es False")
else:
    print("Condicion no reconocida")

lista = [i for i in range(2, 10 + 1) if i % 2 == 0]
print(lista)
