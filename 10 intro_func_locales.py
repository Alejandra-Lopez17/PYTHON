
def calcular_promedios(lista: list):

    def suma(lista):
        acumulador = 0
        for n in lista:
            acumulador += n
        return acumulador

    print('Suma-> ', suma(lista))
    promedio = suma(lista)/len(lista)
    return promedio

#print( calcular_promedios([10,20,30,40,50]) )


def sumar_numeros():

    def sumar(n1, n2): return n1+n2

    print(sumar(20, 30))


sumar_numeros()
