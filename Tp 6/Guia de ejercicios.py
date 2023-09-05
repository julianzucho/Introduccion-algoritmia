#Ej1

'''Escribir una función que reciba como parámetros dos números enteros. 

Calcular y devolver el resultado de la multiplicación de ambos valores utilizando solamen-te sumas. 

Por ejemplo 4 * 3 = 4 + 4 + 4 .'''



'''def multiplicacion(a,b):
    suma=0
    
    for i in range (a):
        i=i+1
        suma=suma+b
        
    print('El resultado es:',suma)




result=0
num1=int(input('Ingrese un valor:'))
num2=int(input('Ingrese otro valor:'))

result=multiplicacion(num1,num2)'''

#Ej 2 


'''Dados dos parámetros enteros A y B,
obtener AB (A elevado a la B) mediante multiplicaciones sucesivas, 
utilizando la función del ejercicio anterior para multi-plicar. 
Por ejemplo 43 = 4 * 4 * 4.'''

'''def multiplicacion(a,b):
    suma=1
    
    for i in range (b):
        i=i+1
        suma=suma*a
        
    print('El resultado de A Elevado a B es:',suma)




result=0
num1=int(input('Ingrese valor A:'))
num2=int(input('Ingrese valor *B:'))

result=multiplicacion(num1,num2)
'''


#Ej 3

'''Imprimir una columna de asteriscos, donde su altura se recibe como parámetro
def columna(a):
    for i in range (a):
        print("*")


alt=int(input('Ingrese la altura:'))

altura=columna(alt)
'''

#Ej 4


'''Devolver True si el número entero recibido como primer parámetro es múltiplo del segundo,
o False en caso contrario. 

Ejemplo: esmultiplo(40, 8) devuelve True y esmultiplo(50, 3) devuelve False.


def esmultiplo(a,b):
    if a%b==0:
        return True
    else:
        return False

num1=int(input('Ingrese un numero:'))
num2=int(input('Ingrese un segundo numero:'))

res=esmultiplo(num1,num2)

if res==True:
    print("True")
else:
    print("False")
'''

#Ej 5 


'''Desarrollar la función signo(n), 
que reciba un número entero y devuelva 1, -1 o 0 según el valor recibido sea positivo, negativo o nulo.


def signo(n):
    if n >0:
        return "Positivo"
    elif n<0:
        return "Negativo"
    elif n == 0:
        return "Nulo"


num=int(input("Ingrese un numero:"))

res=signo(num)

print(res)
'''


#Ej 6 

'''Escribir la función comparar(a, b) que reciba como parámetros dos números en-teros

y devuelva 1 si el primero es mayor que el segundo,
0 si son iguales o 
-1 si el primero es menor que el segundo.

En este ejercicio debe aprovecharse la fun-ción del ejercicio anterior.
Ejemplo: comparar(4, 2) devuelve 1, y comparar(2, 4) devuelve -1.


def signo(a,b):
    if  a>b:
        return 1
    elif a<b:
        return "-1"
    elif a == b:
        return "0"


num1=int(input("Ingrese un numero:"))
num2=int(input("Ingrese otro numero:"))

res=signo(num1,num2)

print(res)

'''

#Ej 7 