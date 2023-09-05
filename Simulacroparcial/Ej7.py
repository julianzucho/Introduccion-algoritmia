'''Generar La sucesión de Fibonacci hasta la posición 30

Obtener y mostrar la suma de los valores ubicados en posiciones primas, a partir de la posición 3

Hacerlo con for'''




def primo(val):
    
    res=0
    div,cont=1,0
    while div<=val:
        if val%div==0:
            cont=cont+1
        div=div+1
    if cont<=2:            
        print(val,end=" ")
        
        return 1

    

a,b,primos=1,1,0
pos=0
suma=0
print(a,b)
for i in range (30):
    c=a+b
    pos=pos+1
    if pos>=3:
        res=primo(c)
        if res==1:
            suma=suma+c
            print( 'posicion',pos)
            
    a=b
    b=c
print()
print('La suma da:',suma)
