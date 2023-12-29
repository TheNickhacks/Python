#Creado por Nicolas Navarro Garrido

import numpy as np
import time

Vector_Bus = []
n= int(input("Ingrese tamaño del vector --> "))

for _ in range(n):
    aux= np.random.randint(0,n)
    Vector_Bus.append(aux)
