
#Ej 1
#Ingresar dos números enteros e indicar si son iguales o distintos.

"""a=int(input("Ingresa el primer numero: "))
b=int(input("Ingresa el segundo numero: "))
if a == b:
    print(a ," y ",b, "son iguales")
else:
    print(a ,"y",b,  "son distintos")"""

#Ej 2
#Leer un número entero e imprimir un mensaje indicando si es par o impar.
"""
a = int(input("Ingresa un numero "))

result = a%2

if result == 0:
    print("es par")
else:
    print("el numero es impar")
"""
#Ej 3
""" meses = enero, febrero, marzo, abril, mayo, junio, julio, agosto, septiembre, octubre, noviembre, diciembre =1,2,3,4,5,6,7,8,9,10,11,12

nummes= int(input("Ingresa un numero de mes: "))

if nummes<1 or nummes>12:
    print("error")
else:
    nummes = meses[nummes-1]
    print(meses)""" 


#Ej 4

#Ingresar las notas de los dos parciales de un alumno e indicar si promocionó, aprobó o si debe recuperar.
#Informar un error si el valor de alguna nota no está entre 0 y 10
nota1 =int(input("Ingresa la primera nota: "))
nota2 =int(input("Ingresa la segunda nota: "))
if nota1<0 or nota1>10 or nota2<0 or nota2>10:
    print("error")
else:
    if nota1<4 or nota2<4:
        print("Recuperas.")
    elif nota1>=7 and nota2>=7:
        print("Felicidades promocionas.")
    else:
        print("Aprobaste pero, tenes que ir a final.")


#Ej 5
"""
encrustica = 3.20
encutela = 200
preciobase = 500
procesp = 336
cantpag = int(input("Cuantas paginas tiene el libro?: "))

if cantpag<= 300:
    prelibro = preciobase + (encrustica*cantpag)
    print("El libro cuesta $",prelibro)
elif cantpag>300 and cantpag<600:
    prelibro = preciobase + encutela + (encrustica*cantpag)
    print("El libro cuesta $",prelibro)
else:
    prelibro =procesp + preciobase + encutela + (encrustica*cantpag)
    print("El libro cuesta $",prelibro)
    """
#Ej 6
"""
viajemin = 250

kmrecor = int(input("Cuantos kilometros desea recorrer?: "))

if kmrecor>0 and kmrecor<=10 and kmrecor*30 < 250:
    print("El viaje vale $",viajemin)
elif kmrecor>0 and kmrecor<=10 and kmrecor*30 > 250:
    print("El viaje vale $",kmrecor*30)
if kmrecor>10 and kmrecor*20 < 250:
    print("El viaje vale $",viajemin)
elif kmrecor>10 and kmrecor*20 > 250:
    print("El viaje vale $",kmrecor*20)
"""
#Ej 7
"""Leer un número correspondiente a un año e imprimir un mensaje indicando si es bisiesto o no. 
Un año es bisiesto cuando es divisible por 4. Sin embargo, 
aquellos años que sean divisibles por 4 y también por 100 no son bisiestos, 
a menos que también sean divisibles por 400. Por ejemplo, 1900 no fue bisiesto pero sí el 2000.

anio = int(input("Ingrese el año:"))

if anio % 4 ==0 and anio % 100!=0:
    print("Es un año bisiesto")
elif anio % 4 == 0 and anio % 100 == 0 and anio % 400 == 0:
    print("Es un año bisiesto")
elif anio % 4 == 0 and anio % 100 == 0 :
    print("No es un año bisiesto")
else:
    print("No es un año bisiesto")
"""

#Ej 8
"""
dia = int(input("Ingresa un numero de dia:"))
mes = int(input("Ingresa un numero de mes:"))
anio= int(input("Ingresa un numero de año:"))

bisiesto = anio % 4 == 0 and (anio % 100 == 0 or anio % 400 == 0)

if mes<1 or mes>12:
    print("Fecha invalida")
elif mes==2:
    if bisiesto:
        maxdias=29
    else:
        maxdias=28
    if dia<1 or dia>maxdias:
        print("Fecha invalida")
    else:
        print("Fecha valida")
elif mes == 4 or mes== 6 or mes==9 or mes==11:
    if dia<1 or dia>30:
        print("Fecha invalida")
    else:
        print("Fecha valida")
else:
    if dia<1 or dia>31:
        print("Fecha invalida")
    else:
        print("Fecha valida")
"""

#Ej 9 

"""basico =int(input("Ingresa el sueldo base sin ningun punto:"))
antig = int(input("Ingresa la cantidad de años de antiguedad que tiene el empleado:"))
estadocivil =int(input("Ingrese 1 si el empleado esta soltero o Ingrese 2 si el empleado esta casado:"))

if estadocivil != 1 and estadocivil !=2:
    print("Error volver a iniciar")
elif estadocivil == 1:
    
    sbruto=basico+(basico * 5/100)*antig
    estadocivil ="Soltero"
elif estadocivil ==2:

    sbruto=basico+(basico * 7/100)*antig 
    estadocivil ="Casado"
jubilacion= sbruto*11/100
sbruto=sbruto-jubilacion
obrasoc =sbruto*3/100
sbruto=sbruto-obrasoc
sind  =sbruto*3/100
sbruto=sbruto-sind


print("Sueldo basico:",basico,"\nEstado civil:",estadocivil,"\n""Antiguedad:",antig,"años","\n","Descuentos:")
print("Jubilacion:",jubilacion,"\n","Obra social:",obrasoc,"\n","Sindicato:",sind,"\nSueldo neto:",sbruto)
"""




"""a=int(input("Ingresa un numero: "))
if a > 5:
    print(a, "Es mayor o igual a 5")

elif a==5:
    print(a, "Es igual a 5")

else:
    print(a, "Es menor a 5")"""

#Ingresa dos numero correspondientes a las notas de los dos parciales
#informar:
"""Si la persona recursa cuando el promedio es menor a 4,
si el promedio es mayor o igual a 4 y menor a 7 va a final 
si el promedio mayor o igual a 7 promiciona 

nota1 =int(input("Ingresa la primera nota: "))
nota2 =int(input("Ingresa la segunda nota: "))
prom = (nota1 + nota2)/2
if prom < 4:
    print("Recursas.")
elif prom >= 7:
    print("Felicidades promocionas.")
else:
    print("Tenes que ir a final.")"""

# Ingresar 3 valores correspondientes a la longiotud de los lados de un trinagulo 
#informar de que clase de trianculo se trata

"""a = int(input("Ingresa el primer lado: "))
b= int(input("Ingresa el segundo lado: "))
c= int(input("Ingresa el tercer lado: "))

if a==b & b==c:
    print("El triangulo es equilatero")
elif a!=b!=c:
    print ("El tringulo es escaleno")
else:
    print ("El tringulo es isoceles")"""


# Ingresar 3 valores correspondientes a la longiotud de los lados de un trinagulo 
#informar si los valores forman un triangulo y de que clase  se trata
"""
a = int(input("Ingresa el primer lado: "))
b= int(input("Ingresa el segundo lado: "))
c= int(input("Ingresa el tercer lado: "))
if a<b+c and b<a+c and c<a+b:
    print("Tus valores forman un triangulo")
    if a==b & b==c:
        print("El triangulo es equilatero")
    elif a!=b!=c:
        print ("El tringulo es escaleno")
    else:
        print ("El tringulo es isoceles")
else:
    print("Ingresa otro valor")"""

#se ingresa por teclado la cantidad de galletitas, queso y dulce 
#para hacer chocotorta, en kilos 
#sabiendo que cada torta consume 400gr de galletitas, 340g de queso y 125g de dulce cuantas tortas se pueden hacer con la cantidad ingresada
"""
cgalle , cqueso, cdulce = 400,340,125
galle= int(input("Ingresa el cuantos kilo de galletitas tenes: "))
queso= int(input("Ingresa el Cuantos kilos de queso tenes: "))
dulce= int(input("Ingresa el cuantos kilos de dulce tenes: "))

galle = galle*1000//cgalle
queso = queso*1000//cqueso
dulce = dulce*1000//cdulce

if  galle < queso and galle < dulce:
    print("Podes hacer: ", galle,"Tortas")

elif queso < galle and queso < dulce:
    print("Podes hacer: ", queso,"Tortas")
else:
    print("Podes hacer: ", dulce,"Tortas")
    """


