
from numpy import random as r

participantes = ['Jorge', 'Juan', 'Andrea', 'Jaime',
                 'Alejandra', 'Alfonso', 'Cristian', 'Paola']

#Generar listas/matrices de manera aleatoria utilizando probabilidad
ganadores = r.choice(participantes, size=[2], p=[
                     0.1, 0.1, 0.3, 0.1, 0.1, 0.1, 0.1, 0.1], replace=False)

print('Ganadores del viaje: ', ganadores)

r.shuffle(participantes)
print(participantes)
