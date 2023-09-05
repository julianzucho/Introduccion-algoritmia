
#Ej 1
"""Leer números que representan edades de un grupo de personas, 
finalizando la lectura cuando se ingrese el número -1. 
Imprimir cuántos son menores de 18 años, cuántos tienen 18 años o más y el promedio de edad de ambos grupos. 
Descartar valores que no representan una edad válida. (Se considera válida una edad entre 0 y 100).

edad=int(input("Ingresa una edad:"))

menores=0
mayores=0
promMayor=0
promMenor=0
cont=0

while edad!=-1:
    if edad<18 and edad>0:
        menores = menores+1
        cont=cont+1
    elif edad>=18 and edad<100:
        mayores=mayores+1
        cont=cont+1
    else:
        print("Edad invalida")
    edad=int(input("Ingresa una edad:"))
promMayor=mayores*100/cont
promMenor=menores*100/cont

print("Hay",menores,"Menores de edad y su pormedioes:",promMenor)
print("Hay",mayores,"Mayores de edad y su pormedioes:",promMayor)
"""
#Ej 2
#Escribir un programa que permita ingresar los números de legajo de los alumnos de un curso y su nota de examen final. 

#El fin de la carga se determina ingresando un -1 en el legajo. 
#Informar para cada alumno si aprobó o no el examen considerando que se aprueba con nota mayor o igual a 4. 
#Se debe validar que la nota ingresada sea entre 1 y 10. 
#Terminada la carga de datos, informar:
#Cantidad de alumnos que aprobaron con nota mayor o igual a 4.
#cantidad de alumnos que desaprobaron el examen con nota menor a 4.
#Porcentaje de alumnos que están aplazados (tienen 1 en el examen).

"""numlegajo=int(input("Ingrese el numero de legajo:"))
notafin=int(input("Ingrese la nota del final:"))
aprobados=0
desaprobados=0
aplazados=0
promaplazados=0
cont=0
while numlegajo!=-1:
    
    

    if notafin>=0 and notafin<=10:
            
        if notafin>=4:
            aprobados=aprobados+1
            cont=cont+1
            print("El alumno",numlegajo,"Aprobo con una nota de",notafin)
        
        elif notafin==1:
            aplazados=aplazados+1
            cont=cont+1
            desaprobados=desaprobados+1
        
        elif notafin<4:
            desaprobados=desaprobados+1
            print("El alumno",numlegajo,"Desaprobo con una nota de",notafin)
            cont=cont+1
        

    numlegajo=int(input("Ingrese el numero de legajo:"))
    if numlegajo!=-1:    
        notafin=int(input("Ingrese la nota del final:"))
    

print(aprobados,"Alumnos tienen un nota mayor o igual a 4")
print(desaprobados,"Alumnos tienen un nota menor a 4")
print(aplazados*100/cont, "Alumnos que fuero aplazados")
"""

#Ej 3
"""Una empresa aplica el siguiente procedimiento en la comercialización de sus productos
    Aplica el precio base a la primera docena de unidades.
    Aplica un 10% de descuento a todas las unidades entre 13 y 100.
    Aplica un 25% de descuento a todas las unidades por encima de las 100.

    Por ejemplo, supongamos que vende 230 unidades de un producto cuyo precio base es 100. 
    El cálculo resultante sería:
    100 * 12 + 90 * 88 + 75 * 130 = 18870 y el precio promedio es de 18870/230 = 82.04

    Escribir un programa que lea la cantidad solicitada de un producto y su precio base, 
    y muestre el valor total de la venta y el precio promedio por unidad. 
    El fin de carga se determina ingresando -1 como cantidad solicitada. 
    Al finalizar informar :

    Cantidad de ventas realizadas total.

    Cantidad de ventas en las que se aplicó un 10% de descuento.

    Cantidad de ventas en las que SOLO se aplicó el precio base, es decir que no se le realizaron descuentos.

cantidad=int(input("Ingrese la cantidad solicitada (-1 para finalizar): "))
precio_base = float(input("Ingrese el precio base del producto: "))
ventas_totales = 0
ventas_con_descuento = 0
ventas_con_descuento10=0
ventas_sin_descuento = 0
promdeprecio=0
while cantidad != -1:
    if cantidad <= 12:
        venta = cantidad * precio_base
        ventas_sin_descuento += 1
    elif cantidad <= 100:
        venta = (12 * precio_base) + ((cantidad - 12) * precio_base * 0.9)
        ventas_con_descuento += 1
        ventas_con_descuento10 +=1
    else:
        venta = (12 * precio_base) + (88 * precio_base * 0.9) + ((cantidad - 100) * precio_base * 0.75)
        ventas_con_descuento += 1
    ventas_totales += venta
    promdeprecio= ventas_totales/cantidad
    print("Valor total de la venta: ", ventas_totales)
    print("Precio promedio por unidad: ",promdeprecio)
    
    cantidad = int(input("Ingrese la cantidad solicitada (-1 para finalizar): "))
print("Valor total de la venta: ", ventas_totales)
print("Precio promedio por unidad: ", promdeprecio)
print("Cantidad de ventas realizadas total: ", ventas_sin_descuento + ventas_con_descuento)
print("Cantidad de ventas en las que se aplicó un 10% de descuento: ", ventas_con_descuento10)
print("Cantidad de ventas en las que SOLO se aplicó el precio base: ", ventas_sin_descuento)
"""


#Ej 4
#Una empresa factura a sus clientes el último día de cada mes. 
#Si el cliente paga su factura dentro de los primeros 10 días del mes siguiente, 
#tiene un descuento de $200 o del 2% de la factura, lo que resulte más conveniente para el cliente. 
#Si paga en los siguientes 10 días del mes deberá pagar el importe original de la factura,
#mientras que si paga después del día 20 deberá abonar una multa de $350 o del 10% de su factura, lo que resulte mayor. 
#Escribir un programa que lea el número del cliente y el total de la factura, 
#y emita un informe donde cons-te el número del cliente y los tres importes que podría abonar según la fecha de pago.

# si paga en los primero 10 dias descuento de $200 o 2% lo que le sirva al cliente
#entre  10 y 20 dias del mes paga la factura completa 
#despues del 20 dias paga una multa de $350 o 10% de de la factura lo que sea mas grande

"""cliente = int (input("Ingrese el numero de cliente:"))
factura = int (input("Ingrese el total de la factura:"))
descuento = 0
multa = 0

if factura >= 200:
    descuento = 200
elif factura >= 2:
    descuento = factura * 0.02
if factura*0.1> factura+350:    
     multa = factura * 0.1
else:
    multa = 350


print("El cliente", cliente, "puede pagar:")
print("El importe original de la factura: $", factura)
print("El importe con descuento: $", factura - descuento)
print("El importe con multa: $", factura + multa)"""


#Ej 5

"""Leer tres números D, M y A correspondientes al día, mes y año de una fecha, 
y un número entero N que representa una cantidad de días. 
Realizar un programa que imprima la nueva fecha que resulta de sumar N días a la fecha dada. 
Tener en cuenta los años bisiestos tal como se detalla en el ejercicio 7 de la práctica 3."""


"""
dias=int(input("Ingresa un dia:"))
mes=int(input("Ingresa un mes:"))
anio=int(input("Ingresa un año:"))


cantdias= int(input("Ingresa un valor:"))

if mes==2 and anio % 4 == 0:
    if dias + cantdias>=29:
        dias= dias+cantdias-29
        mes=mes+1
        print("El anio es viciesto")
elif mes==2 and anio % 4 != 0:
    if dias + cantdias>28:
        dias= dias+cantdias-28
        mes=mes+1

elif dias + cantdias>30:
    dias= dias+cantdias-30
    mes=mes+1
    if mes > 12:
        mes=mes-12
        anio=anio+1
        
else:
    dias=dias+cantdias

print("La nueva fecha es:",dias,"/",mes,"/",anio)"""


#Ej 6

"""Leer un número entero y mostrar un mensaje informando cuántos dígitos contie-ne. 
Tener en cuenta que el número puede ser negativo. 
Ejemplo: Si se ingresa 12345 se debe imprimir 5."""

"""  
num=int(input("Ingresa un valor:"))

cantdigitos=0
digitos=1
for i in range (num):
    if num<0:
        num=num*-1

    elif num<digitos:

        break       
    else:
        cantdigitos=cantdigitos+1
        digitos=digitos*10
        

print("El numero tiene",cantdigitos,"digitos")
print(num)
"""

#Ej 7

"""Leer un número entero e invertir las cifras que contiene. 

Imprimir por pantalla el número invertido. 
Tener en cuenta que el número puede ser negativo. 
Por ejemplo, si se ingresa 1234 debe mostrar 4321.
"""


"""
num=int(input("Ingresa un valor:"))
num2=0
if num<0:       
    num=num*-1
    while num>0:
        num2=num2*10+num%10
        num=num//10
    num2=num2*-1
else:
    while num>0:
        num2=num2*10+num%10
        num=num//10
print("El numero invertido es:",num2)
"""


#Ej 8







#Ej 9

'''Ingresar un número N y validar que sea positivo. 
Luego:
a.Mostrar los primeros números impares, hasta alcanzar el número ingresado.
b.Informar la suma de esos números impares.

Ejemplo:∑Si se ingresa 5, se debe mostrar 1 3 5 y la suma es 9.

∑Si se ingresa 8, se debe mostrar 1 3 5 7 y la suma es 16.

∑Si se ingresa -5, se debe pedir otro número.'''

'''num=int(input('Ingrese un  numero:'))
suma=0
if num>0:
    for i in range(num+1):

        if i%2!=0:
            print(i)
            suma=suma+i
    print('La suma de los numeros impares es:',suma)
else:
    print('Error toque f5 para reintentar')'''


#Ej 10











