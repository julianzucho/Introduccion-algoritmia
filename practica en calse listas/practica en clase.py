#Explicacion breve 

"""cont=0
lista=[]#forma dinamica
lista=[7,5,3,6,7]# forma estatica
len(lista)



print(cont)
print(lista[2])

#posicion num entero dentro de los limites
#puede ser una formula


lista=[]
len(lista)

#Para agregar valores 
lista.append(5)
lista.append(7)# agrega valores atras del anterior

print(lista)
"""





#generar una lista con los numeros del 1 al 5 y mostrarla

"""
lista=[]

for i in range (1,6):
    lista.append(i)

for i in range (len(lista)):
    print(lista[i],end=" ")
print()
print(lista)
"""

#Generar 50 valores aleatorios comprendidos entre 10 y 200 
#Si el valor es par, agregarlo a una lista 
#mostrar la lista obtemiida y su longitud



"""
lista=[]
pares=[]
val=0
import random
for i in range(50):
     
    val=random.randint(10,200)
    
    if val%2==0:
        lista.append(val)

print(lista)
print("La longitud de la lista es de:",len(lista))
"""


#Generar 50 valores aleatorios comprendidos entre 10 y 200 y agregarlos a una lista 
#Sumar los numeros en posiciones pares  
#mostrar el resultado obtenido
 
"""
lista=[]
resul,val=0,0
import random
for i in range(50):
    val=random.randint(10,200)
    lista.append(val)
    if i%2==0:
        resul=val+resul
print(lista)
print(resul)



lista=[]
resul=0
import random
for i in range(50):
    lista.append(random.randint(10,200))
for i in range(len(lista)):
    if i%2==0:
        resul=resul+lista[i]
print(lista)
print(resul)
"""

#Generar 20 valores de la fibonacci y cargarlo a una lista 

#Mostrar la sucesion

"""
fibo=[1,1]

for i in range (2,21):
    fibo.append(fibo[i-1]+fibo[i-2])
print(fibo)
"""

#Generar una lsita con 50 valores comprendidos entre 10 y 100
#Una vez creada la lista recorrerla y Pasar a una segunda lista, aquellos valores que sean primos 
# mostrar la segunda lista creada

'''import random
lista=[]
primos=[]

def esprimo(val):
    div=1
    cont=0
    while div<=val:
        if val%div==0:
            cont=cont+1
        div=div+1
        if cont<=2:
            return 1

for i in range (0,50):
    lista.append(random.randint(10,100))

for i in range (50):
    
    primo=esprimo(lista[i])
    
    if primo==1:
        primos.append(lista[i])
print(primos)
'''

#Generar 20 valores aleatorios comprendidos entre 10 y 100 
#cargarlos en una lista 
# en la lista creada no pueden haber valores repetidos 

'''Rutina de final y de parcial'''
'''import random

lista=[]


for i in range(20):
    val=random.randint(10,100)
    if i==0:
        lista.append(val)
    else:
        j,repetido=0,0
        while j<len(lista):
            if val==lista[j]:
                repetido=1
            
            j=j+1
        if repetido!=1:
            lista.append(val)
    
print(lista)'''

#Tarea   Ej final y parcial  
'''Definir 2 listas, a y b de manera estatica. las listas deben tener una longitud igual o distinta a eleccion de cada uno
los valores ya deben estar ordenados
generar una tercera lista c mediante codigo,
de manera tal que sea la union de a y de b y que quedando ordenada a medidda que se va creando'''



a=[1,3,5,7,9,14]
b=[2,4,6,8,10,11,12,13]
c=[]
i,j=0,0


while i<len(a) and j<len(b):
    if a[i]<b[j]:
        c.append(a[i])
        i=i+1
    else:
        c.append(b[j])
        j=j+1
while i<len(a):
    c.append(a[i])
    i=i+1
while j<len(b):
    c.append(b[j])
    j=j+1
print(c)

















