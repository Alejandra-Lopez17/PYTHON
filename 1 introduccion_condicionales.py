#Condicionales

num_1 = 100
num_2 = 200

if num_1 > num_2:
    print('num_1 es mayor a num_2')
else:
    print('num_1 es menor a num_2')

num_1 = 200
num_2 = 120
num_3 = 50
num_4 = 200

if (num_1 > num_2) and (num_3 > num_4):
    print("Se cumple la condición del and")
else:
    print("No se cumple la condición del and")

'''
Un solo igual (=) es asignación
Un doble igual (==) es comparación
'''
if (num_3 > num_2) or (num_1 == num_4):
    print("Se cumple la condición del or")
else:
    print("No se cumple la condición del or")

#Diferente -> !=
if not((num_1 > num_2 and num_4 != num_1) or (num_3 == num_2 and num_1 > num_3)):
    print("Se cumple condición #4")
else:
    print('No se cumple condición #4')

if not(num_2 == num_1):
    print("Se cumple la condición not(num_2 == num_1)")
else:
    print("No se cumple la condición not(num_2 == num_1)")
