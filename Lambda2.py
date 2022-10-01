numeros = [12,1,2,32,312,33,2,15,65]
mayora10 = lambda numero: numero>10

for i in numeros:
    if (mayora10(i)):
        print(f'{i} es mayor a 10')
    else:
        print(f'{i} es menor a 10')