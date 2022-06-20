
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

for estudiante in notas_estudiantes:
    valor = notas_estudiantes[estudiante]
    print(valor)

#clave: valor
usuarios = {
    'usu_1': 'Roko',
    'usu_2': 'Andres',
    'usu_3': 'Ana',
    'usu_4': 'Erika'
}

#Iterar y acceder a las claves del diccionario
for x in usuarios:
    print(x)
    dictUsu = usuarios[x]
    #print(dictUsu)


print("-----------------------------------------------------------")


#Iterar y acceder al valor del diccionario
for valor in usuarios.values():
    print(valor)


print("-----------------------------------------------------------")


#Itrar y obtener clave-valor
for clave, valor in usuarios.items():
    print("Clave: ", clave)
    print("Valor: ", valor)
