
'''

estudiantes = {
    '12345': {
        'nombre': '',
        'apellido': '',
        'notas': []
    }
}

estudiantes.pop('12345678')

for cedula, info in estudiantes.items():
    pass

'''


def registrar_estudiante(estudiantes: dict):
    print('-------------REGISTRAR ESTUDIANTE:--------------\n')
    #Obtener la cédula del estudiante
    cedula = input('Ingrese la cédula del estudiante: ')
    #Añadir datos al diccionario 'estudiantes'
    estudiantes[cedula] = {
        'nombre': input('Nombre: '),
        'apellido': input('Apellido: ')
    }
    print('\nUsuario registrado con éxito\n')


def registrar_notas(estudiantes: dict):
    print('-------------REGISTRAR NOTAS:--------------\n')
    #Obtener la cédula del estudiante
    cedula = input('Ingrese la cédula del estudiante: ')
    #Validar si la cédula está como clave en el diccionario
    if cedula in estudiantes:
        nombre = estudiantes[cedula]['nombre']
        apellido = estudiantes[cedula]['apellido']
        print(f'Estudiante: {nombre} {apellido}')
        notas = []
        opc = ''
        contador = 1
        while opc != 'N':
            nota = float(input(f'Ingrese nota {contador}: '))
            #Agregar la nota a la lista 'notas'
            notas.append(nota)
            #Solicitar dato al usuario y ponerlo en mayúscula
            opc = input('¿Desea ingresar mas notas? S/N ').upper()
            contador += 1
        estudiantes[cedula]['notas'] = notas

    else:
        print('\nLa cédula ingresada no se encuentra en la base de datos\n')


def actualizar_estudiante(estudiantes: dict):
    print('-------------ACTUALIZAR ESTUDIANTE:--------------\n')
    #Solicitar cedula del estudiante
    cedula = input('Ingrese la cédula del estudiante: ')
    #Validar si el estudiante existe en el diccionario
    if cedula in estudiantes:
        nombre = input('Ingrese nuevo nombre: ')
        apellido = input('Ingrese nuevo apellido: ')
        #Actualizar info en el diccionario
        estudiantes[cedula]['nombre'] = nombre
        estudiantes[cedula]['apellido'] = apellido
    else:
        print('\nLa cédula ingresada no se encuentra en la base de datos\n')


def actualizar_notas(estudiantes: dict):
    print('-------------ACTUALIZAR NOTAS DEL ESTUDIANTE:--------------\n')
    #Solicitar cédula
    cedula = input('Ingrese la cédula del estudiante: ')
    #Validar si el estudiante existe
    if cedula in estudiantes:
        #Validar si el estudiante tiene notas
        if 'notas' in estudiantes[cedula]:
            notas: list = estudiantes[cedula]['notas']
            print('\nnota\tid_nota')
            for index in range(0, len(notas)):
                print(f'{notas[index]}\t{index}')
            #Obtener el id_nota a actualizar
            id_nota = int(input('\nIngrese el id de la nota a actualizar: '))
            #Tarea: Validar si el id_nota que ingresó el usuario existe
            #validar aquí...
            #...
            nueva_nota = float(input('Ingrese la nueva nota: '))
            #Actualizar nota
            notas[id_nota] = nueva_nota
            print('\n¡Nota actualizada con éxito!\n')
        else:
            nombre = estudiantes[cedula]['nombre']
            print(f'\nEl/La estudiante {nombre} no tiene notas asignadas\n')


def consultar_estudiantes(estudiantes: dict):
    print('-------------CONSULTAR ESTUDIANTE:--------------\n')
    #Iterar diccionario
    for cedula, info in estudiantes.items():
        nombre = info['nombre']
        apellido = info['apellido']
        print(f'--------------{nombre} {apellido}--------------')
        print(f'Cédula: {cedula}')
        print('Notas: ')
        #Validar si el estudiante tiene notas
        if 'notas' in info:
            notas = info['notas']
            for n in notas:
                print(f'\t*{n}')
        else:
            print('El estudiante no tiene notas asignadas')


def eliminar_estudiante(estudiantes: dict):
    print('-------------ELIMINAR ESTUDIANTE:--------------\n')
    #Obtener la cédula del estudiante
    cedula = input('Por favor ingrese la cédula del estudiante: ')
    if cedula in estudiantes:
        #Eliminar estudiante
        estudiantes.pop(cedula)
        print('\nEstudiante eliminado con éxito\n')
    else:
        print(
            f'\nEl estudiante con cédula {cedula} no existe en la base de datos')


def menu():
    estudiantes = {
        '123456': {
            'nombre': 'Ana Maria',
            'apellido': 'Varela',
            'notas': [4.2, 5.0, 3.8, 4.5]
        }
    }
    #Tarea: Desarrollar una nueva opción para visualizar las notas del estudiante
    #Tarea: Desarrollar una nueva opción para consultar estudiante por cédula
    mensaje_menu = '------------------CRUD ESTUDIANTES-----------------\n'
    mensaje_menu += '1) Registrar estudiante\n'
    mensaje_menu += '2) Registrar notas del estudiante\n'
    mensaje_menu += '3) Actualizar estudiante\n'
    mensaje_menu += '4) Actualizar notas\n'
    mensaje_menu += '5) Consultar estudiantes\n'
    mensaje_menu += '6) Eliminar estudiante\n'
    mensaje_menu += '7) Eliminar todos los estudiantes\n'
    mensaje_menu += '8) Salir\n'
    mensaje_menu += '>>> '

    opcion = ''
    while opcion != 8:
        opcion = int(input(mensaje_menu))

        if opcion == 1:
            registrar_estudiante(estudiantes)
        elif opcion == 2:
            registrar_notas(estudiantes)
        elif opcion == 3:
            actualizar_estudiante(estudiantes)
        elif opcion == 4:
            actualizar_notas(estudiantes)
        elif opcion == 5:
            consultar_estudiantes(estudiantes)
        elif opcion == 6:
            eliminar_estudiante(estudiantes)
        elif opcion == 7:
            estudiantes.clear()
            print('\nTodos los estudiantes han sido eliminados con éxito\n')
        elif opcion != 8:
            print('Por favor ingrese una opción válida')


menu()


""" nombre = input("Ingrese su nombre: ")
print('Su nombre es: ', nombre)

#Castear/convertir
edad = int( input("Ingrese su edad: ") )
suma = edad + 20
print("Suma: ", suma) """
