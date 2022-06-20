

from functools import reduce


ventas = [
    [1201, ("5464", 4, 25842.99), ("7854", 18, 23254.99), ("8521", 9, 48951.95)],
    [1202, ("8756", 3, 115362.58), ("1112", 18, 2354.99)],
    [1203, ("2547", 1, 125698.20), ("2635", 2, 135645.20),
     ("1254", 1, 13645.20), ("9965", 5, 1645.20)],
    [1204, ("9635", 7, 11.99), ("7733", 11, 18.99), ("88112", 5, 390.95)]
]

""" def obtener_totales(ventas):
    dict_respuesta = dict()
    for lista in ventas:
        #Sacar el id de la lista
        id = lista.pop(0)
        #Mapear la lista de tuplas
        lista_totales = list(map(lambda tupla: tupla[1]*tupla[2],  lista))
        #Sumar los totales
        total = reduce( lambda suma, e: suma+e, lista_totales )
        #añadir datos al diccionario
        dict_respuesta[id] = round(total, 2)
    
    return dict_respuesta """

#print(obtener_totales(ventas))


def obtener_totales(ventas):
    dict_respuesta = dict()
    for lista in ventas:
        #Sacar el id de la lista
        id = lista.pop(0)
        #Mapear la lista de tuplas
        #Sumar los totales
        total = reduce(lambda suma, e: suma+e,
                       list(map(lambda tupla: tupla[1]*tupla[2], lista)))
        #añadir datos al diccionario
        dict_respuesta[id] = round(total, 2)

    return dict_respuesta


print(obtener_totales(ventas))
