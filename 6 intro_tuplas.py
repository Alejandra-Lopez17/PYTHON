""" 
numeros = [1,2,3,4]
numeros[0] = 10
print(numeros)
 """
tupla = tuple()
tupla = (1, 2, 3, 4)

n1 = tupla[1]
print(n1)
#No es válido
#tupla[0] = 10

miTupla = ("Andres",)
print(miTupla)

nombres = "Andres", "Juan", "María", "Karol"
print(nombres)

n1, n2, n3, n4 = nombres
print(n1)
print(n2)


for t in nombres:
    print(t)
'''
Una tupla es inmutable
'''
