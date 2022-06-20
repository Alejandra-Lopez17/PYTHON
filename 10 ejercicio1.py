def crear_operacion(operacion: str):
    funcion = ''
    if operacion == '+':
        def funcion(n1, n2): return n1+n2
    elif operacion == '-':
        def funcion(n1, n2): return n1-n2
    elif operacion == '*':
        def funcion(n1, n2): return n1*n2
    elif operacion == '/':
        def funcion(n1, n2): return n1/n2
    elif operacion == '**':
        def funcion(n1, n2): return n1**n2
    else:
        def funcion(n1, n2): return 'Ingrese una operación válida'

    return funcion


""" def orden_superior(funcion):
    resultado = funcion(10,20)
    return f'El resultado es {resultado}' """


def orden_superior(
    func_operacion): return f'El resultado es {func_operacion(10,20)}'


respuesta = crear_operacion('-')
orden_superior(respuesta)


#print(func_orden_superior(respuesta))


'''
1) Desarrolle una función anónima para calcular el promedio de tres números
2) Desarrolle una función anónima que reciba como parámetro una lista de Strings 
    y retorne un conjunto con los elementos de la lista
'''
#Punto #1
def promedio(n1, n2, n3): return (n1+n2+n3)/3
print(promedio(4.5, 4.2, 4.4))

#Punto #2
def conversion(lista): return set(lista)
print(conversion(['Juan', 'Pedro', 'María', 'Juliana', 'Liliana']))
