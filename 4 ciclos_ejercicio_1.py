
#Input para solicitar datos al usuario
#Input retorna un string
#Castear/convertir -> int()
#num_1 = int( input('Ingrese un número >>> ') )
#num_2 = int( input('Ingrese otro número >>> ') )
#suma = num_1 + num_2
#print(f'La suma es {suma}')

def pedir_numeros():
    datos = {}
    #Solicitar datos al usuario y convertirlos a flotante (números con decimales)
    num_1 = float(input('Ingrese el primer número >>> '))
    num_2 = float(input('Ingrese el segundo número >>> '))
    #Añadir números al diccionario
    datos['num_1'] = num_1
    datos['num_2'] = num_2
    #Retornar diccionario
    return datos


def sumar(n1, n2):
    return (n1+n2)


def restar(n1, n2):
    return (n1-n2)

#numeros = pedir_numeros()
#print(numeros)


def menu():
    opcion = ''

    while opcion != 3:
        mensaje_menu = '1) Sumar\n'
        mensaje_menu += '2) Restar\n'
        mensaje_menu += '3) Salir\n'
        mensaje_menu += '>>> '
        #Capturo lo que ingresa el usuario y lo casteo/convierto a entero
        opcion = int(input(mensaje_menu))
        if opcion == 1:
            #Solicitar datos al usuario y convertirlos a flotante (números con decimales)
            numeros = pedir_numeros()
            #Sumar los números
            suma = sumar(numeros['num_1'], numeros['num_2'])
            print('--------------\n', suma, '\n----------------')
        elif opcion == 2:
            #Solicitar datos al usuario y convertirlos a flotante (números con decimales)
            numeros = pedir_numeros()
            resta = restar(numeros['num_1'], numeros['num_2'])
            print('--------------\n', resta, '\n----------------')
        elif opcion != 3:
            print('opción incorrecta')


#Llamar la función principal
menu()
