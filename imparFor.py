#imparse, se for ele puxa com .append(var)
numeros = [1,2,3,4,5]
pares = []
for numero in numeros:
    if numero % 2 !=0:
     pares.append(numero)
print(pares)