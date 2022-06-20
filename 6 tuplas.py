
def pares_impares(inicio, fin):
    pares = list()
    impares = list()
    for n in range(inicio, (fin+1)):
        if n % 2 == 0:
            pares.append(n)
        else:
            impares.append(n)
    #Retornar listas dentro de una tupla
    return (pares, impares)


#print( pares_impares(1, 100) )
pares, impares = pares_impares(1, 10)

print(pares)
print(impares)


tupla = ("Juan", "María", 'Jorge', 'Samir')
