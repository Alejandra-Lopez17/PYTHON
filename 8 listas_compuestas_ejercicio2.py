'''
2) Desarrolle un programa que solicite nombres de estudiantes y posteriormente
    solicite la nota de cada estudiante. Esta información debe guardarla en
    una lista compuesta con la siguiente estructura:
    *Ejemplo:
    [
        ['Juan', 'Pedro', 'María'],
        [4.5,   3.2, 4.5]
    ]
'''


def registrar_estudiantes(lista: list):
    opc = ''
    lista_nombres = []
    while opc != 'N':
        nombre = input('Nombre del estudiante: ')
        lista_nombres.append(nombre)
        opc = input('¿Desea ingresar mas estudiantes? S/N ').upper()

    lista.append(lista_nombres)


def menu():
    lista = []
    mensaje_menu = '---------------ESTUDIANTES - NOTAS-----------\n'
    mensaje_menu += '1) Registrar estudiantes\n'
    mensaje_menu += '2) Registrar notas\n'
    mensaje_menu += '-1) Salir\n'
    mensaje_menu += '>>> '

    opcion = 0
    while opcion != -1:
        opcion = int(input(mensaje_menu))
        #Evaluar la opción ingresada por el usuario
        if opcion == 1:
            registrar_estudiantes(lista)

        print(lista)


menu()
