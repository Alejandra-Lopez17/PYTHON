
#cadena de caracteres
#Las cadenas de caracteres son inmutables
saludo = "HOLA MUNDO"

primer_caracter = saludo[2]
print(primer_caracter)

espacio = saludo[4]
print(espacio)

print(saludo[5])
print(saludo[7])

#len -> Obtener el tamaño de una cadena de caracteres
tamanio = len(saludo)
print(tamanio)
ultimo_caracter = saludo[tamanio-1]
print("ultimo caracter-> ", ultimo_caracter)
'''
Del primer item hasta el último utilizo números positivos empezando desde cero (0)
Del último hasta el primero utilizo números negativos a partir del -1
'''
ultimo_caracter = saludo[-1]

#------------REBANADO DE CADENAS-------------

saludo = "hola"
#Primer posición se incluye, última posición se excluye
rebanado_1 = saludo[0:3]
print(rebanado_1)

rebanado_2 = saludo[1:3]
print(rebanado_2)
