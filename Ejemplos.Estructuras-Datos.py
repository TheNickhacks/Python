#Created By:
#Nicolás Navarro Garrido

class Nodo: #definicion de la clase nodo para pila, fila, Lista simple enlazada
    def __init__(self, Datos):
        self.datos = Datos # Dato a agregar al nodo
        self.proximo = None #Posicion proxima al dato agregado al nodo, inicia en None
        
    def MostrarNodo (self): #Funcion para mostrar el dato agregado al nodo
        return self.datos

class Pila: #LIFO
    def __init__(self): 
        self.Superior = None #Definicion parte superior de la pila, debido a su topologia LIFO
        #last in, first out

    def Empujar(self, datos): #Agrega nodo con dato a la pila "Empujando" el nodo anterior
        Aux = Nodo(datos)
        Aux.proximo = self.Superior
        self.Superior = Aux

    def Lectura(self): #Mostra la pila generada anteriormente
        Aux = self.Superior
        self.Superior = self.Superior.proximo
        return Aux


class Fila: #FIFO
    def __init__(self):
        self.Primero = None #Definicion primer dato de la fila, debido a su topologia FIFO
        self.Ultimo = None #Definicion ultimo dato de la fila, debido a su topologia FIFO
        #first in, first out

    def Vacia(self): # Funcion para verificar si no posee algun nodo
        return self.Primero is None
    
    def Ingreso(self, datos): # Ingreso de datos a la fila, a traves de la clase nodo anterior

        Nuevo_Nodo = Nodo(datos)

        if self.Vacia() == None: 
            self.Primero = Nuevo_Nodo
            self.Ultimo = Nuevo_Nodo
        else :
            self.Ultimo.proximo = Nuevo_Nodo
            self.Ultimo = Nuevo_Nodo
    
    def Sacar(self): #Eliminando o quitando de la fila al primer nodo que posee la fila, debido a su topologia

        if self.Vacia() == None:
            return None
        datos = self.Primero.datos
        self.Primero = self.Primero.proximo
        
        if self.Primero == None:
            self.Ultimo = None
        return datos
    
class ListaSimpleEnlazada: #Clase lista simple
    def __init__(self):
        self.Inicio = None #definicion del inicio de la lista
        self.Ultimo = None #definicion del final de la lista
    
    def AgregarDatosInicio(self, datos): #Funcion para agregar datos adelante en la lista

        Nuevo_Nodo = Nodo(datos) #Utiliza la clase nodo anterior

        if self.Inicio == None:
            self.Inicio = Nuevo_Nodo
        else:
            Aux = self.Inicio
            while (Aux.proximo):
                Aux = Aux.proximo
                Aux.proximo = Nuevo_Nodo
    
    def AgregarDatosFinal(self, datos):  #Funcion para agregar datos al final en la lista

        Nuevo_Nodo = Nodo(datos) #Utiliza la clase nodo anterior

        if not self.Inicio:
            self.Inicio = Nuevo_Nodo
        else :
            Aux = self.Inicio
            while (Aux.proximo):
                Aux = Aux.proximo
            Aux.proximo = Nuevo_Nodo
    
    def AgregarDatoPosicion(self, datos, posicion):

        Nuevo_Nodo = Nodo(datos)

        if posicion == 0:
            Nuevo_Nodo.proximo = self.Inicio
            self.Inicio = Nuevo_Nodo
        else:
            Aux = self.Inicio
            Count = 0
            while (Aux and Count < posicion-1):
                Aux = Aux.proximo
                Count = Count + 1
            if Aux:
                Nuevo_Nodo.proximo = Aux.proximo
                Aux.proximo = Nuevo_Nodo


    def MostrarDatos(self):

        Datos = []
        Aux = self.Inicio

        while Aux:
            Datos.append(Aux.datos)
            Aux = Aux.proximo
        return Datos
    
    def EliminarDatoPosicion(self, posicion):
        if not self.Inicio:
            return None
        
        if posicion == 0:
            self.Inicio = self.Inicio.proximo
        else:
            Aux = self.Inicio
            Atras = Aux
            Count = 0
            while (Aux != None):
                if posicion == Count:
                    Atras.proximo=Atras.proximo.proximo
                    return print("Finalizado")
                else:
                    Atras = Aux
                    Aux = Aux.proximo
                    Count = Count + 1
                    return print("Finalizado")

    def MostrarPosicion(self, posicion):
        if posicion == 0:
            Aux = self.Inicio
            Mostrar = Aux.MostrarNodo()
            return Mostrar
        else:
            Aux = self.Inicio
            Count = 0
            while Aux != None:
                if Count == posicion:
                    Dato = Aux.MostrarNodo()
                    return Dato
                else:
                    Aux = Aux.proximo
                    Count = Count + 1


class NodoDoble:
    def __init__(self, Datos):
        self.dato = Datos
        self.Proximo = None
        self.Previo = None
    
    def MostrarDato(self):
        return self.dato
    
class ListaDobleEnlazada:
    def __init__(self):
        self.Inicio = None
        self.Final = None
    
    def AgregarDatosInicio(self, datos):

        Nuevo_Nodo = NodoDoble(datos)

        if self.Inicio == None:
            self.Inicio = self.Final = Nuevo_Nodo
        else:
            Nuevo_Nodo.Proximo = self.Inicio
            self.Inicio.Previo = Nuevo_Nodo
            self.Inicio = Nuevo_Nodo

    def AgregarDatosFinal(self, datos):

        Nuevo_Nodo = NodoDoble(datos)
        Nuevo_Nodo.Proximo = None
        Final = self.Inicio

        if self.Inicio == None:
            Nuevo_Nodo.Previo = None
            self.Inicio = Nuevo_Nodo
        while Final.Proximo != None:
            Final = Final.Proximo
        Final.Proximo = Nuevo_Nodo
        Nuevo_Nodo.Previo = Final 
    
    def AgregarDatoPosicion(self, datos, posicion):

        Nuevo_Nodo = NodoDoble(datos)

        if self.Inicio == None:
            self.Inicio = self.Final = Nuevo_Nodo
        elif posicion == 0:
            Nuevo_Nodo.Proximo = self.Inicio
            self.Inicio.Previo = Nuevo_Nodo
            self.Inicio = Nuevo_Nodo
        else:
            Aux = self.Inicio
            Count = 0
            while (Aux != None):
                if posicion == Count:
                    Nuevo_Nodo.Previo = Aux.Previo
                    Nuevo_Nodo.Proximo = Aux
                    if Aux.Previo != None:
                        Aux.Previo.Proximo = Nuevo_Nodo
                    else:
                        self.Inicio = Nuevo_Nodo
                    Aux.Previo = Nuevo_Nodo
                    return True
                else:
                    Aux = Aux.Proximo
                    Count = Count + 1
            return True
        
    def MostrarDatos(self):
        Aux = []
        if self.Inicio == None:
            print("Lista Vacia")
        else:
            Temporal = self.Inicio
            while Temporal != None:
                Aux.append(Temporal.dato)
                Temporal = Temporal.Proximo
            return Aux

    def EliminarDatoPosicion(self, posicion):
        if self.Inicio == None:
            print("Lista Vacia")
        elif posicion == 0:
            self.Inicio = self.Inicio.Proximo
            if self.Inicio != None:
                self.Inicio.Previo = None
            else:
                self.Final = None
        else:
            Aux = self.Inicio
            Count = 0
            while (Aux != None):
                if posicion == Count:
                    if Aux.Previo != None:
                        Aux.Previo.Proximo = Aux.Proximo
                    else:
                        self.Inicio = Aux.Proximo
                    return True
                else:
                    Aux = Aux.Proximo
                    Count = Count + 1
            return True
        
    def MostrarPosicion(self, posicion):
        if posicion == 0:
            Datos = self.Inicio.MostrarDato()
            return Datos
        else:
            Aux= self.Inicio
            Count = 0
            while (Aux != None):
                if Count == posicion:
                    Dato = Aux.MostrarDato()
                    return Dato
                else:
                    Aux = Aux.Proximo
                    Count = Count + 1  

    def MostrarDatosInvertido(self):
        Aux = []
        if self.Inicio == None:
            print("Lista Vacia")
        else:
            Temporal = self.Inicio
            Final = self.Inicio
            while (Temporal != None):
                Final = Temporal
                Temporal = Temporal.Proximo
            while (Final != None):
                Aux.append(Final.dato)
                Final = Final.Previo
            return Aux

    