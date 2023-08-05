import funcionCalcularCostoDelivery as FCCD
import funcionCalcularCostoProductos as FCCP
def calcularCostoTotal(CCompletos,CBebidaC,CBebidaM,CBebidaG,CHamburguesa,CPapas,CEmpanadas,CNuggets,comunaIngresada):

    #Calculo de costo total sumando los costos de los productos y el delivery
    costoTotal = FCCP.calcularCostoProductos(CCompletos,CBebidaC,CBebidaM,CBebidaG,CHamburguesa,CPapas,CEmpanadas,CNuggets) + FCCD.calcularCostoDelivery(comunaIngresada)

    #Retorna el costo total de la compra   
    return costoTotal
