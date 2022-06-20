
estudiante_1 = {
    'nombre': 'Andrés',
    'edad': 20,
    'notas': {
        'nota_1': 3.5,
        'nota_2': 4.2,
        'nota_3': 4.8
    }
}

notas_estudiantes = {
    '1234': estudiante_1,
    '9876': {
        'nombre': 'Alejandra',
        'edad': 24,
        'notas': {
            'nota_1': 3.2,
            'nota_2': 4.5,
            'nota_3': 4.4
        }
    },
    '1155': {
        'nombre': 'Sebastián',
        'edad': 24,
        'notas': {
            'nota_1': 4.2,
            'nota_2': 2.5,
            'nota_3': 3.4
        }
    },
    '2244': {
        'nombre': 'Ana Milena',
        'edad': 28,
        'notas': {
            'nota_1': 4.1,
            'nota_2': 2.8,
            'nota_3': 3.8
        }
    }
}

'''
* Desarrollar una función que reciba como parámetro el diccionario
    notas_estudiante. La función debe retornar un diccionario que 
    contenga el promedio de notas de cada estudiante
'''


def calcular_promedio_notas(notas_est: dict):
    # Diccionario que almacena el promedio de notas
    dict_promedio_estudiante = dict()  # Crea un diccionario vacío

    # Recorrer diccionario padre (notas_est)
    for estudiante in notas_est.values():
        # Imprimir el nombre del estudiante
        # print(estudiante['nombre'])
        nombre = estudiante['nombre']
        # Obtener el diccionario de notas del estudiante
        notas = estudiante['notas']
        # variable que representa el promedio de notas de cada estudiante
        promedio = 0
        # Recorrer diccionario hijo de cada estudiante (notas)
        # For anidado
        for n in notas.values():
            # sumar las notas
            promedio += n
            # Imprimir notas
            # print(n)
        # Obtener el tamaño del diccionario notas
        cant_notas = len(notas)
        #print("Cantidad de notas-> ", cant_notas)
        promedio /= cant_notas
        # Redondear a dos cifras: round(numero_a_redondear, cantidad_de_decimales)
        #print("Promedio: ", round(promedio, 1))
        # Añadir promedio del estudiante al diccionario dict_promedio_estudiante
        dict_promedio_estudiante[nombre] = round(promedio, 1)

    return dict_promedio_estudiante


print(calcular_promedio_notas(notas_estudiantes))
