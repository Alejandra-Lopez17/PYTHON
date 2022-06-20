conjunto_vacio = set()

conjunto_de_elementos = {10, 20, 30, 40, 50, 60}
#print(conjunto_de_elementos)

conjunto_a = {10, 20, 30, 40, 50, 60}
conjunto_b = {5, 10, 15, 20, 25, 35, 40, 60, 65}

print('Conjunto A:\n', conjunto_a)
print('Conjunto B:\n', conjunto_b)
print('---------INTERSECCIÓN------')
interseccion = conjunto_a.intersection(conjunto_b)
print(interseccion)
print('Estado del conjunto A:\n', conjunto_a)

print('------INTERSECTION UPDATE-------')
conjunto_a.intersection_update(conjunto_b)
print('Estado del conjunto A:\n', conjunto_a)

print('---------DIFFERENCE------')
difference = conjunto_a - conjunto_b  # conjunto_a.difference(conjunto_b)
print('Diferencia:\n', difference)
print('Estado de Conjunto A:\n', conjunto_a)

print('---------LOS CONJUNTOS NO TIENEN DUPLICIDAD DE DATOS-------')
nombres = {'Juan', 'Pedro', 'Eliana', 'Pedro', 'Juan', 'Eliana', 'Andrea'}
print(
    "Inicializando un conjunto: \n{'Juan', 'Pedro', 'Eliana', 'Pedro', 'Juan', 'Eliana', 'Andrea'}")
print('Estado del conjunto nombres:\n', nombres)
