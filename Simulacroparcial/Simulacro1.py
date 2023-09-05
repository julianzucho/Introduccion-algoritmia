'''Generar la serie de Fibonacci hasta la posición 40

Informar cuantos valores hay múltiplos de 3, entre las posiciones 12 a 30

Mostrarlos junto con su posición'''


a,b,pos,mult=1,1,2,0


for i in range (40+1):
    c=a+b
    
    
    if c%3==0 and pos>12 and pos<30:
        mult=mult+1
        print(c, ' ',pos)
    pos=pos+1
    a=b
    b=c
print('Existen', mult,'Multiplos de 3')
print()