
nombres = ['Andrés', 'María', 'Juan', 'Juliana', 'Jorge', 'Jose', 'jairo']
# ['NULL', 'NULL', 'JUAN', 'JULIANA']

respuesta = [n.upper() if n[0].lower() == 'j' else n.lower() for n in nombres]

print(respuesta)

""" lista = []
for n in nombres:
    if n[0].lower()=='j':
        lista.append( n.upper() )
    else:
        lista.append( n.lower() ) """


def funcion(lista_nombres): return [
    n.upper() if n[0].lower() == 'j' else n.lower() for n in lista_nombres]


print(funcion(nombres))


'''
1) Obtener una lista con los nombres que empiecen en 'J' ponerlos en mayúscula,
    de lo contrario almacenar un string como 'NULL'
    Ejemplo:
    ['Andrés', 'María','Juan', 'Juliana']
    ['NULL', 'NULL', 'JUAN', 'JULIANA']

2) Desarrolle una función que reciba como parámetro una lista de números,
    retorne una lista con los números pares elevados al cuadrado y 
    los números impares elevados al cubo
'''

#Punto #1


def funcion(nombres): return [
    n.upper() if n[0].lower() == 'j' else 'NULL' for n in nombres]


print(funcion(['Andrés', 'María', 'Juan', 'Juliana']))

#Punto #2
#Solución de Juan Carlos


def funcion(lista): return [n**2 if n % 2 == 0 else n**3 for n in lista]


print(funcion([2, 3, 4, 5, 6, 7, 8]))


print('---------UTILIZANDO MAP Y FILTER---------')


def funcion(lista): return list(
    map(lambda n: n**2, list(filter(lambda n: n % 2 == 0, lista))))


print(funcion([2, 3, 4, 5, 6, 7, 8]))
