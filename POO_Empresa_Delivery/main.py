import funcionCalcularCostoProductos as FCCP
import funcionCalcularCostoDelivery as FCCD
import funcionCalcularCostoTotal as FCCT
import funcionCantidadProductos as FCP
import funcionProductos as FP
import funcionPrecioT as FPT

#Variables a utilizar
terminar = 2
CCompletos = 0
CBebidaC = 0
CBebidaM = 0
CBebidaG = 0
CHamburguesa = 0
CPapas = 0
CEmpanadas = 0
CNuggets = 0

#Pedido de comuna al usuario
comunaIngresada = str(input("Ingrese la comuna de destino ---] "))

#Pedido de productos a comprar
print("Ingrese cantidad a comprar de cada producto")
while(terminar == 2):
    Completos=int(input("Completos ---] "))
    BebidaC=int(input("Bebida Chica ---] "))
    BebidaM=int(input("Bebida Mediana ---] "))
    BebidaG=int(input("Bebida Grande ---] "))
    Hamburguesa=int(input("Hamburguesa ---] "))
    Papas=int(input("Papas fritas ---] "))
    Empanadas=int(input("Empanadas ---] "))
    Nuggets=int(input("Nuggets ---] "))
    CCompletos = CCompletos + Completos
    CBebidaC = CBebidaC + BebidaC
    CBebidaM = CBebidaM + BebidaM
    CBebidaG = CBebidaG + BebidaG
    CHamburguesa = CHamburguesa + Hamburguesa
    CPapas = CPapas + Papas
    CEmpanadas = CEmpanadas + Empanadas
    CNuggets = CNuggets + Nuggets
    terminar = int(input("Desea finalizar el pedido?\n1)Si\n2)No\n"))

#Variables pedidas de las funciones
costoProductos = FCCP.calcularCostoProductos(CCompletos,CBebidaC,CBebidaM,CBebidaG,CHamburguesa,CPapas,CEmpanadas,CNuggets)
costoEnvio = FCCD.calcularCostoDelivery(comunaIngresada)
costoTotal = FCCT.calcularCostoTotal(CCompletos,CBebidaC,CBebidaM,CBebidaG,CHamburguesa,CPapas,CEmpanadas,CNuggets,comunaIngresada)
Cantidad = FCP.cantidadProductos(CCompletos,CBebidaC,CBebidaM,CBebidaG,CHamburguesa,CPapas,CEmpanadas,CNuggets)
Productos = FP.productos(CCompletos,CBebidaC,CBebidaM,CBebidaG,CHamburguesa,CPapas,CEmpanadas,CNuggets)
PrecioT = FPT.precioT(CCompletos,CBebidaC,CBebidaM,CBebidaG,CHamburguesa,CPapas,CEmpanadas,CNuggets)

print("El costo de los productos es ---] ",costoProductos)
print("El costo de envio es ---] ",costoEnvio)
print("El costo total fue ---] ",costoTotal)


#Creacion de la boleta
boleta = open("Boleta.txt","w")
boleta.write("------------------------------------------\n")
boleta.write("\n")
boleta.write("Delivery MHBtarken\n")
boleta.write("Comuna Destino: ")
boleta.write(comunaIngresada)
boleta.write("\n")
boleta.write("Dueños: Catalina Gonzalez, Nicolas Navarro\n")
boleta.write("ID: 00201032\n")
boleta.write("\n")
boleta.write("Detalle de la venta:\n")
boleta.write("\n")
boleta.write("******************************\n")
boleta.write("Producto -- Cantidad -- Precio\n")
boleta.write("******************************\n")
boleta.write("\n")
for i in range(0,len(Productos)):
    boleta.write(Productos[i])
    boleta.write(" -- ")
    boleta.write(str(Cantidad[i]))
    boleta.write(" -- ")
    boleta.write("$")
    boleta.write(str(PrecioT[i]))
    boleta.write("\n")

boleta.write("\n")
boleta.write("Envio -- $")
boleta.write(str(costoEnvio))
boleta.write("\n")
boleta.write("Valor final: $")
boleta.write(str(costoTotal))
boleta.write("\n")
boleta.write("\n")
boleta.write("------------------------------------------\n")
boleta.close()













