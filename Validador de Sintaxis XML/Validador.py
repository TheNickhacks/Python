#Created by Nicolas Navarro Garrido "Nickhacks"

class Nodo:
    def __init__(self, Dato):
        self.Dato = Dato
        self.Sig = None

class Pila: #LIFO (Last IN, First OUT)
    def __init__(self):
        self.Tope = None
    
    def Vacio (self): #Verificar Pila Vacia
        if (self.Tope == None):
            return None
        else:
            return self.Tope.Dato

    def Push(self, Datos): #Agregar a la Pila
        Nodo_Nuevo = Nodo(Datos)
        Nuevo_Siguiente = self.Tope
        self.Tope = Nodo_Nuevo
    
    def Pop(self): #Sacar de la Pila
        if (self.Vacio() != None):
            Elemento = self.Tope.Dato
            self.Tope = self.Tope.Sig
            return Elemento
        else:
            return None
    
    def Print(self): #Muestra toda la lista
        Elemento = self.Tope
        while (Elemento != None):
            print(Elemento.Dato)
            Elemento = Elemento.Sig

def Abrir_Texto(Texto):
    #Abre un archivo.txt y lo ingresa a una Variable String
    Archivo = open(Texto,"r")
    Contenido = Archivo.read()
    Archivo.close()
    return Contenido

def Verificar(Texto):
    Aux = [] #Almacena los Errores
    Count = 0 #Cuenta los Errores
    while Count < len(Texto):
        if Texto[Count] == '<':
            if Count + 1 < len(Texto) and Texto[Count + 1] == '/':
                if Aux:
                    Aux.pop()
                    Count = Count + 2
                else:
                    return False
            else:
                Count = Count + 1
                Auxd = Count
                while Count < len(Texto) and Texto[Count] != '>':
                    Count = Count + 1
                if Count == len(Texto):
                    return False
                tag = Texto[Auxd:Count]
                Aux.append(tag)
                Count = Count + 1
        else:
            Count = Count + 1

    return True


Contenido_Archivo = None
Use_Pila = Pila()

#Main
while True:
    for _ in range(5*1000000):  # Aproximadamente 5 segundos de pausa
        pass
    print("\nMenu de opciones")
    print("Opcion 1: Leer, Almacenar y Mostrar Archivo")
    print("Opcion 2: Verificar Sintaxis del Archivo")
    print("Opcion 3: Salir")
    
    Opcion = int(input("Ingrese su Opcion como Numero --> "))
    if(Opcion == 1):
        print("\nA Continuacion se Leera el Archivo de Texto")

        Archivo = input("\nIngrese Nombre del Archivo sin extension-->")
        ArchivoU = Archivo + ".txt"
        Contenido_Archivo = Abrir_Texto(ArchivoU)
        print("\nArchivo Cargado Correctamente")

        print("\nA Continuacion se Almacenará el Archivo de Texto")
        Use_Pila.Push(Contenido_Archivo)
        print("\nArchivo Almacenado en la Pila")

        print("\nA Continuacion se Mostrará el Archivo Almacenado")
        Use_Pila.Print()
        for _ in range(5*1000000):  # Aproximadamente 5 segundos de pausa
            pass

    elif(Opcion == 2):
        print("\nVerificando la sintaxis")
        for _ in range(5*1000000):  # Aproximadamente 5 segundos de pausa
            pass
        Verificacion = Verificar(Contenido_Archivo)
        if(Verificacion == True):
            print("Sintaxis Ok")
        else:
            print("Error de Sintaxis")
    
    elif(Opcion == 3):
        print("----Fin Programa----")
        break
    
    else:
        print("Opcion no valida")
        for _ in range(5*1000000):  # Aproximadamente 5 segundos de pausa
            pass