'''Generar una lista con 150 valores aleatorios entre 10 y 750 

Pasar a una segunda lista sumadig aquellos valores cuya suma de dígitos sea impar 

La determinación respecto a si la suma de los dígitos es impar debe hacerlo una función 

Informar cuantos valores con suma de dígitos impares fueron encontrados''' 


def impares(b):
    suma = 0
    
    numero=b[i]
        
    while numero > 0:
        digito = numero % 10  
        suma =suma+ digito        
        numero =numero //10         
    if suma %2 !=0:

        return 1



a=[]
sumadig=[]
suma=0
import random
for i in range (15):  
    a.append(random.randint(10,750))

    resul=impares(a)
    if resul==1:
        sumadig.append(a[i])
        suma=suma+1
print('Hubieron',suma,"Suma de digitos impares")




for j in range (len(sumadig)-1):
    for i in range(len(sumadig)-1):
        if sumadig[i]>sumadig[i+1]:
            aux=sumadig[i]
            sumadig[i]=sumadig[i+1]
            sumadig[i+1]=aux

print(sumadig)
print("Ingrese un numero en el rango de",sumadig[0],"y",sumadig[len(sumadig)-1],end="")
busca=int(input(":")) 


min,max,flag,pos=0,len(sumadig)-1,0,0

while flag!=1:
    
    while min<=max and flag==0:
        medio=(min+max)//2
        if busca==sumadig[medio]:
            flag=1
            pos=medio
        elif busca<sumadig[medio]:
            max=medio-1
        else:
            min=medio+1
            
    if flag==1:
        print('El valor se encuentra en la posicion',pos+1)
    else:
        print('El valor no se encuentra en la lista')
        busca=int(input('Ingrese un valor:'))
        min,max,flag,pos=0,len(sumadig)-1,0,0
            





