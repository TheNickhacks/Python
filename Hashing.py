"""
Marcelo Alcapan
Nicolas Navarro

"""

class Elemento:
    def __init__(self, s, c):
        self.s = s #String max 10 caracteres
        self.c = c #Numero Entero (casteo)
   
    def Mostrar (self):
        return self.s, self.c

class Pila:
    def __init__(self):
        self.Datos = []
        self.Nivel = 0
        self.Listas = []
  
    def Vacio(self):
       return len(self.pila)
    
    def push(self, string, casteo):
        if self.Nivel < 256:
            if self.Nivel > 0:
                for i in range(1, casteo):
                    if len(self.Listas.Nivel[i]) != 0:
                       pass
                    elif self.Nivel == casteo:
                       self.Datos[self.Nivel] = string
                       self.Listas.append(string)
        else:
           print("La lista de almacenamiento esta llena. No se puede agregar mas elementos.")

    def BuscarValor(self, string):
       if self.Vacio() == 0:
          print("La pila se encuentra vacia")
       else:
        for i in len(self.Datos):
           aux = self.Listas.Nivel
           if len(aux[i]) != 0:
              if (self.Listas == string):
                 print("El elemento ", string, "esta en el nivel ->", i)

XD=0
SumaPalabra = 0
while XD ==0:
  String = input("Ingrese una palabra de maximo 10 caracteres --> ")
 #Validador de cantidad de caracteres

  if (len(String) > 10):
      #Caso Negativo
      print("Palabra con mas de 10 caracteres")
      String = input("\n Ingrese otra palabra --> ")
   
   
  elif (len(String) <= 10):
     #Caso Positivo
      print("Palabra valida")
      suma = 0
      #Conversion palabra a numero con ASCII
      for letra in String:
          aux = ord(letra)
          aux = aux*( 128 ** suma)
          SumaPalabra = aux + SumaPalabra
          suma = suma + 1
      Casteo = SumaPalabra % 256 #Nivel de la pila
      xdd= input("¿ingresara otra palabra? 1.-SI , 2.-NO")