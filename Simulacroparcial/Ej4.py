'''Ingresar 2 números e informar si son números amigos

Son números amigos aquellos números cuya suma de divisores de uno, sin el propio número, es igual al otro, y viceversa .
Ej 220 y 284 son amigos'''




suma=0
sumb=0
        


num1=int(input('Ingrese un valor:'))
num2=int(input('Ingrese otro valor:'))

for i in range (num1):
    i=i+1
    if num1%i==0 and i!=num1 :
        suma=suma+i
        
    if num2%i==0 and i!=num2 :
        sumb=sumb+i
        

if suma==num2 and sumb==num1:
        print('Los numeros ingresados son amigos')
else:
    print('Los numeros estan peleados a muerte, no son amigos ')





