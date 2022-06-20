
from functools import reduce

nombres = ['Cristian', 'Jorge', 'María']


def obtener_inicial(string): return string[0]


iniciales = list(map(obtener_inicial, nombres))
print(iniciales)


def sumar(concatenar, letra):
    return concatenar+letra


cadena = reduce(lambda concatenar, letra: concatenar+letra,  iniciales)
print(cadena)

concatenar = ''
for i in iniciales:
    concatenar += i
print(concatenar)
