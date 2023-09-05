'''Generar la serie de Fibonacci hasta el elemento 50

Informar cuales son los valores que tienen raíz cuadrada exacta entre las posiciones 10 a 40

Para determinar la raíz cuadrada, usar el método explicado en clase'''


a,b,pos=1,1,3
entero=int

for i in range (3,50):
    c=a+b

    if pos>=10 and pos<=40 and (c**0.5)**2==c:
        print(c, ' ',pos)
    #print(c,'posicion ',pos)    
    pos=pos+1
    a=b
    b=c
print()
print()




"""Generar la serie de Fibonacci hasta el elemento 50
Informar cuales son los valores que tienen raíz cuadrada exacta entre las posiciones 10 a 40
Para determinar la raíz cuadrada, usar el método explicado en clase"""




"""a,b,pos=1,1,3

entero=int
cont=0
resta=0

x=1
for i in range (3,50):
    c=a+b
    aux=c
    if pos>=10 and pos<=40:
        #print(c,'posicion ',pos)
        cuenta=c
        while cuenta>0:
            cuenta=cuenta-x
            x=x+2
            
        if cuenta==0:
            print('La raiz de',c)
        
        
        
    #print(c,'posicion ',pos)    
    pos=pos+1
    a=b
    b=c
print()
print()"""


num1 = 0
num2 = 1
resta=0
for a in range (50):
    num3 = num1 + num2
    if a>= 10 and a <= 40:
        x = 1
        cuenta = num3
        while cuenta > 0:
            cuenta = cuenta - x
            x = x + 2
            resta=resta+1
        if cuenta == 0:
            print(num3, resta)

            
    num1 = num2
    num2 = num3
