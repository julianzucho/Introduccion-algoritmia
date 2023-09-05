#Realizar un programa para ingresar desde el teclado un conjunto de números. 
#Al finalizar mostrar por pantalla el primer y último valor ingresado. 
#Finalizar la lectura con -1.

"""num1=int(input("Ingresa el numero:"))
num=[]
while num!=-1:
    num=int(input("Ingresa -1 para frenar sino,segui ingresando numeros:"))
print("El primer numero es:",num1)
print("El ultimo numero es:",num)"""

#Ej 2
#Realizar un programa para ingresar desde el teclado un conjunto de números e informar si la cantidad de elementos es impar o par,
#sin utilizar contadores. Fi-nalizar la lectura de datos con -1. 

"""num=int(input("Ingrese un numero:"))
cont=0
while num!=-1:
    cont = cont+1
    num=int(input("Ingrese un numero(Para terminar pone:-1)"))
if cont%2==0:
    print("La cantidad de datos ingresada es par")
else:
    print("La cantidad de datos ingresada es impar")"""

#Ej 3

#Ej 4
#Desarrollar un programa que imprima la suma de los números impares compren-didos entre 42 y 176.

"""num=0

for i in range (42,177):
    if i%2 != 0:
        print(i,end=", ")
    else:
        num=0"""
        
#Ej 5
#Desarrollar un programa que imprima los números naturales comprendidos entre 1 y N. 
#El valor de N se ingresa desde el teclado.

"""num=int(input("Ingresa un numero:"))
resul=0
for i in range(1,num+1):
    resul=resul+1
    print (resul)"""

#Ej 6
#Mostrar la tabla de multiplicar (entre 1 y 12) del número 4. 
#¿Cómo cambiaría el algoritmo para que el usuario pueda decidir la tabla de multiplicar a mostrar?
"""cont=0
num=int(input("Ingrese un numero:"))
for i in range(1,12+1):
    cont=cont+1
    resul=cont*num
    print(resul, end=" ")"""

#Ej 7
#Leer 10 números enteros e imprimir su promedio, 
#el mayor valor leído y en qué posición se encontraba.
#Si se ingresó más de una vez sólo debe informar la pri-mera.
"""suma, cont= 0,0
for i in range(10):
    num=int(input("Ingrese un numero:"))
    if cont==0:
        numMayor=num
        posMayor=cont
    if num>numMayor:
        numMayor = num
        posMayor = cont
    cont=cont+1
    suma = suma + num
prom=suma/10
print("\nPromedio:", prom)
print("El mayor es:", numMayor, "y su posicion es:", posMayor,"Contando 0 como primer lugar")"""


#Ej 8
#Ingresar números, hasta que la suma de los números pares supere 100. 
#Mostrar cuántos números se ingresaron en total.
"""suma=0
cont=0
while suma<100:
    num=int(input("Ingrese un numero:"))
    cont=cont+1
    if num%2==0:
        suma=suma+num
print("Se ingresaron:",cont,"Numeros")"""


#Ej 9
#Se desea analizar cuántos autos circulan con patente con numeración par y cuántos con numeración impar en un día. 
# Escribir un programa que permita in-gresar la terminación de la patente (entre 0 y 9) hasta ingresar -1
#e informe cuántos vehículos pasaron con numeración par y cuántos con numeración impar.
"""
contpar=0
contimp=0
numfin=0
while numfin!=-1:
    numfin=int(input("Ingresa el ultimo numero de tu patente: "))
    if numfin%2==0:
        contpar=contpar+1
    else:
        contimp=contimp+1
print("Hay", contpar, "de autos con patente par y" ,contimp -1, "con patente impar")"""


#Ej 10
# El factorial de un número entero N mayor que cero se define como el producto de todos los enteros X tales que 0 < X <= N.
#  Desarrollar un programa para cal-cular el factorial de un número dado. Deberán rechazarse las entradas inválidas (menores que 0).


"""
factorial = 1

numero = int(input("Ingresa un número entero mayor que cero: "))


if numero < 0:
     print("Error")
elif numero == 0:
     print("El factorial de 0 es 1")
else:
    for i in range(1, numero + 1):
        factorial=factorial*  i
     
# Calcular el factorial del número dado
resultado = factorial


print("El factorial de", numero, "es:", resultado)
"""


# Ej 11
# Realizar un programa que lea un número natural H e imprima un mensaje indi-cando si H es primo o no. 
# Se dice que un número es primo cuando sólo es divi-sible por sí mismo y por la unidad.







#Ej 12
# La sucesión de Fibonacci es una sucesión de números enteros donde cada tér-mino se obtiene como 
# suma de los dos anteriores, siendo los dos primeros 0 y 1. 
# Por lo tanto, Fib=0, 1, 1, 2, 3, 5, 8, 13, 21.... 
# Realizar un programa que lea N e imprima los N primeros términos de esta sucesión, como así también la suma de los mismos.