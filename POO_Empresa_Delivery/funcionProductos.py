def productos(CCompletos,CBebidaC,CBebidaM,CBebidaG,CHamburguesa,CPapas,CEmpanadas,CNuggets):
    Producto=[]
    #Comprobar si la cantidad de producto es 1 o mas, si se cumple se agrega a la lista    
    if(CCompletos>0):
        Producto.append('Completos')
        
    if (CBebidaC>0):      
        Producto.append('Bebida Chica')
             
    if (CBebidaM>0):       
        Producto.append('Bebida Mediana')     
      
    if(CBebidaG>0):       
        Producto.append('Bebida Grande')
           
    if (CHamburguesa>0):  
        Producto.append('Hamburguesa')
           
    if(CPapas>0):
        Producto.append('Papas Fritas')
      
    if (CEmpanadas>0):      
        Producto.append('Empanadas')
     
      
    if (CEmpanadas>0):
        Producto.append('Nuggets')
      
    #Retorna lista con los productos
    return Producto

