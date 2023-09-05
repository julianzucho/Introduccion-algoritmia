'''Ingresar por teclado la longitud de dos listas, lista1 y lista2
Cada longitud debe estar entre 10 y 20
Validar este dato
Completar cada lista con valores aleatorios entre 1 y 30
Mostrar ambas listas
Obtener una lista3, que resulta ser la unión de la lista1 y la lista2. Unión significa que no hay valores repetidos en la lista3
O sea, si en la lista1 hay un 1, y en la lista2 hay otro 1, en cualquier orden, en la lista3 solo se agregar un 1
Y obtener una lista4 que resulta ser la intersección de la lista1 y la lista2, o sea, solo pasan a la lista4 los elementos comunes en ambas listas (uno solo)
Mostrar las listas resultados obtenidas'''
def repite(a,b):
    for i in range (len(a)):
        if a[i]==b:
            return 1
    return 0



import random 
lista1=[]
lista2=[]
lista3=[]
lista4=[]
pos=0
longitud1=int(input('Ingrese la longitud de la primera lista entre 10 y 20 :'))
longitud2=int(input('Ingrese la longitud de la segunda lista entre 10 y 20:'))

while (longitud1<10 or longitud1>20) or (longitud2<10 or longitud2>20):
    print('Error, la longitud debe estar entre 10 y 20')
    longitud1=int(input('Ingrese la longitud de la primera lista entre 10 y 20 :'))
    longitud2=int(input('Ingrese la longitud de la segunda lista entre 10 y 20:'))


for i in range(longitud1):
    lista1.append(random.randint(1,30))

for i in range(longitud2):
    lista2.append(random.randint(1,30))



### Ordeno las listas 

for i in range (len(lista1)-1):
    for j in range (i+1,len(lista1)):
        if lista1[i]>lista1[j]:
            aux=lista1[i]
            lista1[i]=lista1[j]
            lista1[j]=aux

for i in range (len(lista2)-1):
    for j in range (i+1,len(lista2)):
        if lista2[i]>lista2[j]:
            aux=lista2[i]
            lista2[i]=lista2[j]
            lista2[j]=aux

print('Lista 1:',lista1)
print('Lista 2:',lista2)

### Busco los valores repetidos y los agrego a la lista 3

for i in range (len(lista1)):
    resul1=repite(lista3,lista1[i])
    if resul1==0:
        lista3.append(lista1[i])



for i in range (len(lista2)):
    resul1=repite(lista3,lista2[i])
    if resul1==0:
        lista3.append(lista2[i])
     
### Ordeno lista 3

for i in range (len(lista3)-1):
    for j in range (i+1,len(lista3)):
        if lista3[i]>lista3[j]:
            aux=lista3[i]
            lista3[i]=lista3[j]
            lista3[j]=aux

print('Lista 3:',lista3)


### Busco los valores repetidos y los agrego a la lista 4

for i in range (len(lista1)):
    resul1=repite(lista2,lista1[i])
    if resul1==1:
        lista4.append(lista1[i])

print('Lista 4:',lista4)