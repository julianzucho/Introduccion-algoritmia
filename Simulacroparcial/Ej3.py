'''Realizar un algoritmo que ingrese primero la cantidad de empleados de la empresa y a continuación el sueldo de cada uno

Informar

Cantidad de sueldos mayores a 15000

Cuantos sueldos hay entre 12000 y 20000

Sueldo máximo

Generar los valores con un numero random'''

cantemp=int(input("Ingrese la cantidad de empleados que tiene la empresa:"))
sueldo=0
sueldo15=0
sueldoentre=0
sueldomax=0
pos=0
import random
for i in range (cantemp):
    pos=pos+1
    
    sueldo=random.randint(1200,100000)
    print(sueldo)

    if sueldo>sueldomax:
        sueldomax=sueldo
        sueldo15=sueldo15+1
    
    elif sueldo>=15000 and sueldo<20000:
        sueldo15=sueldo15+1
        sueldoentre=sueldoentre+1
    
    elif sueldo>=15000:
        sueldo15=sueldo15+1
        


    elif sueldo>=12000 and sueldo<=20000:
        sueldoentre=sueldoentre+1

print('El sueldo maximo es de',sueldomax)
print('Hay',sueldo15,'Cantidad de empleados que cobran mas de $15000')
print('Hay',sueldoentre,'Cantidad de empleados que ganan entre 12000 y 20000')