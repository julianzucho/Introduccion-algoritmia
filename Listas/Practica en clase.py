'''a=[25,12,3,4,35,10,1]

for j in range (len(a)-1):
    for i in range(len(a)-1):
        if a[i]>a[i+1]:
            aux=a[i]
            a[i]=a[i+1]
            a[i+1]=aux
    
    
print(a)'''

'''Inicilizar una lista con 5 valores cero(0)

generar dos valores aletorios 
el 1 entre 1 y 5 --- pos en la lista 
el 2 entre 100 y 1000 --- gasto diario
realizar 50 vueltas generando estos valores
cada dia puede tener varios gastos

al finalizar informar cual fue el dia que mas se gasto 
ordenar lista de mayor a menor y mostrarla  


a=[0,0,0,0,0]
mayor=0
pos=0
import random

for i in range (50):
    dia=random.randint(1,5)
    gasto=random.randint(100,1000)
    a[dia-1]=a[dia-1]+gasto

for i in range(5):
        if a[i]>mayor:
             mayor=a[i]
             pos=i
print(a)
print('El dia que mas se gasto fue',pos+1)

for j in range (len(a)-1):
    for i in range(len(a)-1):
        if a[i]<a[i+1]:
            aux=a[i]
            a[i]=a[i+1]
            a[i+1]=aux

print(a)'''

#Metodo de seleccion
'''
a=[25,12,3,4,35,10,1]
for i in range (len(a)-1):
    for j in range (i+1,len(a)):
        if a[i]>a[j]:
            aux=a[j]
            a[j]=a[i]
            a[i]=aux
print(a)
'''

'''Cargar una lista con 15 valores deficientes 
comprendidos entre 50 y 500
ordenar la lista obtenida por seleccion 
mostrar la lista obtenida

Valor deficiente: cuando la suma de los divisores es menor al numero Ej 10>1+2+5 


def deficiente(a):
    div,suma=1,0
    while div<a:
        if a%div==0:
            suma=suma+div
        div=div+1
    if suma<a:
        return 1

a=[]

import random
while len(a)<15:
    num=random.randint(50,500)
    flag=deficiente(num)
    if flag == 1:
        a.append(num)
print(a)
for i in range (len(a)-1):
    for j in range (i+1,len(a)):
        if a[i]>a[j]:
            aux=a[j]
            a[j]=a[i]
            a[i]=aux

print(a)'''



#######  Busqueda de datos en lista ######



'''Busqueda secuencial 
a=[8,3,4,5,2,1,6,7]
num=9

for i in range (len(a)):
    if num==a[i]:
        print ('el valor se encuentraen la pos' ,i)
    else:
        print('No esta en la lista')

'''

##### Busqueda binaria #######

"""La lista debe estar ordenada de menor a mayor
a=[1,2,3,4,5,6,7]

num=6

min=0
max=len(a)-1
flag=0
pos=0

while min<=max and flag==0  :
    medio=(min+max)//2

    if num ==a[medio]:
        flag=1
        pos=medio
        print('El valor se encuentra en la posicion',medio)

    elif num<a[medio]:
        max=medio-1

    else:
        min=medio+1

if flag!=0:
    print('El valor se encuentra en la posicion',pos)
else:
    print('El valor no esta ')
 """


"""Generar una lista con 20 val entre 10 y 80 no debe teener valores repetidos.
ordenar por seleccion
solicitar dato por teclado, validar que se encuentre dentro del rango 10-80 y buscarlo en la lista utilizando la lista binaria 
"""

def numigual(val,lista):
    for i in range (len(lista)):
        if val==lista[i]:
            return 1
        
def buscanum(lista):
    min,max,flag,pos=0,len(lista)-1,0,0
    val=int(input('Ingresa valor a buscar entre 10 y 80:'))

    if val>=10 and val<=80:
        while min<=max and flag==0  :
            medio=(min+max)//2

            if val ==lista[medio]:
                flag=1
                pos=medio
            elif val<lista[medio]:
                max=medio-1
            else:
                min=medio+1
        if flag!=0:
            return pos
        else:
            return-1    
    else:
        print('Valor fuera de rango')
        
import random

a=[]
while len(a)<20:
    num=random.randint(10,80)
    resul=numigual(num,a)
    if resul!=1:
        a.append(num)
print(a)

for i in range (len(a)-1):
    for j in range(i+1,len(a)):
        if a[i]>a[j]:
            aux=a[i]
            a[i]=a[j]
            a[j]=aux
print(a)

resul2=buscanum(a)
if resul2==-1:
    print('El valor no esta en la lista')
else:
    print('El valor se encuentra en la posicion',resul2)
