#Created By:  Nickhacks
#Nicolas Andres Navarro Garrido

class Arbol: #Definicion Clase Arbol Vista en Clases
    def __init__(self, Valores, Lista):
        self.Valores = Valores
        self.Descendencia = Lista

def Suma_Arbol(Estructura, Valor_Inicial): #Funcion Recursiva para Calcular la Suma de los Valores dentro 
    if Estructura is None: #de un Arbol Incluyendo un Valor Inicial.
        return Valor_Inicial
    else:
        Suma = Estructura.Valores + Valor_Inicial
        for Valor in Estructura.Descendencia:
            Suma = Suma_Arbol(Valor, Suma) #Aplicacion de la Recursividad
        return Suma #Retorno de la Variable que Almacena la Suma

# Aplicacion de la Clase Arbol, con Formato Visto en Clases
Arbol_Uno =Arbol(3, [Arbol(6, [Arbol(12, []), Arbol(18, [Arbol(21, []), Arbol(24, []), Arbol(27, [])])]), Arbol(9, [Arbol(15, [])])]) # Arbol 1 con 9 Valores
Arbol_Dos = Arbol(8, [Arbol(12, []), Arbol(6, [])]) #Arbol 2 con 3 Valores
Arbol_Tres = Arbol(3, [Arbol(6, []), Arbol(9, [Arbol(12, [Arbol(15, [])])])]) #Arbol 3 con 5 Valores, uno de ellos Negativo

Inicio = 35 #Valor Inicial para Test de Programa

Total = Suma_Arbol(Arbol_Uno, Inicio)#Aplicacion de Funcion Recursiva con Arbol 1

print("La Suma de los Datos en el Arbol Incluyendo el Valor Inicial es: ",Total) #Retorno de la Suma Calculada
