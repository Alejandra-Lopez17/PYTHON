from functools import reduce


lista_numeros = [10, 15, 20, 25, 30, 35, 45, 50, 55, 60, 65, 75, 80, 85]

numeros = [1, 2, 3, 4]


def funcion_sumar(acumulador, elemento): return acumulador+elemento


suma_num = reduce(funcion_sumar, numeros)
print(suma_num)


'''
Imprimir los nombres de la lista separados por coma (,)
'''
nombres = ['andrés', 'Juan', 'juliana', 'cristian', 'jaime']


def concatenar(ac, e): return ac+', '+e


respuesta = reduce(concatenar, nombres)
print(respuesta)

'''
A partir de la lista de nombres imprima todos los nombres 
que empiezan por 'J' separados por coma. 
NOTA: Para el resultados final los nombres deben empezar en mayúscula
Algoritmo:
1) Filtrar la lista
2) Convertir iniciales a mayúsculas
3) Reducir la lista a String
'''
nombres = ['andrés', 'Juan', 'juliana', 'cristian', 'jaime']

nombres = tuple(filter(lambda n: n[0].lower() == "j", nombres))
nombres = list(map(lambda n: n.capitalize(), nombres))


def concatenar(ac, e): return ac+", " + e


respuesta = reduce(concatenar, nombres)
print(respuesta)
