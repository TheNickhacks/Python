#Creado por Nicolas Navarro Garrido
import numpy as np
import time
import matplotlib.pyplot as plt

#Respuestas a preguntas teoricas al final del programa

Vector_Bus = []
n= int(input("Ingrese tamaño del vector --> "))

for _ in range(n):
    aux= np.random.randint(0,n)
    Vector_Bus.append(aux)

print(Vector_Bus)
Aux = False
Buscar = int(input("Ingrese valor a buscar en vector --> "))
for fila in range(n):
    Cont_tiempo = time.time()
    if Vector_Bus[fila] == Buscar:
        print("Valor encontrado en la posicion -->",fila)
        Aux = True
        break

if Aux == False:
    print("El valor no se encuentra en el vector")
else:
    pass

Cont_final = time.time()
T_Ejecucion = Cont_final-Cont_tiempo
print("Tiempo de ejecucion --> ", T_Ejecucion)

'''
Lenguaje Formal
Algorithm VectorSearch (V, n, X)
    Input Vector V of n integers, X value to search
    Output integer b with position of the search value
    V <- New array of n integers
    for i <- 0 to n do
        if V[i] <- X
            b <- i
    return b
'''

# Hacer tiempos de ejecucion para
# n= [100000, 500000, 640000, 900000, 430000]
#Tiempos de ejecucion

import numpy as np
import time

def Buscar_Valor_Vector(n, X):
    Vector_Bus = []
    T_Ejecuciondef = 0
    for _ in range(n):
        aux = np.random.randint(0, n)
        Vector_Bus.append(aux)
    
    #print("Vector generado:", Vector_Bus)
    
    encontrado = False
    
    for fila in range(n):
        Cont_tiempo = time.time()
        if Vector_Bus[fila] == X:
            print("Valor encontrado en la posicion -->", fila)
            encontrado = True
            break
    Cont_final = time.time()
    T_Ejecuciondef = Cont_final-Cont_tiempo
    print("Tiempo de ejecución:", T_Ejecuciondef)
    if Aux == False:
        print("El valor no se encuentra en el vector")
    else:
        pass
    return T_Ejecuciondef

# n= [10000000, 5000000, 6400000, 9000000, 4300000]
print(" ")
print(" ")
print(" ")
print("--------------------------")
print(" ")
Xu = np.random.randint(0, 100000)
tu = 10000000
print("Valor Buscado -->", Xu)
Ejecu = Buscar_Valor_Vector(tu, Xu)

print("--------------------------")
print(" ")
Xd = np.random.randint(0, 500000)
print("Valor Buscado -->", Xd)
td = 5000000
Ejecd = Buscar_Valor_Vector(td, Xd)

print("--------------------------")
print(" ")
Xt = np.random.randint(0, 640000)
print("Valor Buscado -->", Xt)
tt = 6400000
Eject = Buscar_Valor_Vector(tt, Xt)

print("--------------------------")
print(" ")
Xc = np.random.randint(0, 900000)
print("Valor Buscado -->", Xc)
tc = 9000000
Ejecc = Buscar_Valor_Vector(tc, Xc)

print("--------------------------")
print(" ")
Xcc = np.random.randint(0, 430000)
print("Valor Buscado -->", Xcc)
tcc = 4300000
Ejeccc = Buscar_Valor_Vector(tcc, Xcc)

#Grafico Tamaño_Problema vs Tiempo_Ejecucion

# x = Tamaño_Problema
x_plot = [tu, td, tt, tc, tcc]

# y = Tiempo_Ejecucion
y_plot = [Ejecu, Ejecd, Eject, Ejecc, Ejeccc]

plt.plot(x_plot, y_plot, marker='*')

plt.xlabel('Tamaño_Problema')
plt.ylabel('Tiempo_Ejecucion')

plt.title('Tamaño_Problema vs Tiempo_Ejecucion')

plt.show()

'''
1)¿En que se parece el grafico de g(n) y el grafico tamaño del problema vs tiempo?
Respuesta 1: Se asemejan en que a medida que el valor de n aumenta, el valor del tiempo
aumenta, debido a que se debe de buscar el valor entre un vector mucho mas grande.

2)¿En que aspectos la teoria acierta con la prediccion y en que aspectos no acierta?
Respuesta 2: Acierta en el ambito de que a mayor tamaño del problema, el tiempo de espera sera mucho mayor,
pero no acierta en que a medida que los valores buscados y tamaños del problema son bajos, los tiempos de espera
son casi nulos, por lo que no se nota, gracias al gran nivel de computo que poseen los computadores hoy en dia.

3)¿Que pasa si hacemos esto mismo en un computador mas lento?
Respuesta 3: Lo que pasará es que los tiempos aumentarian significativamente en referencia a los encontrados al ejecutar
este programa, debido a que mi computador personal, posee caracteristicas similares a los presentes en los laboratorios de
la universidad. Para resumir, al ejecutar este programa en un equipo con menos capacidades este tendra tiempos de espera
mas prolongados y seran mas notorios.

4)Segun el programa en otro lenguaje de programacion mostrado por el profesor, ¿porqué se produce la diferencia?
Respuesta 4: Se tomará como referencia los lenguajes de programacion de Python y C++, en el caso de que el problema
fuera resuelto mediante C++, los tiempos de espera serian mucho menores, debido a que este lenguaje de programacion
esta mucho mas optimizado para el trabajo interno del equipo, mientras que python ofrece un entorno simplificado y 
flexible a la hora de escribir codigo, es por eso que penaliza mas la forma en la que el computador trabaja con 
busquedas de computo como las que se realizan en este programa.
'''
