
import random
legajo,materiasapro,cursadaaprob=[],[],[]
alumaprob,alumdesaprobados,porcentdesa,todasaprob,entreaprob=0,0,0,0,0

alumnos=int(input("Ingresa la cantidad de alumnos:"))
while alumnos>50:
    alumnos=int(input("Ingresa la cantidad de alumnos:"))

for i in range (alumnos):
    numleg=random.randint(0,10000)
    legajo.append(numleg)

for i in range (alumnos):
    aprobadas=random.randint(0,10)
    materiasapro.append(aprobadas)

for i in range (alumnos):
    if materiasapro[i]>=(10/2)+2:
        cursadaaprob.append(1)
    else:
        cursadaaprob.append(0)

#A
for i in range (alumnos):
    if cursadaaprob[i]==1:
        alumaprob+=1
    #B
    elif cursadaaprob[i]==0:
        alumdesaprobados+=1
    #C
    if  materiasapro[i]==10:
        todasaprob+=1
    
    if materiasapro[i]>=4 and materiasapro[i]<=6:
        entreaprob+=1

porcentdesa=alumdesaprobados*100/alumnos


print("Aprobaron la cursada",alumaprob,"Alumnos")
print("El porcentaje de alumnos desaporbados fue de:",porcentdesa,"%")
print("La cantidad de alumnos que aprobaron todas las materias fue de:",todasaprob)
print("La cantidad de alunos que aprobaron entre 4 y 6 materias es de:",entreaprob)


print(legajo)
print(materiasapro)
print(cursadaaprob)

