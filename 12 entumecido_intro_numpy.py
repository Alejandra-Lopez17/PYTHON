import numpy as np


def guion(): return print('-----------------------------------------------------')


#Crear una matriz
matriz = np.array([[10, 20], [30, 40]])
print(matriz)

guion()

matriz_flotante = np.array([[10, 20], [30, 40.2]])
print(matriz_flotante)

guion()
matriz_string = np.array([[10, 20], [30.2, '40']])
print(matriz_string)

guion()

lista_n1 = [10, 80, 20, 50, 60]
lista_n2 = [90, 150, 40, 10, 40]
lista_n = lista_n1 + lista_n2
guion()

matriz_n1 = np.array(lista_n1)
matriz_n2 = np.array(lista_n2)

sumatoria = matriz_n1 + matriz_n2
print(sumatoria)
matriz_suma = np.add(matriz_n1, matriz_n2)
print(matriz_suma)

guion()
print('Resta')
guion()
matriz_resta = matriz_n1 - matriz_n2
print(matriz_resta)
matriz_resta = np.subtract(matriz_n1, matriz_n2)
print(matriz_resta)

guion()
print('Dividir')
guion()
matriz_division = matriz_n1 / matriz_n2
print(matriz_division)

guion()
print('Multiplicar')
guion()

multiplicacion_elemento_x_elemento = matriz_n1 * matriz_n2
print(multiplicacion_elemento_x_elemento)

guion()
print('Multiplicación de matrices')
guion()
matriz_1 = np.array([[1, 2, 3], [4, 5, 2]])
matriz_2 = np.array([[5, 2], [1, 3], [2, 4]])
matriz_multiplicacion = np.dot(matriz_1, matriz_2)
print(matriz_multiplicacion)
