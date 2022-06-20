
'''
1) Desarrollar una función que reciba como parámetro el nombre y la edad
    del usuario. Muestre en pantalla el nombre del usuario e indique si es mayor de edad
    o menor de edad. Ejemplo: "Pepito es mayor de edad"

2) Desarrolle una función que calcule y muestre el promedio de 4 notas de un estudiante
    e imprima en consola si el estudiante pasó la materia o no.
    NOTA:
    *Con una nota mayor o igual a 3 pasa la materia
    *La función debe de recibir como parámetro el nombre del estudiante y las cuatro notas
    *Motrar en pantalla el nombre del estudiante, su promedio e indicar si pasó
    o no pasó la materia

3) Desarrolle una función que calcule el valor del interes de un CDT.
    Muestre en pantalla:
        *El valor TOTAL DEL DINERO al momento de retirarlo del CDT
        *Si el usuario retira el dinero menor o igual a dos meses se aplica una penalidad del 2%
            Fórmula: 
                *Penalidad: dinero * 0.02
                *Mostrar en pantalla el valor de la penalidad
        *Si el usuario retira el dinero en un plazo mayor a dos meses su interés será:
            Fórmula:
                *valor_interes = (dinero * porcentaje_interes * tiempo) / 12
            *Mostrar en pantalla el valor del interés ganado

'''


def CDT(dinero: float, porcentaje_interes: float, tiempo: int):
    if tiempo <= 2:
        penalidad = dinero * 0.02
        total_dinero = dinero - penalidad
        txt_penalidad = f'La penalidad es de {penalidad}'
        txt_total_dinero = f'El total de dinero a retirar es {total_dinero}'
        return txt_penalidad+'\n'+txt_total_dinero
    else:
        valor_interes = (dinero * porcentaje_interes * tiempo) / 12
        total_dinero = dinero + valor_interes
        txt_intereses = f'El valor de los intereses es de {valor_interes}'
        txt_total_dinero = f'El total de dinero a retirar es {total_dinero}'
        return txt_intereses+'\n'+txt_total_dinero


print(CDT(1000000, 0.3, 3))


def definir_mayor_edad(nombre: str, edad: int):
    if edad >= 18:
        print(f'{nombre} es mayor de edad')
    else:
        print(nombre, ' es menor de edad')

#definir_mayor_edad('Juan', 18)

#Punto 2
#Solución de Andrea


def rendimientoAcademico(estudiante: str, nota_1: float, nota_2: float, nota_3: float, nota_4: float):
    resultado = (nota_1 + nota_2, nota_3, nota_4) / 4
    if (resultado < 3.0):
        print(estudiante, "Reprobó la materia con una nota de", resultado)
    else:
        print(estudiante, "Aprobó la materia con una nota de", resultado)

#rendimientoAcademico("Andrea", 3.4, 5.2, 3.4, 6.1)
