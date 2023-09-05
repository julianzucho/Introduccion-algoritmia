'''Generar dos listas con 20 valores aleatorios, de la siguiente manera
lista1 - valor aleatorio entre 100 y 300, siendo el código del producto
lista2 - valor aleatorio entre 0 y 100, siendo la cantidad para el código generado
Ordenar la lista1, de manera ascendente, arrastrando a la lista 2,
de manera tal que, el código siga emparentado con su respectiva cantidad 
Siendo el punto de reposición de 10 unidades, obtener una lista3, 
con el código del producto cuya cantidad se encuentre por debajo de las 10 unidades
Ingresar un código por el teclado y buscarlo en la lista3, usando la rutina de búsqueda binaria
Mostrar la lista3, con los códigos separados por 3 espacios'''


lista1=[]
lista2=[]
lista3=[]
import random
for i in range (20):
    lista1.append(random.randint(100,300))
    lista2.append(random.randint(0,100))



for i in range (len(lista1)-1):
    for j in range (i+1,len(lista1)):
        if lista1[i]>lista1[j]:
            aux=lista1[i]
            lista1[i]=lista1[j]
            lista1[j]=aux
            
            aux=lista2[i]
            lista2[i]=lista2[j]
            lista2[j]=aux
for i in range (len(lista2)):
    if lista2[i]<=10:
        lista3.append(lista1[i])

print(lista1)
for i in range (len(lista2)):
    print("",lista2[i],end=", ")
print()


for i in range (len(lista3)):
    print(lista3[i],end='   ')

busca=int(input('Ingrese un codigo de producto:'))
min,max,flag,pos=0,len(lista3)-1,0,0

while min<=max and flag==0:
    medio=(min+max)//2
    if busca==lista3[medio]:
        flag=1
        pos=medio
    elif busca<lista3[medio]:
        max=medio-1
    else:
        min=medio+1

if flag!=0:
    print('El valor se encuentra en la posicion',pos+1)
else:   
    print('El valor no esta')








