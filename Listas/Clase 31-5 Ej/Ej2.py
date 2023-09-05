'''Dado la lista  FIBO, generar y cargar en ella, la sucesión de Fibonacci,
 siendo los dos primeros valores de la sucesión el cero (0) y el (1). 
Detener el proceso cuando se detecte un número con raíz cuadrada exacta,
 a partir de la posición 10, o se llegue a la posición 20, lo que ocurra primero 
Para determinar si el valor generado tiene raíz exacta, deberá hacerlo programando una función.
 No puede utilizar ni sqrt ni elevar a la ½  

Informar en que posición se detiene la sucesión 

 

 

Ejercicio 2 

Generar aleatoriamente una serie de valores OBLONGOS, comprendidos entre 15 y 450, y cargarlos a una lista. La carga de la lista finalizará cuando se detecte que se hayan cargados 30 valores oblongos  
Ordenar ésta de menor a mayor por Burbujeo 
Ingresar un nuevo valor por teclado, validar que el valor ingresado se encuentre dentro del rango indicado, y buscarlo  en la lista por búsqueda binaria. Mostrar un mensaje de error si no se encuentra y permitir el ingreso de un nuevo valor a buscar 
Nro Oblongo: Es un valor que surge como el producto de dos números consecutivos. 
EJ: 20=4*5 – 42=6*7 – 56=7*8 '''


def raiz(a):
    aprox=0
    
    while aprox*aprox < a:
        aprox =aprox +1
    
    
    if aprox*aprox== a:
        return 0
    




fibo=[0,1]
flag,i=0,2
while flag==0 and i<=20:
    num=fibo[i-2]+fibo[i-1]
    if i>=10:
        
        resul=raiz(num)
        
        if resul==0:
            flag=1
            fibo.append(num)
             
        else:
            fibo.append(num)
    else:
        fibo.append(num)
        
    
    i=i+1 
print('La lista es',fibo)
print('Se detiene en la posicion',i-1)  




########  Ej 2
'''Generar aleatoriamente una serie de valores OBLONGOS, comprendidos entre 15 y 450, y cargarlos a una lista.
La carga de la lista finalizará cuando se detecte que se hayan cargados 30 valores oblongos  
Ordenar ésta de menor a mayor por Burbujeo 
Ingresar un nuevo valor por teclado, validar que el valor ingresado se encuentre dentro del rango indicado,
 y buscarlo  en la lista por búsqueda binaria. 
 Mostrar un mensaje de error si no se encuentra y permitir el ingreso de un nuevo valor a buscar 
Nro Oblongo: Es un valor que surge como el producto de dos números consecutivos. 

EJ: 20=4*5 – 42=6*7 – 56=7*8 '''


import random
lista=[]
while len(lista)<30:
    val1=random.randint(1,450)
    val2=val1+1
    oblongo=val1*val2
    if oblongo>=15 and oblongo<=450:
        lista.append(oblongo)


print('La lista es',lista)


for j in range (len(lista)-1):
    for i in range (len(lista)-1):
        if lista[i]>lista[i+1]:
            aux=lista[i]
            lista[i]=lista[i+1]
            lista[i+1]=aux

print('La lista ordenada es',lista)


busca=int(input('Ingrese un codigo de producto:'))
min,max,flag,pos=0,len(lista)-1,0,0
while flag!=1:
    
    while min<=max and flag==0:
        medio=(min+max)//2
        if busca==lista[medio]:
            flag=1
            pos=medio
        elif busca<lista[medio]:
            max=medio-1
        else:
            min=medio+1

    if flag!=0:
        print('El valor se encuentra en la posicion',pos+1)
    else:   
        print('El valor no esta')
        busca=int(input('Ingrese un codigo de producto:'))
        min,max,flag,pos=0,len(lista)-1,0,0

