
listaVacia = list()

listaVacia = []

miLista = [10, 3.14, ""]

nombres = ["Juan", "Andrés", "María", "Ana", "Jorge"]

for n in nombres:
    print(n)

nombres.append("Jose")

print('-------------')

for n in nombres:
    print(n)

#Elimina el último elemento
nombres.pop()

print(nombres)
print('-------------')

#Eliminar un elemento en una pocision en especifico
nombres.pop(1)
print('-------------')
print(nombres)

for n in range(10, 100):
    print(n)


'''
1) Crear una lista con números pares del 1 al 1000
2) Crear una lista con número impares del 1 al 1000
'''

lista_pares = list()
lista_impares = list()

for n in range(1, 1001):
    if n % 2 == 0:
        lista_pares.append(n)
    else:
        lista_impares.append(n)

print(lista_pares)
print(lista_impares)
