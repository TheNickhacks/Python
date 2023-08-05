print("------------------Calculadora Basica------------------")
aux=input("¿Son fracciones?--> ")

print("Simbolo +, para suma")
print("Simbolo -, para resta")
print("Simbolo x, para multiplicacion")
print("Simbolo :, para division")
op=input("Ingrese el simbolo correspondiente a la operacion a realizar--> ")

if(aux=="si" or aux=="Si"):

    a=float(input("Ingrese numerador del primer numero "))
    b=float(input("Ingrese denominador del primer numero "))
    auxu=a/b

    c=float(input("Ingrese numerador del segundo numero "))
    d=float(input("Ingrese denominador del segundo numero "))
    auxd=c/d


    if(op=="+"):
        suma=0
        suma=auxu+auxd
        print(a,"/",b,"+",c,"/",d,"= ",suma)
    elif(op=="-"):
        resta=0
        resta=auxu-auxd
        print(a,"/",b,"+",c,"/",d,"= ",resta)  
    elif(op=="x"):
        mult=0
        mult=auxu*auxd
        print(a,"/",b,"+",c,"/",d,"= ",mult)  

    elif(op==":"):
        div=0
        div=auxu/auxd
        print(a,"/",b,"+",c,"/",d,"= ",div) 

    else:
        print("Operacion Invalida")  

elif(aux=="no" or aux=="No"):
    if(op=="+"):
        a=float(input("Ingrese numero "))
        b=float(input("Ingrese numero "))
        print(a,"+",b)
        c=a+b
        print(c)    
    elif(op=="-"):
        a=float(input("Ingrese numero "))
        b=float(input("Ingrese numero "))
        print(a,"-",b)
        c=a-b
        print(c)   
    elif(op=="x"):
        a=float(input("Ingrese numero "))
        b=float(input("Ingrese numero "))
        print(a,"x",b)
        c=a*b
        print(c)   
    elif(op==":"):
        a=float(input("Ingrese numero "))
        b=float(input("Ingrese numero "))
        print(a,":",b)
        c=a/b
        print(c)  
    else:
        print("Operacion Invalida") 


