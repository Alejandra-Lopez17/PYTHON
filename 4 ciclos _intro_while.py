
incremental = 0

while incremental < 10:
    #print(incremental)
    incremental += 1


incremental = 0
while True:
    #print(incremental)
    if incremental == 1000:
        #break -> Rompe el ciclo
        break
    incremental += 1

print('Fin while 1')

incremental = 0
while incremental != 1001:
    #print(incremental)
    incremental += 1

'''
1) Desarrolle un programa que imprima todos los numeros impares del 1 al 1000
'''

numero = 1
while numero <= 1000:
    if numero % 2 != 0:
        print(numero)
    numero += 1

'''
1) Uso del input ✔
2) Construcción de un menú utilizando inputs ✔
3) Listas
4) Tuplas
5) Conjuntos
6) CRUD utilizando diccionarios
'''
