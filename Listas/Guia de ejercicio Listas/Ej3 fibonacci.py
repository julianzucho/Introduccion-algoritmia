'''Generar la serie de Fibonacci hasta la posición 30 

Una vez generada la serie, recorrerla, y a partir de la posición 17,
 determinar si el valor que se encuentre en posiciones primas (por ej, posición 17, posición 19,  …) es abundante 

Por fin de proceso, informar a cuantos valores se les hizo este proceso 

Para determinar si la posición es primo, se usará una función, la cual llamará a otra función para determinar si el número es abundante, en el caso de que la posición sea primo 

Debe enviarse elemento a elemento a la función. No se puede enviar la lista completa'''

def esprimo(val):
    div=1
    cont=0
    while div<=val:
        if val%div==0:
            cont=cont+1
        div=div+1
    if cont==2:
        return 0
        
        
def abundante(val):
    div,suma=1,0
    while div<val:
        if val%div==0:
            suma=suma+div
            div=div+1
        if suma>val:
            return 1
        


a,b=1,1
lista=[0,1]
abund=[]
for i in range (2,30):
    c=a+b
    lista.append(c)
    a=b
    b=c
    print(c,end=", ")
print()
print (lista)


for i in range (len(lista)):
    if i>=17:
        resul=esprimo(i)
        if resul==0:
            print(i)
            resul2=abundante(lista[i])
            if resul2==1:
                abund.append(lista[i])
    
print(abund)