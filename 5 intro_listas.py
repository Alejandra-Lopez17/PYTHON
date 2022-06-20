
lista_vacia = []

miLista = ['Juan', 20, True]

print(miLista)

primer_elemento = miLista[0]
print(primer_elemento)

segundo_elemento = miLista[1]
print(segundo_elemento)

tercer_elemento = miLista[2]
print(tercer_elemento)

#Actualizar valores de la lista
miLista[0] = "Jaime"
print(miLista)

miLista[1] = "Ana maria"
print(miLista)

miLista[2] = 10
print(miLista)

#Añadir elementos a la lista
miLista.append("John")
print(miLista)
miLista.append("María")
print(miLista)

#Eliminar elementos de la lista
#pop -> elimina el último elemento de la lista
miLista.pop()
print(miLista)
#Eliminar elementos por indice
miLista.pop(1)
print(miLista)
