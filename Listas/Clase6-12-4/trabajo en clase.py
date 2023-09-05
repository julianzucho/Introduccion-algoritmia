#Funciones
#No devuelve ningun resultado
#Se la usa para mostrar un titulo

"""Desarrolle una funcion para que muestre un cartel de bienvenida a la clase de funciones
"""
"""
def cartel():
    print("Bienvenido a  la clase de funciones")
    



cartel()
print("Fin")"""

#Devuelve resultado al programa principal
"""Desarrolle una funcion para que reciba un dato desde teclado e informe si el valor es par

def espar(a):
    if a%2==0:
        print("Es par")
    else:
        print("No es par")
    
num=int(input("Ingrese un valor:"))
espar(num)"""

"""Desarrolle una funcion para que reciba un dato desde el teclado e informe si el valor es par o impar
El resultado se debe informar en el programa principal

def espar(a):
    if a%2==0:
        return 1
    else:
        return 2
    
num=int(input("Ingrese un valor:"))
res=espar(num)
if res==1:
    print("Es par")
else:
    print("No es par")"""


"""Generar 80 numeros entre 10 y 90 
informar cuantos valores impares salieron
La deteccion del valor impar lo deben hacer en la funcion

def impar(a):
    
    if a%2!=0:
        return 1

import random
imp=0
for i in range (80):
    val=random.randint(10,90)
    print(val,end=" ")
    res=impar(val)
    if res==1:
        imp=imp+1
    
print()
print("salieron ",imp,"numero pares")"""


#Generar 80 numeros entre 10 y 90 
#informar cual fue el mayor y cual fue el menor valor de la serie

"""        

import random


numMenor=91
numMayor=0

for i in range (80):
    val=random.randint(10,90)
    print(val,end=" ")
    
    if val<numMenor:
       numMenor=val
    if val>numMayor:
        numMayor=val
    
    
print()
print("El valor mas chico es:",numMenor)
print("El valor mas grande es:",numMayor)"""


#Ej 
"""num=int(input("Ingrese un valor:"))
div=1
cont=0

for i in range (1,num+1):
    if num%div==0:
        cont=cont+1
    div=div+1
if cont<=2:
    print(num,"Es primo")
else:
    print(num,"No es primo")
"""

#Ejercicio de fibonacci
#Generar la sucesion de fibonacci hasta la pos 25"""

"""a,b=1,1
print(a,b,end=" ")
for i in range (2,26):
    c=a+b
    print(c,end=" ")
    
    a=b
    b=c"""


#Ejercicio de fibonacci
#Generar la sucesion de fibonacci hasta la pos 25"""
#Determinar cuantos valores primos hay en la serie, a partir de la pos 5

"""a,b,primos=1,1,0

print(a,b,end=" ")
for i in range (2,26):
    c=a+b
    if i>=5:
        div,cont=1,0
        while div<=c:
            if c%div==0:
                cont=cont+1
            div=div+1
        if cont<=2:            
            print(c,end=" ")
            primos=primos+1
    a=b
    b=c
print()
print("Salieron",primos,"valores primos")"""


#Ejercicio de fibonacci
#Generar la sucesion de fibonacci hasta la pos 25"""
#Determinar cuantos valores primos hay en la serie, a partir de la pos 5
#Si el valor es primo, lo debe determinar una funcion
"""def primo(val):
    
    
    div,cont=1,0
    while div<=val:
        if val%div==0:
            cont=cont+1
        div=div+1
    if cont<=2:            
        print(val,end=" ")
        return 1

    

a,b,primos=1,1,0

print(a,b,end=" ")
for i in range (2,26):
    c=a+b
    if i>=5:
        res=primo(c)
        if res==1:
            primos=primos+1
    a=b
    b=c
print()
print("Salieron",primos,"valores primos")"""


#Generar 90 valores comprendidos entre 5 y 120
# informar
# 1- cuantos valores son numeros deficientes
# 2- que porcentaje representa este resultado sobre el total de datos
#Numero deficiente: Es todo numero en donde la suma de los divisores propios, sin considerar el mismo numero, es menor al numero
#Ej:8>1+2+4




  
import random
deficientes=0
for i in range (90):
    num=random.randint(5,120)
    div,suma=1,0
    while div<num:
        if num%div==0:
            suma=suma+div
        div=div+1
    if suma<num:
        print(num,end=" ")
        deficientes=deficientes+1
print()
print(deficientes, " Son numeros deficientes")
print("El porcentaje es de",deficientes*100/90)
