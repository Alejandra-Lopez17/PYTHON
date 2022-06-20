from numpy import random as r


def crear_baraja(id_cartas: list):
    corazones = list(map(lambda id: (id, '♥︎'), id_cartas))
    diamantes = list(map(lambda id: (id, '♦︎'), id_cartas))
    trebol = list(map(lambda id: (id, '♣︎'), id_cartas))
    picas = list(map(lambda id: (id, '♠︎'), id_cartas))
    #Unir las listas en una sola baraja
    baraja = corazones+diamantes+trebol+picas
    #Barajar cartas
    r.shuffle(baraja)
    return baraja


def repartir_cartas(baraja: list):
    carta_1 = baraja.pop()
    carta_2 = baraja.pop()
    return carta_1, carta_2


id_cartas = ['A', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K']
baraja = crear_baraja(id_cartas)


def jugar():
    print('-------------POKER---------')
    num_jugadores = int(input('Por favor ingrese el número de jugadores: '))
    #
    jugadores = dict()
    for j in range(num_jugadores):
        jugadores[f'jugador{j+1}'] = list(repartir_cartas(baraja))

    print(jugadores)


jugar()
