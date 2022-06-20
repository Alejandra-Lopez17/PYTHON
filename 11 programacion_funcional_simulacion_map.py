

def simulacion_map(funcion, lista):
    respuesta = []
    for n in lista:
        num = funcion(n)
        respuesta.append(num)

    return respuesta


def elevar(n): return n**2


#Elevar al cuadrado todos los números de la lista
lista_numeros_1 = [10, 20, 30, 40, 50, 60, 70, 80]
lista_numeros_2 = [20, 5, 15, 40, 50, 60, 70, 80]
lista_principal = [lista_numeros_1, lista_numeros_2]

for lista in lista_principal:
    print(simulacion_map(elevar, lista))
