import random
Cadena = []

aux = int(input("Ingrese el largo del vector a generar -->"))
for _ in range(aux):
    Numero = random.randint(0,255)
    Cadena.append(Numero)
print("Vector Generado Aleatoriamente")
print(Cadena)

n = int(input("Ingrese valor a buscar -->"))

#Algoritmo de Busqueda Binaria
Left = 0                            # 1
Right = len(Cadena)-1               #1
BooleanAux = False                  #1 

while (Left <= Right):              #n/2
    Middle = (Left+Right) // 2      #Suma Exacta #1

    if (Cadena[Middle] == n):       #n-1
        print("El valor buscado esta en la posicion, ",Middle)
        BooleanAux = True 
        break

    elif (Cadena[Middle] < n):      #n-1
        Left = Middle + 1 

    else:                           #n-1
        Right = Middle - 1

if (BooleanAux == False):           #1
    print("Valor no Encontrado en el vector")
else: 
    pass

#la funcion g(n) para una lista de largo n es: 1+ 3*n+ n/2
'''
La complejidad algoritmica es del tipo logaritmica o "O(log n)"
debido a que a medida que itera el programa, reduce el tamaño de busqueda dividiendo
en dos, ya que busca desde atras y adelante, hasta encontrar el punto medio.
'''