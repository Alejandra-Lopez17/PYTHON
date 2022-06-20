
from functools import reduce


nombres = ['Juan', 'Juliana', 'María', 'Jaime']
apellidos = ['Quintana', 'Torres', 'Hernandez', 'Medina']

relacion_nombres_apellidos = set(zip(nombres, apellidos))
#print(relacion_nombres_apellidos)

lista_1 = [10, 20, 30, 40, 50, 60, 70, 80, 90]
lista_2 = [90, 80, 70, 60, 50, 40, 30, 20, 10]
lista_tuplas = list(zip(lista_1, lista_2))
print(lista_tuplas)
suma = list(map(lambda tupla: tupla[0]+tupla[1], lista_tuplas))
resultado = reduce(lambda ac, e: ac+e, suma)
print(resultado)
