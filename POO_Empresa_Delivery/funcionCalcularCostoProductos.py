def calcularCostoProductos(CCompletos,CBebidaC,CBebidaM,CBebidaG,CHamburguesa,CPapas,CEmpanadas,CNuggets):
    #Calcula costo de cada producto multiplicando la cantidad con el precio de estos
    PC=CCompletos*900
    PBC=CBebidaC*700
    PBM=CBebidaM*900
    PBG=CBebidaG*1100
    PH=CHamburguesa*1500
    PP=CPapas*1000
    PE=CEmpanadas*500
    PN=CNuggets*300
    total=PC+PBC+PBM+PBG+PH+PP+PE+PN

    #Retorna la suma del costo de cada producto
    return total
