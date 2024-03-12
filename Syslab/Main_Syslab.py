#Created By: The_Nickhacks02

import socket #Biblioteca para Trabajar con los Puertos de Conexion
import signal #Biblioteca para Realizar acciones con las señales entrantes al dipositivo
import os #Biblioteca para Acceder a Funciones Naturales del Sistema Operativo
from datetime import datetime #Biblioteca para Extraer datos Temporales del Reloj
import configparser #Biblioteca para Leer Archivos de Extension .Ini
import importlib
import time #Biblioteca para Controlar el Tiempo de Espera

aux=-1 #Variable Auxiliar para Trabajar con un Sistema de Menú de Selección
while (aux != 0): #Menú Intuitivo
    print("\nOpcion 1: Validar Puerto Abierto/Cerrado") #Finalizado
    print("Opcion 2: Verificar Puertos Abiertos y Disponibles") #Finalizado
    print("Opcion 3: Enviar Mensaje por Puerto Especifico") #Finalizado
    print("Opcion 4: Convertir Maquina en Servidor") #Finalizado
    print("Opcion 5: Leer Mensajes HL7 ORU") #Finalizado
    print("Opcion 0: Finalizar el Programa") #Nativo

    aux = int(input("\n Ingrese su Opcion--> ")) #Elegir la Opcion para Trabajar

    if(aux == 1): #Backend de Opcion 1
        #Validador de Puerto Abierto/Cerrado
        print("--------------------Validar Puerto--------------------")
        DIp = input("Ingrese Direccion IpV4 del equipo--> ")
        Puerto = int(input("Ingrese Puerto de Interes--> "))
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM) #Establece el Tipo de Direccion Ip y la Conexion Bidireccional TCP
        sock.settimeout(1)  # Establece un Tiempo de Espera Corto para la Conexión
        try:
            sock.connect((DIp,Puerto)) #Funcion que Establece una Conexion con el Puerto
            print("El Puerto:",Puerto," en la Direccion Ipv4:",DIp," está Abierto") #Si hay Conexion Significa que el Puerto esta Abierto
        except socket.error:
            print("El Puerto:",Puerto," en la Direccion Ipv4:",DIp," está Cerrado") #Si no hay Conexion Significa que esta Cerrado el Puerto
        finally:
            sock.close() #Cierra la Conexion para que se Mantenga Abierto el Puerto.

    elif(aux==2): #Funcion para Verificar los Puertos Abiertos y Disponibles
        RangoI = int(input("Ingrese Rango Inferior para Busqueda de Puertos Abiertos--> "))
        RangoS = int(input("Ingrese Rango Superior para Busqueda de Puertos Abiertos--> "))
        Ip=input("Ingrese Direccion IpV4 del equipo--> ")
        ogR = range(RangoI, RangoS) #Rango de la Busqueda de Puertos
        Puertos_Disp = []
        for puerto in ogR:
            sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM) #Establece el Tipo de Direccion Ip y la Conexion Bidireccional TCP
            sock.settimeout(1) # Establece un Tiempo de Espera Corto para la Conexión
            resultado = sock.connect_ex((Ip, puerto)) #Realiza la Conexion Entre los Puertos y Entrega Valor 0

            if (resultado == 0):
                Puertos_Disp.append(puerto) #Agrega El Puerto a la Lista
            sock.close() #Cierra la Conexion

        if Puertos_Disp:
            print("Puertos abiertos en",Ip,"-->",Puertos_Disp) #Entrega la Ip y los Puertos Abiertos en Forma de Lista
        else:
            print("No se encontraron puertos abiertos en ",Ip) #Mensaje de que No hay Puertos Abiertos

    elif(aux==3): #Conexion por Puerto Especifico y Envio de Informacion
        DIp = input("Ingrese Direccion IpV4 del Servidor--> ")
        Puerto = int(input("Ingrese Puerto para Conexion--> "))
        Variante=input("¿Desea Enviar un Archivo?--> ")
        Variante= Variante.upper()

        if(Variante == "SI"):
            with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as cliente: #Establece el Tipo de Direccion Ip y la Conexion Bidireccional TCP
                try:
                    # Intentar conectar al servidor
                    cliente.connect((DIp, Puerto))
                    MensajeA = "ARCHIVO"
                    cliente.sendall(MensajeA.encode('utf-8'))
                except ConnectionRefusedError:
                    print("Error: No se pudo establecer conexión con el servidor.")

            print("Datos para enviar el archivo")
            Ruta = input("Ingrese Ruta del Archivo a Enviar--> ")

            def enviar_archivo(DIp, Puerto, Ruta):
                with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as cliente:
                    try:
                        cliente.connect((DIp, Puerto))
                        print("Conexión establecida con el servidor de Ip",DIp,"en el Puerto",Puerto)

                        # Enviar nombre del archivo al servidor
                        Nombre_A = os.path.basename(Ruta)
                        cliente.sendall(Nombre_A.encode('utf-8'))

                        # Enviar el contenido del archivo al servidor
                        with open(Ruta, 'rb') as archivo:
                            for datos in iter(lambda: archivo.read(1024), b''):
                                cliente.sendall(datos)

                        print("Archivo",Nombre_A," enviado exitosamente.")

                    except ConnectionRefusedError:
                        print("Error: No se pudo establecer conexión con el servidor.")

            enviar_archivo(DIp, Puerto, Ruta)

        elif(Variante == "NO"):
            with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as cliente: #Establece el Tipo de Direccion Ip y la Conexion Bidireccional TCP
                try:
                    # Intentar conectar al servidor
                    cliente.connect((DIp, Puerto))
                    Menaux="MENSAJE"
                    cliente.sendall(Menaux.encode('utf-8'))
                except ConnectionRefusedError:
                    print("Error: No se pudo establecer conexión con el servidor.")
            time.sleep(2)

            Mensaje = input("Ingrese su Mensaje a Enviar--> ")
            with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as cliente: #Establece el Tipo de Direccion Ip y la Conexion Bidireccional TCP
                try:
                    # Intentar conectar al servidor
                    cliente.connect((DIp, Puerto))
                    print("Conexión establecida con la Ip,",DIp," y el Puerto",Puerto)

                    # Enviar datos al servidor
                    cliente.sendall(Mensaje.encode('utf-8'))
                    print("---------Mensaje Enviado Exitosamente---------")
                except ConnectionRefusedError:
                    print("Error: No se pudo establecer conexión con el servidor.")
        else:
            print("\nOpcion no Valida")

    elif(aux==4): #Backend para Iniciar Servidor y Escuchar un Puerto Especifico
        # Variable global para indicar si el servidor debe detenerse
        Apagar_Server = False

        def manejar_interrupcion(signum, frame):
            #global Apagar_Server
            print("\n Recibida Señal de Detención. Deteniendo el Servidor...")
            Apagar_Server = True

        def generar_nombre_archivo():
            # Generar un nombre único basado en la fecha y hora actual
            fecha_hora_actual = datetime.now().strftime("%Y%m%d%H%M%S")
            nombre_archivo = f"HL7_ORU_{fecha_hora_actual}"
            return nombre_archivo

        def recibir_archivo(conexion, directorio):
            datos = conexion.recv(8192).decode('latin-1')
            if not datos:
                Apagar_Server = True
                print("\n Conexion cerrada",Apagar_Server )

            # Recibir el nombre del archivo
            nombre_archivo = generar_nombre_archivo() + ".res"
            print("\n Archivo en Transmision: ",nombre_archivo)
            if not nombre_archivo:
                return

            # Crear un directorio para cada archivo
            ruta_directorio = os.path.join(directorio).replace('\\','/') #Ojo Aqui

            #ruta_directorio = os.path.join(directorio, nombre_archivo)
            print("\n Archivo por Guardar en: ",ruta_directorio)

            os.makedirs(ruta_directorio, exist_ok=True) #Verificacion de que el directorio existe

            # Crear y escribir el archivo en el directorio
            ruta_archivo = os.path.join(ruta_directorio, nombre_archivo)
            print("\n Direccion del Archivo a Guardar: ",ruta_archivo)
            #print("\n Datos Almacenados en el Archivo",datos)
            

            #open text file
            text_file = open(ruta_archivo, "w")
            #write string to file
            n = text_file.write( datos )
            #close file
            text_file.close()
            sop = ""
            Auxiliar = datos.splitlines()
            for linea in Auxiliar:
                campo = linea.split('|')
                if campo[0] == 'MSH':
                    mensaje_id = campo[6]
                    sop = mensaje_id
                    
            Mensaje = (
                        f"MSH|^~\\&|ReceivingApp|ReceivingFacility|SendingApp|SendingFacility|"
                        f"{datetime.now().strftime('%Y%m%d%H%M%S')}||ACK^R01|{sop}|P|2.5||||||latin-1|||NE\r"
                        f"MSA|AA|{sop}|\r")
            
            conexion.sendall(Mensaje.encode('latin-1'))
            print(Mensaje,":", nombre_archivo)

        def iniciar_servidor(puerto, directorio):
            global Apagar_Server
            # Configurar el manejador de señales para Ctrl+C
            signal.signal(signal.SIGINT, manejar_interrupcion)

            # Crear un socket IPv4 y TCP
            with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as servidor:
                # Enlazar el socket a la dirección y puerto especificados
                servidor.bind(('0.0.0.0', puerto))
                print("Servidor Escuchando el Puerto", puerto)
                # Establecer el servidor en modo de escucha
                servidor.listen()
                conexion, direccion_cliente = servidor.accept()
                print("Conexión Establecida desde", direccion_cliente)
            
                while not Apagar_Server:
                    # Establecer el servidor en modo de escucha
                    try:

                        # Iniciar la recepción de archivos en el directorio especificado
                        recibir_archivo(conexion, directorio)
                    except socket.error as e:
                        print("Error en la Conexion: ",e)
                        Apagar_Server = True

        if __name__ == "__main__":
            Parametros = configparser.ConfigParser()
            Parametros.read('Config.ini')

            Puerto = int(Parametros.get('Servidor','Puerto'))
            Directorio = Parametros.get('Servidor','Directorio')
            iniciar_servidor(Puerto, Directorio)

    elif(aux==5): #Funcion para Leer Mensajes ORU Almacenados en Archivos

        def leer_archivo_hl7(ruta_archivo):
            try:
                with open(ruta_archivo, 'r') as archivo:
                    contenido = archivo.read()
                    return contenido
            except FileNotFoundError:
                print(f'Error: No se encontró el archivo {ruta_archivo}')
                return None

        def Lectura_Hl7 (Mensaje):
            Auxiliar = Mensaje.split('\n')
            for linea in Auxiliar:
                campo = linea.split('|')
                #dkk9285
                if campo[0] == 'PID':
                    print("\nDatos Segmento PID")
                    print("ID Paciente: ", campo[3])
                    print("Nombre Paciente: ", campo[5])
                    print("Fecha de Nacimiento: ", campo[7])
                    print("Genero: ", campo[8])

                elif campo[0] == 'OBR':
                    print("\nDatos Segmento OBR")
                    print("Identificador Orden: ", campo[2])
                    print("Identificador Lugar: ", campo[3])
                    print("Identificador Analisis: ", campo[4])

                elif campo[0] == 'OBX':
                    print("\nDatos Segmento OBX")
                    print("Resultado Examen: ", campo[5])
                    print("Resultado Examen: ", campo[6])

        if __name__ == "__main__":
             # Cambia la ruta del archivo según tu necesidad
            ruta = input("Ingrese Ruta del Archivo Almacenado--> ")
            # Lee el contenido del archivo
            mensaje_hl7 = leer_archivo_hl7(ruta)
            if mensaje_hl7:
                # Procesa el mensaje HL7 como cadena de texto
                Lectura_Hl7(mensaje_hl7)

    elif(aux==0): #Backend para Finalizar el software
        print("\nFin Programa")
        print("-----------------------------------------------")

    else: #LLega aquí Cuando la Opcion Seleccionada no es Valida
        print("\nOpcion no Valida")
        print("-----------------------------------------------")