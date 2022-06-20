
numeros = [10, 15, 20, 25, 30, 35, 40, 45, 50, 55]

print('--------ELEVAR AL CUADRADO--------')
numeros_al_cuadrado = [n**2 for n in numeros]
print(numeros_al_cuadrado)

print('--------DIVIDIR POR 2--------')
division_numeros = [n/2 for n in numeros]
print(division_numeros)

print('-------OPERADORES TERNARIOS------')
numeros_pares = [n for n in numeros if n % 2 == 0]
print(numeros_pares)
impares_en_cero = [n if n % 2 == 0 else 0 for n in numeros]
print(impares_en_cero)

print('------------------------------------')
nombres = ['Juan', 'María', 'Pedro', 'Juliana']
iniciales = [n[0] for n in nombres]
print(iniciales)

mayusculas = [n.upper() for n in nombres]
print(mayusculas)
