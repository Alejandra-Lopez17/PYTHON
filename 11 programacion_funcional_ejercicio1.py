

'''
UTILIZAR LIST COMPREHENSION Y LAMBDA
1) Desarrolle una función que reciba como parámetro una lista de números,
    retorne una lista con los números pares elevados al cuadrado
2) Desarrolle una función que reciba como parámetro una lista de nombres,
    Retorne una lista con las iniciales
    ['Andres', 'María']
    ['A', 'M']
3) Desarrolle una función que reciba como parámetro una lista de nombres,
    Retorne una lista con los nombres que empiecen por 'J' y coloque 
    su nombre en mayúscula
'''
#Punto #1
def elevar_pares_al_cuadrado(lista): return [n**2 for n in lista if n % 2 == 0]


numeros = [10, 20, 30, 40, 50, 60, 70, 80, 90, 15, 25, 35, 45]
print(elevar_pares_al_cuadrado(numeros))


#Punto #2
def obtener_iniciales(lista): return [n[0] for n in lista]


nombres = ['Andres', 'María', 'Juan']
print(obtener_iniciales(nombres))

#Punto #3


def nombre_x_J(lista): return [n.upper() for n in lista if n[0].lower() == 'j']


print(nombre_x_J(['Andrés', 'María', 'Juan', 'Juliana', 'Jorge', 'Jose']))
