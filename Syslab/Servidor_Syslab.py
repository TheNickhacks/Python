#Sistema Finalizado
import socket
import signal
import os
from datetime import datetime
import configparser

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