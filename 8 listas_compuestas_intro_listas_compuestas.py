
hijo_1 = ['Sebastián', 'Alejandra']
hijo_2 = ['Juan', 'Andrea']

padre = [hijo_1, hijo_2, ['Samir', 'María']]

print(padre)
print(padre[0])

nombre_1 = padre[0][0]
print(nombre_1)

nombre_2 = padre[0][1]
print(nombre_2)

nombre_3 = padre[1][0]
print(nombre_3)

nombre_4 = padre[1][1]
print(nombre_4)

print('\n-----------------------\n')

for hijo in padre:
    #Iterar los hijos
    for n in hijo:
        print(n)
