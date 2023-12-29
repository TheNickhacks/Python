#Creado por Nicolás Navarro Garrido

import random

Matriz_Generada  = []
n = int(input("Ingrese el tamaño de la matriz-->")) #Tamaño matriz
#random.randint
Matriz_Generada=[[random.randint(0,255) for _ in range(n)]for _ in range(n)] #Matriz rellena por random.randint
print(" ")
print("Matriz Generada")
for f in Matriz_Generada:
    print(f)

def Buscar_Valores(Matriz):
    # Calculo funcion de costo g(n)
    naux= len(Matriz) #1
    ProductoMaximo = 0 #1
    Maximos = [] #1

#Ventana Deslizante
    for i in range(naux): # Iterador Vertical #n
        for h in range(naux): # Iterador Horizontal #n
            #Ventana Deslizante Horizontal 
            if (h + 3) < naux: #1
                Producto = Matriz[i][h] * Matriz[i][h + 1] * Matriz[i][h + 2] * Matriz[i][h + 3] 
                if (Producto > ProductoMaximo) : #1
                    ProductoMaximo = Producto
                    Maximos = [Matriz[i][h], Matriz[i][h+1], Matriz[i][h+2], Matriz[i][h+3]]
            
            #Ventana Deslizante Vertical
            elif(i + 3 < naux): #1
                Producto = Matriz[i][h] * Matriz[i + 1][h] * Matriz[i + 2][h] * Matriz[i + 3][h]
                if (Producto > ProductoMaximo) : #1
                    ProductoMaximo = Producto
                    Maximos = [Matriz[i][h], Matriz[i + 1][h], Matriz[i + 2][h], Matriz[i + 3][h]]
            
            #Ventana Deslizante Diagonal
            elif (i + 3 < naux) and (h + 3 < naux): #1
                Producto = Matriz[i][h] * Matriz[i + 1][h + 1] * Matriz[i + 2][h + 2] * Matriz[i + 3][h + 3]
                if (Producto > ProductoMaximo) : #1
                    ProductoMaximo = Producto
                    Maximos = [Matriz[i][h], Matriz[i + 1][h + 1], Matriz[i + 2][h + 2], Matriz[i + 3][h + 3]]
            
            #Ventana Deslizante Diagonal Invertida
            elif (i + 3 < naux) and (h - 3 < naux): #1
                Producto = Matriz[i][h] * Matriz[i + 1][h - 1] * Matriz[i + 2][h - 2] * Matriz[i + 3][h - 3]
                if (Producto > ProductoMaximo) : #1
                    ProductoMaximo = Producto
                    Maximos = [Matriz[i][h], Matriz[i + 1][h - 1], Matriz[i + 2][h - 2], Matriz[i + 3][h - 3]]

            else: #1
                pass
    print(" ")
    print("El producto maximo es-->", ProductoMaximo)
    print(" ")
    print("Los valores encontrados son-->", Maximos)

Buscar_Valores(Matriz_Generada)

'''
Analisis (Solo funcion Buscar_Valores)

1) Indicar el mejor y el peor caso si existen
Respuesta 1: En este tipo de programas donde se desea analizar toda la matriz no existen mejores o peores casos, debido 
a que la matriz se debe de comparar con todas las combinaciones de 4 numeros que tenga la matriz, para asi obtener
cual es el mayor producto de las combinaciones posibles.

2) Obtener la funcion de costo total g(n)
Respuesta 2: 9*n^2 + 3

3) Obtener el orden de complejidad O
Respuesta 3: El orden de complejidad del algoritmo de busqueda con ventana deslizante es O(n^2), debido a que
al tener un bucle for dentro de otro bucle for, el programa depende directamente del tamaño de la matriz, ya que
este debe de realizar la busqueda entera dentro de la matriz y asi generar la comparacion. 
Para sintetizar, el orden de complejidad de este algoritmo es O(n^2), debido a sus ciclos for enlaazados.

'''