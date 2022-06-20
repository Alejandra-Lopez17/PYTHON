def ordenes(rutinaContable):
    from functools import reduce
    ordenMinima = 600000
    ordenTotal = list(map(lambda x: [x[0]] + list(map(lambda y: y[1]*y[2], x[1:])), rutinaContable))
    ordenTotal = list(map(lambda x: [x[0]] + [reduce(lambda a, b: round(a + b, 2), x[1:])], ordenTotal))
    ordenTotal = list(map(lambda x: x if x[1] >= ordenMinima else (x[0], x[1] + 25000), ordenTotal))

    print('------------------------ Inicio Registro diario ---------------------------------')
    for x in range(len(ordenTotal)):
        print(
            f'La factura {ordenTotal[x][0]} tiene un total en pesos de {ordenTotal[x][1]:,.2f}')
    print('-------------------------- Fin Registro diario ----------------------------------') 
