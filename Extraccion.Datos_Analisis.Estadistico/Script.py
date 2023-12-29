import psutil
import time
import openpyxl


# Almacenamiento de datos
Excel = openpyxl.Workbook()

hoja = Excel.active
hoja.title = "Entradas_Salidas Minimo"

hoja.append(["Iteración", "bytes enviados", "bytes recibidos", "Paquetes enviados", "Paquetes recibidos", "Total errores al recibir",
             "Total errores al enviar", "Paquetes recibidos descartados", "Paquetes enviados descartados"])


#Recoleccion de datos

Tiempo_Ejecucion = 300  #15 Minutos = 900 Segundos

T_Recolector = 15

N_para_For = Tiempo_Ejecucion // T_Recolector #Division Entera

datosRed = [] # Lista de datos

for i in range(N_para_For):
    datos = psutil.net_io_counters()
    datosRed.append(datos)
    hoja.append([i+1, datos.bytes_sent, datos.bytes_recv, datos.packets_sent, datos.packets_recv, datos.errin, datos.errout, datos.dropin, datos.dropout])
    time.sleep(T_Recolector)

for idx, datos in enumerate(datosRed): #Imprimir en consola
    print(f"Iteración {idx + 1}: {datos}")


# Almacenamiento de datos
hojad = Excel.create_sheet("Entradas_Salidas Maximo")

hojad.append(["Iteración", "bytes enviados", "bytes recibidos", "Paquetes enviados", "Paquetes recibidos", "Total errores al recibir",
             "Total errores al enviar", "Paquetes recibidos descartados", "Paquetes enviados descartados"])

for id in range(N_para_For):
    datos = psutil.net_io_counters()
    datosRed.append(datos)
    hojad.append([id+1, datos.bytes_sent, datos.bytes_recv, datos.packets_sent, datos.packets_recv, datos.errin, datos.errout, datos.dropin, datos.dropout])
    time.sleep(T_Recolector)

Nombre_Excel = "Psutil_Red_Recoleccion.xlsx"
Excel.save(Nombre_Excel)
print("Datos Guardados en --> ", Nombre_Excel)
