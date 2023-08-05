def calcularCostoDelivery(comunaIngresada):
    numero = []
    comuna = []
    delivery = 0
    verificacion = 'a'
    comunas = []
    #Lectura de archivo de PrecioPorComuna
    with open('PrecioPorComuna.txt', 'r', encoding='utf8') as f:
        #Division de lineas para sacar el numero y las comunas solas
        lineas = [linea.split() for linea in f]

    #Extraer el numero de su respectiva comuna, se guarda en orden
    for linea in lineas:
        numero.append(linea[len(linea)-1])

    #Extraer la comuna, como estas se encuentran con numero('Til','Til','1'), se saca el numero('Til', 'Til')
    for linea in lineas:
        unaComuna = []
        for i in range(0,len(linea)-1):
            unaComuna.append(linea[i])
            ' '.join(unaComuna)
            comuna.append(unaComuna) 
        
    #Se borran comunas repetidas
    resultado = []
    for i in comuna:
        if i not in resultado:
            resultado.append(i)

    #Se juntan los nombres de las comunas que tengan mas de una palabra ('Til','Til') ---] ('Til Til')
    for unacomuna in resultado:
        ver =' '.join(unacomuna)
        comunas.append(ver)

    #Se verifica que numero pertenece a la comuna ingresada
    while(verificacion != comunaIngresada):
        for i in range(0,len(comunas)):
            if(comunaIngresada == comunas[i]):
                delivery = numero[i]
                verificacion = comunaIngresada

    #Costos de delivery dependiendo de numero de comuna
    if delivery == '1':
        costoEnvio = 1500

    elif delivery == '2':
        costoEnvio = 2000

    elif delivery == '3':
        costoEnvio = 2500

    elif delivery == '4':
        costoEnvio = 4000

    #Retorna costo de envio
    return costoEnvio
