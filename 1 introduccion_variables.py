#Esto es un comentario en python de una sola linea
"""
Esto es un
comentario de
varias
lineas
"""

'''
Este es otro comentario
de varias
lineas
'''

#Instrucción para mostrar mensaje por consola
print("¡Hola mundo!")

#Variables
numero = 10
num_1 = 5
#num-1 = 5 esto es una forma incorrecta
miVariable = 2
num1 = 4
#2num = 5 esto es una forma incorrecta

#Operaciones
num_1 = 5
num_2 = 2
num_3 = 4

suma = num_1 + num_2
multiplicacion = num_1 * num_3
division = num_1 / num_2
elevado = num_1 ** num_2
#módulo -> retorna el residuo de una división
modulo = elevado % 2
'''
Mostrar resultados por consola concatenando (uniendo) texto con el valor
de las variables
'''
print('Suma = ', suma)
print("Multiplicación = ", multiplicacion)
#Formatear salida
print(f"División = {division}")
#-----------
print("Elevado = %f" % elevado)
print('Suma = %f' % suma)

pi = 3.141598
print('PI = %.2f' % pi)

#String
texto = "Esto es una cadena de texto"
print(texto)

direccion = 'Cra 100 #42-25 '
ciudad = 'Barranquilla'
concatenado = direccion + ciudad
print(concatenado)

#El signo mas(+) no se puede utilizar con string y números
ejemplo = direccion + num1
