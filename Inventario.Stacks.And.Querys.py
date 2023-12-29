class Pelicula():
    def __init__(self, Id, Titulo, Copias):
        self.Id = Id
        self.Titulo = Titulo
        self.Copias = Copias

class Arriendo():
    def __init__(self, Id_Pelicula, Rut_Arrendador, Fecha_Arriendo):
        self.Id_Pelicula = Id_Pelicula  
        self.Rut_Arrendador = Rut_Arrendador
        self.Fecha_Arriendo = Fecha_Arriendo

class VideoClub ():
    def __init__ (self):
        self.peliculas =[]
        self.arriendos =[]
        self.retrasos =[]
    
    def Agregar (self, Pelicula): #Agrega pelicula al videoclub y a la lista de peliculas
        Aux = len(self.peliculas)
        self.peliculas.append(Pelicula)
        if(Aux == len(self.peliculas)):
            print("La Pelicula No Fue Agregada")
        else:
            print("Pelicula Agregada Correctamente")
    
    def Mostrar_Pelicula(self): #muestra las peliculas que estan en la lista self.peliculas
        for i in self.peliculas:
            print("ID:",i.Id, ", Titulo ->",i.Titulo, ", N° Copias ->",i.Copias)

    def Arrendar(self, Id, Rut, Fecha): #Agrega a la clase arriendo los datos y quita una copia de la clase videoclub, de la lista self.peliculas
        for i in self.peliculas:
            if(i.Id == Id and i.Copias > 0):
                i.Copias = i.Copias - 1
                Uso = Arriendo(Id, Rut, Fecha)
                self.arriendos.append(Uso)
                print("Pelicula Arrendada Exitosamente")
            elif(i.Id == Id and i.Copias == 0):
                print("Copias Insuficientes Para el Arriendo")
    
    def Devolver_Arriendo(self, Id, Rut): #agrega la copia que se quito en self.peliculas
        for i in self.arriendos:
            if(i.Id_Pelicula == Id and i.Rut_Arrendador == Rut):
                self.arriendos.remove(i)
                for j in self.peliculas:
                    if(j.Id == Id):
                        j.Copias = j.Copias + 1
                        print("Devolucion Completa")
            else:
                print("La Pelicula no Fue Devuelta")

    def Mostrar_Arriendos(self): #Muestra la lista self.arriendos
        for i in self.arriendos:
            print("Id:",i.Id_Pelicula,", Rut Arrendador ->",i.Rut_Arrendador,", Fecha Arriendo ->", i.Fecha_Arriendo)

    def Ajuste_Inventario(self): #elimina las peliculas que no tengan copias en la lista self.peliculas
        print("----Seccion Verificacion de Inventario----")
        for i in self.peliculas:
            if(i.Copias == 0):
                print("La Pelicula Con el Id:", i.Id," Sera Eliminada Por Falta de Inventario")
                self.peliculas.remove(i)
        print("----")
        print(" ")
        print("----Seccion Verificacion de Retrasos----") #Hacer codigo para restar meses con la fecha que se entrega a self.arriendos
        print("----")
        print(" ")
        print("----Seccion Varias----") #Hacer codigo para las peliculas mas arrendadas y las menos arrendadas
        print("----")

Video = VideoClub()
Pelis = Pelicula(1, "La Era del Hielo", 5)
Pelid = Pelicula(2, "Jurassic Park", 3)
Pelit = Pelicula(3, "Pacific Rim", 15)
#Agregamos Peliculas a self.peliculas
print(" ")
Video.Agregar(Pelis)
Video.Agregar(Pelid)
Video.Agregar(Pelit)

print("\n Peliculas en Inventario")
Video.Mostrar_Pelicula()

print("\n Arriendo de Peliculas")
Video.Arrendar(2, 122596348, "17/11/23")
Video.Arrendar(2, 142521618, "17/08/23")
Video.Arrendar(2, 142369633, "17/01/23")
print("\n Peliculas en Arriendo")
Video.Mostrar_Arriendos() #muestra las peliculas que estan en self.arriendos

#Video.Devolver_Arriendo(2, 122596348) #Funcion para devolver una de las peliculas solo con el id y el rut
print(" ")
Video.Ajuste_Inventario() #Muestra las funciones varias
print(" ")
print("Peliculas en Inventario del VideoClub")
Video.Mostrar_Pelicula() #Muestra las peliculas en el Videoclub
