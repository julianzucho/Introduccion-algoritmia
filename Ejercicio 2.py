"""Dado un vector de 100 posiciones (N), ingresar por teclado valores numéricos positivos y cargarlos en el vector hasta la posición N-2.
Ordenarlo por el método del selección
Ingresar por teclado un nuevo valor y buscarlo en el vector de manera secuencial.
Si no existe, ubicarlo en la ubicación que corresponde, desplazando el resto de los valores"""


import random

vector=[]
n=10
for i in range (n-2):
    vector.append(int(input("Ingrese un numero:")))

for i in range (len(vector)-1):
    for j in range(i+1,len(vector)):
        if vector[i]>vector[j]:
            aux=vector[i]
            vector[i]=vector[j]
            vector[j]=aux

num=int(input("Ingrese el numero que quiere buscar:" ))
for i in range (vector[i]):
    if num==vector[i]:
        print("El numero se encuentra en la posicion",i)
    else:
        vector.append(num)
        for i in range (len(vector)-1):
            for j in range(i+1,len(vector)):
                if vector[i]>vector[j]:
                    aux=vector[i]
                    vector[i]=vector[j]
                    vector[j]=aux
        break




print(vector)