#Importe de funciones externas
import csv
import random

#Solicitud de contraseña
Contrasena = input("Ingrese Contraseña -->")

#Apertura de excel con la base de datos
csv_file = open('Lista.csv','r')
csv_reader = csv.reader(csv_file)

Lista_Contrasenas = ["password","123456","123456789","guest","qwerty","12345678","111111","12345","col123456","123123","1234567","1234","1234567890","0","555555",
                     "666666","123321","654321","7777777","123","D1lakiss","777777","110110jp","1111","987654321","121212","Gizli","abc123","112233","azerty",
                     "159753","1q2w3e4r","54321","pass@123","222222","qwertyuiop","qwerty123","qazwsx","vip","asdasd","123qwe","123654","iloveyou","a1b2c3",
                     "Gruod2013","1q2w3e","usr","Liman1000","1111111"]
#Validador que verifica la contraseña en la base de datos
Contrasena_lista = False
for i in len(Lista_Contrasenas) :
    if Contrasena == Listas_Contrasenas[i] :
        Contrasena_lista = True
        break
    else :
        Contrasena_lista =False
        break

#Validador de espacios
while " " in Contrasena :
    print("No se debe ingresar espacios en la contraseña.")
    Contrasena = input("Ingrese Contraseña -->")

#Generador automatico de contraseñas
if Contrasena_lista == False :
    #Funciona Bien
    Letras = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPRQSTUVWXYZ"
    Numeros = "0123456789"
    Caracteres = "*_-!&@"
    Union = f"{Letras}{Numeros}{Caracteres}"
    Longitud = random.randit (8, 60)
    Contrasena  random.sample (Unir, Longitud)
    Contrasena_Final = "".join(Contrasena)
    print("La contraseña ingresada no es segura, pertenece al top 50 mas usadas en el mundo")
    print("Se ha generado una contraseña mas segura -->", Contrasena_Final)
elif Contrasena_lista == True:
    #Contraseña que no esta dentro del top 50
    print("La contraseña es segura.")
    print("Contraseña Valida.")
else :
    pass
#Cierre de Base de datos
csv_file.close()
    
    
