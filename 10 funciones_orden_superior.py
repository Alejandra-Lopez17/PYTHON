
from math import sqrt


def funcion_orden_superior(sumar):
    print(sumar(60, 40))


def sumar(n1, n2):
    return n1+n2


referencia_sumar = sumar
otra_referencia = referencia_sumar
ultima_referencia = otra_referencia
#print(referencia_sumar(40,50))
#funcion_orden_superior(sumar)


def mapear_datos(funcion, lista_numeros: list) -> list:
    respuesta = []
    for num in lista_numeros:
        x = funcion(num)
        respuesta.append(x)
    return respuesta

#Fabrica de funciones sobre un mismo número
#Retorna una función que recibe un solo parámetro de tipo numérico


def fabricar_operacion(operador):
    def respuesta(
        n): return f'No existe la operación para n con operación {operador}'
    #Evaluar el operador
    if operador == '**2':
        def respuesta(n): return n**2
    elif operador == 'sqrt':
        #Raíz cuadrada
        def respuesta(n): return sqrt(n)
    elif operador == '/2':
        def respuesta(n): return n/2
    return respuesta


numeros = [4, 20, 30, 40, 50, 60, 70, 80]
operacion = fabricar_operacion('/2')
respuesta = mapear_datos(operacion, numeros)
print(respuesta)


'''
1) Desarrolle un función que retorne una lista con las iniciales de cada string a partir
    de una lista de strings. Para esto utilice el concepto de funciones de orden superior y
    funciones anónimas
'''

nombres = ['Juliana', 'Pedro', 'María', 'Juan Carlos', 'Andrés', 'Alejandra']
'''
['J, 'P',...]
'''


def lista_nombre(obtener_inicial, nombres) -> list:
    respuesta = []
    for n in nombres:
        x = obtener_inicial(n)
        respuesta.append(x)
    return respuesta

#obtener_inicial = lambda cadena: cadena[0]


def obtener_inicial(cadena):
    return cadena[0]


lista_iniciales = lista_nombre(obtener_inicial, nombres)
print(lista_iniciales)


ejercicio_2 = "2) Desarrolle una función que reciba como parámetro una lista de string,\n"
ejercicio_2 += "retorne una lista de tuplas donde cada tupla representa a cada string\n"
ejercicio_2 += "de la lista inicial.\n"
ejercicio_2 += "nombres = ['Andrés', 'María']\n"
ejercicio_2 += "retornar: [ ('A', 'n', 'd', 'r', 'e', 's'), (...) ]\n"
print(ejercicio_2)


nombres = ['Andrés', 'María']
n1 = nombres[0]
""" print(n1)
tupla_n1 = tuple(n1)
print(tupla_n1)
lista_tupla = [tupla_n1]
print(lista_tupla)

n2 = nombres[1]
n2 = tuple(n2)
lista_tupla.append(n2)
print(lista_tupla) """


def iterar_lista(convertir, lista: list):
    respuesta = []
    for n in lista:
        tupla = convertir(n)
        respuesta.append(tupla)
    return respuesta


def convertir_a_tupla(cadena): return tuple(cadena)


respuesta = iterar_lista(convertir_a_tupla, nombres)
print(respuesta)

print(iterar_lista(lambda cadena: set(cadena), nombres))
