# estudiantes = []
# cantidad_estudiantes=int(input("cuantos estudiantes va registrar: "))
# for i in range(cantidad_estudiantes):
#     nombre =input("nombre: ")
#     notas1=float(input("digite la nota 1"))
#     notas2=float(input("digite la nota 2"))
#     notas3=float(input("digite la nota 3"))
#     notas=[notas1, notas2 ,notas3 ]
#     estudiante={}
#     "nombre":nombre,
#     "notas":nota,
#     estudiante.append(estudiante) 
# for  in estudiantes :
#     suma = 0
#     for  in estudiantes["notas "]:
#         suma+=nota
#     promedio = suma / len(estudiante ["notas "])
#     print(estudiante[ "nombre"], round(promedio, 2))
#  for estudiante in estudiantes:
#     if estudiante["nota" ] >= 3:
#        print (estudiante [ "nombre"], "aprobo" )
# else :
#    print( estudiante[ "nombre"], " no aprobo" )


# numeros={10,20,30,30,40}
# datos=set()
# if 10 in numeros:
#     numeros.add(50)
#     numeros.remove(30)
#     numeros.discard(60)
# print (numeros)

# numeros={10,20,30,30,40}
# numb={10,25,30,45}
# datos=set()
# if 10 in numeros:
#     numeros.add(50)
#     numeros.remove(30)
#     numeros.discard(60)
# print (numeros-numb)
numeros={10,20,30,30,40}
# numb={10,25,30,45}
# datos=set()
# if 10 in numeros:
#     numeros.add(50)
#     numeros.remove(30)
#     numeros.discard(60)
# print (numeros&numb)
numeros={10,20,30,30,40}
numb={10,25,30,45}
datos=set()
if 10 in numeros:
    numeros.add(50)
    numeros.remove(30)
    numeros.discard(60)
print (numeros|numb)