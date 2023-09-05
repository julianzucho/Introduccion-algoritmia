'''Escribir una función para ingresar desde el teclado una serie de números entre A y B y guardarlos en una lista.
En caso de ingresar un valor fuera de rango la fun-ción mostrará un mensaje de error y solicitará un nuevo número. 
Para finalizar la carga se deberá ingresar -1.

 La función recibe como parámetros los valores de A y B, 
 y devuelve la lista cargada (o vacía, si el usuario no ingresó nada) como valor de retorno. 
 Tener en cuenta que A puede ser mayor, menor o igual a B.'''



def ingresar_numeros(A, B):
    numeros = []
    num = 0
    num = int(input("Ingrese un número: "))
    while num!=-1:
        if num < A or num > B:
            print("El número ingresado está fuera de rango. Intente nuevamente.")
        else:
            numeros.append(num)
        num = int(input("Ingrese un número: "))

    return numeros

def es_capicua(lista):
    for i in range(len(lista) // 2):
        if lista[i] != lista[-i - 1]:
            return False
    return True


def repetido(lista, a):
     for i in range (len(lista)):
          if lista[i]==a:
               return 1
     
# Programa principal
numeros=[]
suma=0
A = int(input("Ingrese el valor de A: "))
B = int(input("Ingrese el valor de B: "))
print("Ingrese un numeor entre")
numeros = ingresar_numeros(A, B)

for i in range (len(numeros)):
        suma=suma+numeros[i]
        i=i+i


resul=es_capicua(numeros)
if resul==True:
     print('La lista es capicua')
else:
     print('No es capicua')

valrepetido=int(input('Ingrese un valor para chequear:'))

valor=repetido(numeros,valrepetido)

if valor == 1:
    print('El valor se encuentra en la lista')
print('La suma de los numeros es',suma)
print("Los números ingresados son:", numeros)

