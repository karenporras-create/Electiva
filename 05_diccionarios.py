
# estudiante = {
#      "nombre":"ana" ,
#      "edad" :20,
#      "notas":[4.0, 3.5 , 5.0]
# } 
# print (estudiante  [ "nombre"])
# print (estudiante  [ "notas"])

# producto = {
#      "nombre":" mouse " ,
#      " precio " : 50000
#  } 
# producto  ["precio" ]= 55000
# producto  [" cantidad" ]= 4


# print (producto.get("cantidad" , 0))


# if "precio" in producto :
#     print (producto [ " precio "])

# persona = {
#     "nombre " : "laura " ,
#     "edad": 23 ,
#     "ciudad": "bogota"
#     } 

# for clave in persona:
#     print (clave , persona[ clave] )

# for clave, valor in persona.items():
#    print(clave , ": ", valor)

# estudiantes = [ 
#     { "nombre":"ana" , " nota " : 4.5 },
#     { "nombre":"luis" , "nota " : 2.8 },
#     { "nombre":"carlos" , "nota " : 3.7 }
# ]

# for estudiante in estudiantes:
#     if estudiante["nota" ] >= 3:
#         print (estudiante [ "nombre"], "aprobo" )
# else :
#     print( estudiante[ "nombre"], " no aprobo" )


estudiantes = [ 
     { "nombre":"ana" , " notas " :  [ 4.0 , 3.5 ,5.0]},
     { "nombre":"luis" , "notas " : [ 2.8 , 3.0 , 4.2]},
     { "nombre":"carlos" , "notas " :[ 2.0 , 2.5 ,2.8]}
]
for estudiante in estudiantes :
    suma = 0
    for estudiante in estudiantes["notas "]:
        suma += nota

    promedio = suma / len(estudiante ["notas "])
    print(estudiante[ "nombre"], round(promedio, 2))
           

 
 

