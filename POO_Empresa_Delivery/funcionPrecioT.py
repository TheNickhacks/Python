def precioT(CCompletos,CBebidaC,CBebidaM,CBebidaG,CHamburguesa,CPapas,CEmpanadas,CNuggets):
    PrecioT=[]

    #Calcula el precio total por producto a partir de la cantidad
    if(CCompletos>0):
        PrecioT.append(CCompletos*900)
        
    if (CBebidaC>0):      
        PrecioT.append(CBebidaC*700)
             
    if (CBebidaM>0):       
        PrecioT.append(CBebidaM*900)     
      
    if(CBebidaG>0):       
        PrecioT.append(CBebidaG*1100)
           
    if (CHamburguesa>0):  
        PrecioT.append(CHamburguesa*1500)
           
    if(CPapas>0):
        PrecioT.append(CPapas*1000)
      
    if (CEmpanadas>0):      
        PrecioT.append(CEmpanadas*500)
     
      
    if (CNuggets>0):
        PrecioT.append(CNuggets*300)
      
    #Retorna lista con todos los precios totales por producto
    return PrecioT
