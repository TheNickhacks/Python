import socket
import signal
import os
import datetime

# Variable global para indicar si el servidor debe detenerse
Apagar_Server = False

def manejar_interrupcion(signum, frame):
    global Apagar_Server
    print("\nRecibida Señal de Detención. Deteniendo el Servidor...")
    Apagar_Server = True

def generar_nombre_archivo():
    # Generar un nombre único basado en la fecha y hora actual
    fecha_hora_actual = datetime.now().strftime("%Y%m%d%H%M%S")
    nombre_archivo = f"archivo_{fecha_hora_actual}"
    return nombre_archivo

def recibir_archivo(conexion):
    datos = conexion.recv(4096).decode('latin-1')
    if not datos:
        print("\n Conexion cerrada")
        return
    
    # Recibir el nombre del archivo
    nombre_archivo = generar_nombre_archivo()
    print("Archivo en Transmision: ",nombre_archivo)
    if not nombre_archivo:
        return

    # Crear un directorio para cada archivo
    ruta_directorio = os.path.join('c:\\', 'archivos').replace('\\','/')
    #ruta_directorio = os.path.join(directorio, nombre_archivo)
    print("Archivo por Guardar en: ",ruta_directorio)
    
    os.makedirs(ruta_directorio, exist_ok=True) #Verificacion de que el directorio existe

    # Crear y escribir el archivo en el directorio
    ruta_archivo = os.path.join(ruta_directorio, nombre_archivo)
    print("Direccion del Archivo a Guardar: ",ruta_archivo)
    print("Datos Almacenados en el Archivo",datos)

    #open text file
    text_file = open(ruta_archivo, "w")
    #write string to file
    n = text_file.write( datos )
    #close file
    text_file.close()

def iniciar_servidor(puerto):
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

        while not Apagar_Server:
            # Esperar a que llegue una conexión
            conexion, direccion_cliente = servidor.accept()
            print("Conexión Establecida desde", direccion_cliente)

            # Iniciar la recepción de archivos en el directorio especificado
            recibir_archivo(conexion)

if __name__ == "__main__":
    puerto_escucha = int(input("Ingrese el Puerto que se Desea Escuchar--> "))
    iniciar_servidor(puerto_escucha)