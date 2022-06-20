
'''------------FUNCIONES------------'''

#def -> Palabra reservada para crear una función

#Función
#camelCase -> Combinar minúsculas con mayúsculas


def miPrimeraFuncion():
    mensaje = "Hola mundo, esta es mi primera función"
    print(mensaje)


def sumar():
    num_1 = 10
    num_2 = 15
    suma = num_1 + num_2
    print(f"{num_1} + {num_2} = {suma}")


def sumar_con_parametros(num_1: int, num_2: int, num_3: int):
    suma = num_1 + num_2 + num_3
    print(suma)


#Llamar la función
#miPrimeraFuncion()
#sumar()
#Llamar función con valores
#sumar_con_parametros(5, 2, 4)
#sumar_con_parametros(10, 20, 30)
#sumar_con_parametros(6,8,9)


'''
Ejercicios:
1) Desarrolle una función que eleve a la potencia un número
2) Desarrolle una función que calcule los intereses de un CDT
    -> (cantidad * porcentaje_interes * tiempo) / 12
3) Desarrolle un una función que calcule el promedio de 4 notas de un estudiante
'''

#Punto 1


def elevar_a_la_potencia(num, potencia):
    resultado = num ** potencia
    print(resultado)

#Punto 2


def calcularCDT(cantidad, porcentaje, tiempo):
    resultado = (cantidad*porcentaje*tiempo)/12
    print(f"{resultado}")

#Punto 3
#Solución de Juan Carlos


def promedioNotas(nota1: float, nota2: float, nota3: float, nota4: float):
    prome = (nota1 + nota2 + nota3 + nota4) / 4
    print(prome)


#promedioNotas(4.5,3.8, 3.2, 5.0)
#calcularCDT(1000,0.19,6)
#elevar_a_la_potencia(5, 2)

def sumar(num_1, num_2):
    resultado = num_1 + num_2
    return resultado


resp = sumar(10, 5)
print(resp)
print(sumar(2, 12))

sumatoria = sumar(20, 50)

sumatoria_2 = sumatoria + 10
print(sumatoria_2)


def saludar(nombre_usuario):
    return "Hola "+nombre_usuario+", nos alegra que nos visites"


print(saludar('Andrea'))
