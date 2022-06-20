
miDiccionario = {
    'estudiante': 'David Calle',
    'edad': 20,
    'activo': True,
    'promedio_nota': 4.5
}

estudiante = miDiccionario['estudiante']
print(estudiante)

x = miDiccionario['edad']
print(x)

#--------------------------------------------
estudiante_1 = {
    'nombre': 'Andrés',
    'edad': 20,
    'notas': {
        'nota_1': 3.5,
        'nota_2': 4.2,
        'nota_3': 4.8
    }
}
estudiante_2 = {
    'nombre': 'Alejandra',
    'edad': 24,
    'notas': {
        'nota_1': 3.2,
        'nota_2': 4.5,
        'nota_3': 4.4
    }
}
notas_estudiantes = {
    '12345678': estudiante_1,
    '98765432': estudiante_2
}

print(notas_estudiantes['12345678'])


supermercado = {
    'belen': {
        'aseo': 12000000,
        'frutas': 24000000
    },
    'estadio': {
        'aseo': 10000000,
        'frutas': 8000000
    }
}

'''
* Calcular el promedio de ventas de cada sede
* Calcular el total de ventas de todas las sedes
'''
sede_belen = supermercado['belen']
ventas_belen = sede_belen['aseo']
ventas_belen += sede_belen['frutas']
promedio_ventas_belen = ventas_belen/2

sede_estadio = supermercado['estadio']
ventas_estadio = sede_estadio['aseo']
ventas_estadio += sede_estadio['frutas']
promedio_ventas_estadio = ventas_estadio/2

total_ventas = ventas_belen + ventas_estadio

mensaje_ventas = 'PROMEDIO DE VENTAS:\n'
mensaje_ventas += f'Sede belén: ${promedio_ventas_belen}\n'
mensaje_ventas += f'Sede estadio: ${promedio_ventas_estadio}\n'
mensaje_ventas += 'TOTAL VENTAS:\n'
mensaje_ventas += f'{total_ventas}'

print(mensaje_ventas)

print("-----------------------------------------------------------")

#Declarar un diccionario vacío
diccionario = dict()
#diccionario = {}

#Añadir elementos a un diccionario

diccionario['estudiante_1'] = {
    'nombre': 'Franklin',
    'apellido': 'Castaño',
    'activo': True
}

print(diccionario)

diccionario['estudiante_2'] = {
    'nombre': 'Erika',
    'apellido': 'Delgado',
    'activo': False
}
print(diccionario)

print('Estudiante 2:\n', diccionario['estudiante_2'])

diccionario['estudiante_2']['activo'] = True
print('Estudiante 2:\n', diccionario['estudiante_2'])
