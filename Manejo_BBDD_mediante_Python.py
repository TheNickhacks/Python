# -*- coding: utf-8 -*-
"""
Created 18/07/2023
Created by:
    TheNickhacks;
"""
def menu():
    print("""
-----Ingreso de datos-----
[1] Agregar Cliente a Adoptar #Ejemplo
[1] Agregar Sucursal
[2] Ingresar Mascota Rescatada #Ejemplo
[2] Agregar Personal de trabajo
[3] Agregar Partners #Ejemplo
[3] Agregar Pacientes
[4] Agregar Aporte Monetario #Ejemplo
[4] Agregar Receta de Lentes #Ejemplo

-----Consulta de datos-----
[5] Agregar Adopción #Ejemplo
[5] Buscar Paciente Por Rut
[6] Agregar Tratamientos #Ejemplo
[6] Buscar Receta Por ID
[7] Agregar Ficha Medica Mascota #Ejemplo
[7] Buscar Sucursal de Origen de la Receta

[8] Conocer la Cantidad de Mascotas que se Pueden Mantener #Ejemplo
[9] Conocer la Cantidad de Mascotas Rescatadas #Ejemplo
[10] Verificar Que Animales Van al Corral Municipal #Ejemplo
[11] Generar un Aviso para los Partners, Cuyo Compromiso Vencerá Pronto #Ejemplo
[S] Salir del programa         
""")

#Función Auxiliar 1
# 8)
def Capacidad(conn):
  cur=conn.cursor()
  query="""
  select count("Id_Mascota") from public."Registro_Mascota"
  """
  #print(query)
  cur.execute(query)
  fila=cur.fetchone()
  c=fila[0]
  print(c)
  cur.close()    
  conn.commit()
  return c

#Función Auxiliar 2
# 9)
def CantidadMascotas(conn):
   cur=conn.cursor()
   query="""
   select sum("Monto") from public."Aporte"
   """
   cur.execute(query)
   fila=cur.fetchone()
   Aux=fila[0]
   Cantidad=Aux/10000
   cur.close()
   conn.commit()
   print(Cantidad)
   return Cantidad

#Función Borrar Mascota
def borrarMascota(idmascota,conn):
    cur=conn.cursor()
    query=f"""
    select "Nombre_Mascota", "Especie_Mascota" from public."Registro_Mascota" 
    where "Id_Mascota" = {idmascota}
    """
    cur.execute(query)
    # Borrar el cliente
    cur=conn.cursor()
    queryu=f"""
    delete from public."Ficha_Medica" 
    where "Id_Mascota" = {idmascota}
    """
    cur.execute(queryu)
    cur.close()
    conn.commit()

    cur=conn.cursor()
    query=f"""
    delete from public."Registro_Mascota" 
    where "Id_Mascota" = {idmascota}
    """
    cur.execute(query)
    cur.close()    
    conn.commit()
    print("Enviado al Corral Correctamente")

#Sección Para Insertar Datos en el Sistema (Insert into)

#AgregaCliente(conn)
# 1)
def AgregaCliente(conn):
    nombre=input("Ingrese el nombre: ")
    Rut=input("Ingrese el Rut (Sin Puntos ni Guión): ")
    Telefono=input("Ingrese Numero de Telefono: ")
    Email=input("Ingrese Email (Opcional): ")
    Direccion=input("Ingrese Dirección: ")

    cur=conn.cursor()    
    query=f"""insert into  public."Cliente" ("Rut_Cliente", "Nombre_Cliente", "Telefono", "Email", "Direccion") 
    values ('{Rut}','{nombre}','{Telefono}','{Email}','{Direccion}')"""
    #print(query)
    cur.execute(query)
    cur.close()    
    conn.commit() 
    print("Cliente Agregado Correctamente") 

#AgregaRescate(conn)
# 2)
def AgregaRescate(conn):
    print("Ejemplo Id: 001")
    cm=int(input("Ingrese la id de la mascota: "))
    Nm=input("Ingrese el nombre de la mascota: ")
    edadm=input("Ingrese la edad de la mascota: ")
    especie=input("Ingrese Especie de la mascota: ")
    raza=input("Ingrese la raza: ")
    fechaIngreso=input("Ingrese Fecha de llegada (MM-DD-YYYY): ")
  
    cur=conn.cursor()    
    query=f"""insert into  public."Registro_Mascota" ("Id_Mascota", "Edad_Mascota", "Nombre_Mascota", "Especie_Mascota", "Raza_Mascota", "Fecha_Ingreso" ) 
    values ('{cm}','{edadm}','{Nm}','{especie}','{raza}','{fechaIngreso}')"""
    #print(query)
    cur.execute(query)
    cur.close()    
    conn.commit()  
    print("Animal Rescatado con Exito") 

#AgregaPartner(conn)
# 3)
def AgregaPartner(conn):
    RutP=input("Ingrese rut, sin puntos ni guión: ")
    nombrep=input("Ingrese Nombre: ")
    telefonop=input("Ingrese numero de telefono: ")
    emailp=input("Ingrese Email (Opcional): ")
    Monto_Mensualp=input("Ingrese Monto Mensual a Donar: ")
    fechaIniciop=input("Ingrese Fecha de inicio de donación (MM-DD-YYYY): ")
  
    cur=conn.cursor()    
    query=f"""insert into public."Partner" ("Rut_Partner", "Nombre_Partner", "Telefono", "Email", "Monto_Mensual", "Fecha_Inicio" ) 
    values ('{RutP}','{nombrep}','{telefonop}','{emailp}','{Monto_Mensualp}','{fechaIniciop}')
    """
    #print(query)
    cur.execute(query)
    cur.close()    
    conn.commit()

    print("Partner Creado exitosamente")

#AgregaAporte(conn)
# 4)
def AgregaAporte(conn):
    print("Ejemplo Numero Aporte (003)")
    Nap=int(input("Ingrese el numero del aporte: "))
    Rutd=input("Ingrese rut, sin puntos ni guión: ")
    fechaA=input("Ingrese Fecha de donación (MM-DD-YYYY): ")
    Montod=input("Ingrese monto de donación: ")
    partner=input("¿Es Usted Partner Registrado? (Si/No): ")
    if partner=="Si" or partner=="si":
      partner=True
    elif partner=="No" or partner=="no":
      partner=False 

    cur=conn.cursor()    
    query=f"""insert into  public."Aporte" ("N_Aporte", "Rut_Donante", "Fecha_Aporte", "Monto", "¿Partnert?" ) 
    values ('{Nap}','{Rutd}','{fechaA}','{Montod}','{partner}')"""
    #print(query)
    cur.execute(query)
    cur.close()    
    conn.commit()

    print("Aporte Agregado con exito")

#AgregaAdopcion(conn)
# 5)
def AgregaAdopcion(conn):
    print("Formato Id Adopcion (001) ")
    cad=int(input("Ingrese Id de adopción: "))
    idm=input("Ingrese Id de Mascota a adoptar: ")
    Rutca=input("Ingrese Rut de persona quien adoptará: ")
    fechaa=input("Ingrese fecha en la que se adoptará (MM-DD-YYYY): ")
      
    cur=conn.cursor()    
    query=f"""insert into public."Adopcion" ("Cod_Adopcion", "Id_Mascota", "Rut_Cliente", "Fecha_Adopcion" ) 
    values ('{cad}','{idm}','{Rutca}','{fechaa}')"""
    #print(query)
    cur.execute(query)
    cur.close()    
    conn.commit()
    R=input("¿Desea hacer un aporte monetario para apoyar a la fundación? (Si/No)")
    
    print("Mascota Adoptada Exitosamente")
    if R=="Si" or R=="si":
      AgregaAporte(conn)
    else:
      print("Que tenga buen día")
    
    #borrarMascota(conn)
    print("Mascota Adoptada con exito")

#AgregaTratamiento
# 6)
def AgregaTratamiento(conn):
    print("Formato Numero de Tratamiento (001) ")
    ct=int(input("Ingrese Numero de Tratamiento"))
    Descripcion=input("Ingrese el tratamiento: ")
    montot=input("Ingrese el monto del tratamiento: ")

    cur=conn.cursor()    
    query=f"""insert into  public."Tratamiento" ("Cod_Tratamiento", "Descripcion", "Monto_Tratamiento") 
    values ('{ct}','{Descripcion}','{montot}')"""
    #print(query)
    cur.execute(query)
    cur.close()    
    conn.commit()
    print("Tratamiento Agregado con exito") 

#AgregaFicha(conn)
# 7)
def AgregaFicha(conn):
    print("Formato Numero de Ficha (001) ")
    cfm=int(input("Ingrese Numero de Ficha"))
    idfm=input("Ingrese Id de Mascota: ")
    Codt=input("Ingrese el Cod de tratamiento: ")
    det=input("Ingrese el nombre del tratamiento: ")
    
    cur=conn.cursor()    
    query=f"""insert into  public."Ficha_Medica" ("Id_Ficha", "Id_Mascota", "Cod_Tratamiento", "Detalles" ) 
    values ('{cfm}','{idfm}','{Codt}','{det}')"""
    #print(query)
    cur.execute(query)
    cur.close()    
    conn.commit()
    print("Ficha Creada con exito")

#Sección Para Consultar Datos y Generar Avisos (query´s)

#10 def Corral(conn)
def Corral(conn):
  cur=conn.cursor()
  query="""
  select "Id_Mascota","Nombre_Mascota",(Extract(month from Current_date))-(Extract(month from "Fecha_Ingreso"))
  from public."Registro_Mascota"
  where (Extract(month from Current_date))-(Extract(month from "Fecha_Ingreso"))>3
  """
  cur.execute(query)
  fila=cur.fetchone()
  print("Los siguientes animales van a corrales municipales por exceder el tiempo de 3 meses:")
  while fila is not None:
    if cur.rowcount==0:
      print("No hay animales por enviar")
    else:
      print(fila)
      resp=fila[0]
      print("\n")
      borrarMascota(resp,conn)
      fila=cur.fetchone()
          #    if cur.rowcount==0:
#        print("No se encuentra el id", idCliente)

  cur.close()    
  conn.commit()

#11 def Aviso(conn)
def Aviso(conn):
  cur=conn.cursor()
  query="""
  select "Rut_Partner","Nombre_Partner", Current_date-"Fecha_Inicio" as "Resta"
  from public."Partner"
  where Current_date-"Fecha_Inicio">=358
  """
  cur.execute(query)
  fila=cur.fetchone()
  while fila is not None:
    print(f"La suscripción al Partner de {fila[1]} está pronta a finalizar")
    fila=cur.fetchone()
  cur.close() 

# Programa principal (Basado en Programa Visto en Clases)
import sys
sys.path.insert(0, "../..")
import psycopg2
clave="obyw94485%#"
usuario="lmachucaw"
conn=psycopg2.connect(host="34.121.224.106", database="lmachucaw",user=usuario,password=clave)

while True:
    menu()
    opcion=input("Ingrese el comando: ")
    if opcion=="1":
        AgregaCliente(conn)
    elif opcion=="2":
        AgregaRescate(conn)
    elif opcion=="3":
        AgregaPartner(conn)
    elif opcion=="4":
        AgregaAporte(conn)
    elif opcion=="5":
        AgregaAdopcion(conn)
    elif opcion=="6":
        AgregaTratamiento(conn)
    elif opcion=="7":
        AgregaFicha(conn)
    elif opcion=="8":
        CantidadMascotas(conn)
    elif opcion=="9":
        Capacidad(conn)
    elif opcion=="10":
        Corral(conn)
    elif opcion=="11":
        Aviso(conn)
    elif opcion=="12":
        listarPeliculas(conn)
    elif opcion=="13":
        listarPeliculas(conn)
    
    elif opcion=="s" or opcion=="S":
        print("Fin Programa")
        print("------------")
        print("-------------")
        print("--------------")
        break
