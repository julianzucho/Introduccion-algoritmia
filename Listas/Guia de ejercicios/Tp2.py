#Ej 2
"Desarrollar un programa que permita ingresar dos números enteros A y B a través del teclado. Imprimir su suma y su diferencia."
"""
a = int(input("Ingresa el primer numero entero:"))
b = int(input("Ingresa el segundo numero entero:"))
suma= a + b
resta = a-b
print("La suma es:",suma)
print("La resta es:",resta)"""



#Ej 3
"Calcular el promedio de las notas que obtiene un alumno al rendir los dos parciales."
"""par1 = int(input("Ingresa la nota del primer parcial:"))
par2 = int(input("Ingresa la nota del segundo parcial:"))

prom = (par1 + par2) /2

print("Tu promedio es:", prom)

if(prom>=7):
    print("Felicidades,promocionaste")
else:
    print("Casi capo, tenes que rendir el final")"""


#Ej 4
"""Escribir un programa que permita ingresar la edad de una persona en años y la convierta a días, 
imprimiendo el resultado. Considerar que to-dos los años tienen 365 días.

anios = int(input("Ingresa tu edad:"))

dias = anios*365

print("Tu edad es de:",dias,"dias")"""

#Ej 5
"""Tres personas invierten dinero para fundar una empresa (no necesaria-mente en partes iguales).
Calcular qué porcentaje invirtió cada una.

inv1 = float(input("Ingresa la inversion en $ de la primera persona:"))
inv2 = float(input("Ingresa la inversion en $ de la segunda persona:"))
inv3 = float(input("Ingresa la inversion en $ de la tercera persona:"))

totalinv = inv1 + inv2 + inv3

prom1 = inv1*100/totalinv
prom2 = inv2*100/totalinv
prom3 = inv3*100/totalinv

print("El primer inversor puso un:",prom1)
print("El segundo inversor puso un:",prom2)
print("El tercer inversor puso un:",prom3) """

#Ej 6
# Ingresar tres números enteros, calcular su promedio y mostrarlo por pantalla.
"""
val1 =int(input("ingresa el preimer valor:" ))
val2 =int(input("ingresa el segundo valor:" ))
val3 =int(input("ingresa el tercer valor:" ))

prom= (val1 + val2 + val3)/3

print("Tu promedio es de:",prom)"""

#Ej7
"""Una persona invierte su capital en un banco y desea saber cuánto dinero ganará en un mes,
 teniendo en cuenta que el banco paga 2% mensual. ¿Cuánto ganará en seis meses si deja su dinero invertido?

dininv = int(input("Ingresa cuanto dinero invirtio:"))

dinObt = dininv + dininv*2/100*6

print("Ganaras: ", dinObt)
"""



#Ej 8
"""Leer una medida en metros e imprimir esta medida expresada en centí-metros, pulgadas, pies y yardas. 
Los factores de conversión son:
1 yarda = 3 pies,
1 pie = 12 pulgadas, 
1 pulgada = 2,54 cm.
1 metro = 100 cm. 

medida = int(input("Ingresa tu medida en metros:"))
cm = medida*100
pulg = cm /2.54
pie = pulg /12
yard = pie/3
print("Son" ,cm, "cm, ", pulg,"pulgadas, ",pie,"Pies, ",yard,"yardas, ")

"""

#Ej 9

"""
Una inmobiliaria paga a sus vendedores un salario de $50000, más una comisión de $5000 por cada venta realizada,
más el 5% del valor de las ventas. 
Realizar un programa que imprima el número del vendedor y el salario que le corresponde en un determinado mes. 
Se leen el número del vendedor, la cantidad de ventas que realizó y el valor total de las mismas

numvend = int(input("Ingresa el numero del vendedor:"))
cantvent= int(input("Ingresa la cantidad de ventas realizadas por el vendedor:"))
valtotal =int(input("Ingresa el valor total de las ventas:"))
base = int(50000)

sueldo = base + (cantvent*5000)+(5*valtotal/100)

print("El sueldo del vendedor:",numvend," es de $",sueldo)"""

#Ej 10 
"""
Leer un período en segundos e imprimirlo expresado en días, horas, minutos y segundos. 
Por ejemplo, 200000 segundos equivalen a 2 días, 7 horas, 33 minutos y 20 segundos.

segs = int(input("Ingresa el periodo de tiempo en segundos:"))
mins = int(segs/60)
horas= int(mins/60)
dias = int(horas/24)

print(segs,"Equivalen a: ",dias,"Dias, ",horas,"Horas, ",mins,"Minutos. ")"""





