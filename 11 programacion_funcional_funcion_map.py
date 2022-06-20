
lista_numeros = [10, 20, 30, 40, 50, 60, 70, 80]

respuesta = list(map(lambda n: n**2, lista_numeros))
print(respuesta)

print(list(map(lambda n: f'{n}', lista_numeros)))

'''
Retornar una lista con la inicial de cada nombre en mayúscula
'''
nombres = ['andrés', 'juan', 'juliana', 'cristian', 'jaime']

respuesta = list(map(lambda n: n.capitalize(), nombres))
print(respuesta)
