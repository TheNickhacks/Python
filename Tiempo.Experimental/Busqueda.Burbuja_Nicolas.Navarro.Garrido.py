#Creado por Nicolas Navarro Garrido

import numpy as np
import time

Vector_Bus = []
n= int(input("Ingrese tamaño del vector --> "))

#Relleno de matriz Vector_Bus[]
for _ in range(n):
    aux= np.random.randint(0,n)
    Vector_Bus.append(aux)

Vector_Busd = Vector_Bus #Para ordenar Descendentemente
print("Matriz sin Orden")
print(Vector_Bus)

#Aplicacion de Metodo Burbuja Ascendente

for i in range(n):
    Count_inicio=time.time()
    for j in range(0,n-i-1):
        if (Vector_Bus[j] > Vector_Bus[j+1]):
            Aux = Vector_Bus[j]
            Vector_Bus[j] = Vector_Bus[j+1]
            Vector_Bus[j+1] = Aux

Tiempo_Ejecu=time.time()-Count_inicio
print("Orden Ascendente por Metodo burbuja")
print(Vector_Bus)
print("Tiempo de ejecucion Orden Ascendente -->", Tiempo_Ejecu)

print("------------------------------")
print(" ")
print(" ")

for i in range(n):
    Count_iniciod=time.time()
    for j in range(0,n-i-1):
        if (Vector_Busd[j] < Vector_Busd[j+1]):
            Auxd = Vector_Busd[j]
            Vector_Busd[j] = Vector_Busd[j+1]
            Vector_Busd[j+1] = Auxd

Tiempo_Ejecd=time.time()-Count_iniciod
print("Orden Descendente por Metodo burbuja")
print(Vector_Busd)
print("Tiempo de ejecucion Orden Descendente -->", Tiempo_Ejecd)