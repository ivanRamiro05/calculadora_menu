# Calculadora con menú

from math import log 
print("-----------------------------")
print("----Calculadora-Menu---------")
print("-----------------------------")

#input
bandera=False
x=float(input("Dame el valor  del número x: "))
y=float(input("Dame el valor  del número y: "))

print("\n dame la opción que deseas realizar: \n")
#se despliega el menu para seleccionar la opcion que deseas realizar
print("1.Sumar(el primero mas el segundo)")
print("2.Restar(el primero menos el segundo)")
print("3.Multiplicar(el primero por el segundo)")
print("4.dividir(el primero entre el segundo)")
print("5.Potenciar(el primero a la potencia  del segundo)")
print("6.Logaritmo(de el primero ")

#PROCESSING
opcion=int(input("\n Dame la opción: "))
if(opcion==1):
    z= x + y
    print(x,"+",y)
elif (opcion==2):
    z = x - y
    print(x,"-",y)
elif(opcion==3):
    z = x * y
    print(x,"X",y)
elif (opcion==4 and y!=0):
    z = x / y
    print(x,"/",y)
elif(opcion==4 and y==0):
    print("El denominador es igial a cero y")
    print("NO se puede realizar la division.")
    bandera= True
elif (opcion==5):
    z = pow(x,y)
    print(x,"^",y)
elif(opcion==6 and x>0):
    z=log(x)
    print("Logaritmo de",x)
elif(opcion==6 and x<=0):
    print("El valor de x es <= a cero y")
    print("NO se puede calcular el logaritmo. ")
else:
    print("opcion no valida ")

    # se escribe el resultado con otra condicion 
if(opcion<7 and bandera==False):
        print("Resultado =",z)

#fin

