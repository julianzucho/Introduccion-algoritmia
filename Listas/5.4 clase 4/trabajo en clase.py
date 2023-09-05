# mostrar los numeros del 1 al 10 y mostar la suma de los valores pares
"""num=1
while num<=10:
    print(num)
    num=num+1
print("fin")"""


"""import random

num,cont=3,0
while cont<100: #por conteo
    dado = random.randint(1,6)
    if dado==3:
        num=num + 1
        print(dado,end=" ")
    cont=cont+1

print("\nSalieron: ",num,"Numeros 3")"""
        
#While por evento
"""total=0
venta= int(input("Ingresa el importe del ticket:"))
while venta!=-1:
    total=total+venta
    venta= int(input("Ingresa el importe del ticket:"))

print("El total es:", total)"""
    

#Ingresa una nota entre 0,10
#Luego mostrar la nota ingresada

"""nota1 =int(input("Ingresa la primera nota: "))
#nota2 =int(input("Ingresa la segunda nota: "))

while nota1>=0 and nota1<=10:
    print(nota1)
    nota1 =int(input("Ingresa la primera nota: "))
print("pifiaste pa")"""


#For----> hacer ciclos
"""for variable in range(v1):
    print(cont,end="  ") 
cont=0
while cont<10:
    print(cont,end=" ")
    cont=cont+1
print()
print(cont)
for cont in range(0,10,2): 
    print(cont, end=" ")"""

#generar valores entre 1 y 10 
#obtener la suma de ellos y mostrarla 1+2+3
"""resultado=1
for cont in range(0,11):
    print(cont,end=" ")
    resultado=resultado+cont
print("=",resultado)
"""
"""a,b=1,1
print(a,b, end=" ")
for i in range(13):
    c=a+b
    print(c,end=" ")
    a=b
    b=c"""

#generar dos numero aleatorios 
#el 1 entre 1,4 suendo 1 oro, 2 espada,3 copa,4 basto
#el segundo es el valor de cartas 1,12
#Realizar 90 tirada de cartas

#Se pide
#mostrar cuantas veces salio el 7 de espadas
#cuantas veces salio una carta impar
#porcentaje de veces que salio el 5 de oro

import random
imp=0
cartaesp=0
cartaoro=0
for i in range(10):
    palo = random.randint(1,4)
    num = random.randint(1,12)
    print(palo,"",num)
    if palo==2 and num == 7:
        cartaesp=cartaesp + 1
        imp=imp+1
    elif palo==1 and num==5 :
        cartaoro=cartaoro+1
        imp=imp+1
           
    elif num%2!=0:
        imp=imp+1
    
    
        
    
prom5=cartaoro*100/10
print("\nSalieron:",cartaesp,"Sietes de Espadas")
print("Salieron:",imp,"cartas impares")
print("Salieron:",prom5,"%" "de 5 de oro")