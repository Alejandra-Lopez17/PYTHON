'''
List Comprehension
'''

numeros = [10, 20, 30, 40, 50, 60, 70, 80, 90]

numeros_al_cuadrado = [n**2 for n in numeros]
print(numeros_al_cuadrado)

""" lista = []
for n in numeros:
    lista.append(n**2) """


def funcion(lista): return [n/2 for n in lista]

#print( funcion(numeros_al_cuadrado) )


numeros = [10, 20, 30, 40, 50, 60, 70, 80,
           90, 15, 25, 35, 45, 55, 65, 75, 85, 95]
numeros_pares = [n for n in numeros if n % 2 == 0]
print(numeros_pares)

numeros_impares = [n for n in numeros if n % 2 != 0]
print(numeros_impares)
