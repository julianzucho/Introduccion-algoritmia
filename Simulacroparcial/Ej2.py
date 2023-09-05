'''En una veterinaria, se ingresa el tipo de animal, siendo ellos 1 – perro, 2 – gato, 3 – conejo¸
y por cada uno de ellos se ingresa 1 o 2, correspondiendo a macho y hembra, respectivamente

El fin de ingreso se indica ingresando -1

Informar la cantidad de animales tratados, cuantas hembras perros y cuantos machos conejos se trataron

Porcentaje de gatos ingresados'''

canthembra=0
porcentgat=0
total=0
gato=0
conejosmacho=0

print('1 para perro, 2 para gato, 3 para conejo ')

animal=int(input('Ingrese que tipo de animal es:'))

while animal!=-1:
    
    sexo=int(input('Ingrese si es macho 1 o hembra 2: '))
    total=total+1

    if animal ==1:
        if sexo==2:
            canthembra=canthembra+1
    elif animal==2:
        gato=gato+1
    elif animal==3 and sexo==1:
        conejosmacho=conejosmacho+1
    print()
    animal=int(input('Ingrese que tipo de animal es:'))

porcentgat=gato*100/total

print("")
print('Se trataron a',total,"de animales")

print('Ingresaron',canthembra,'perros hembras')
print('Se trataron ',conejosmacho,'conejos machos')
print('Ingresaron un ',porcentgat,'"%" de gatos')

    









