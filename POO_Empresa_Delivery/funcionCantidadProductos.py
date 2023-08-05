def cantidadProductos(CCompletos,CBebidaC,CBebidaM,CBebidaG,CHamburguesa,CPapas,CEmpanadas,CNuggets):
    Cantidad=[]

    #Comprueba si la cantidad de producto es mayor a 0, si es asi lo agrega a la lista de productos
    if(CCompletos>0):
        Cantidad.append(CCompletos)
        
    if (CBebidaC>0):      
        Cantidad.append(CBebidaC)
             
    if (CBebidaM>0):       
        Cantidad.append(CBebidaM)     
      
    if(CBebidaG>0):       
        Cantidad.append(CBebidaG)
           
    if (CHamburguesa>0):  
        Cantidad.append(CHamburguesa)
           
    if(CPapas>0):
        Cantidad.append(CPapas)
      
    if (CEmpanadas>0):      
        Cantidad.append(CEmpanadas)
     
      
    if (CNuggets>0):
        Cantidad.append(CNuggets)

    #Regresa la cantidad de cada producto en una lista      
    return Cantidad
