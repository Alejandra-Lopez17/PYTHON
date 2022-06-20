
lista_numeros = [10, 15, 20, 25, 30, 35, 45, 50, 55, 60, 65, 75, 80, 85]


def funcion_pares(n): return n % 2 == 0


print(list(filter(funcion_pares, lista_numeros)))


nombres = ['andrés', 'Juan', 'juliana', 'cristian', 'jaime']

nombres_x_j = tuple(filter(lambda n: n[0].lower() == 'j', nombres))
nombres_x_j = list(map(lambda n: n.capitalize(), nombres_x_j))
print(nombres_x_j)

'''
A partir de la lista de 'nombres' retorne una lista con las iniciales 
de todos los nombres.
    Ejemplo:
    ['andrés','Juan','juliana','cristian','jaime']
    ['a','J','j','c','j']
'''
respuesta = list(map(lambda n: n[0], nombres))
print(respuesta)
