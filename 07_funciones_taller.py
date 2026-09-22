# def presentar(nombre,edad):
#     print ("Nombre:",nombre)
#     print ("Edad:",edad)
# presentar("laura ", 22)

# def sumar(a,b):
#     print (a+b)
# resultado=sumar (5,3)
# print(resultado)

# def sumar(a,b):
#     return (a+b)
# resultado=sumar (5,3)
# print(resultado)


# def multiplicar(a,b):
#     return a*b
# resultado=multiplicar(4,5)+10
# print(resultado)

# def calcular_promedio(notas):
#     suma=0
#     for nota in notas:
#         suma+=nota
#     return suma/len(notas)   
# notas_ana=[4.0,3.5,5.0] 
# promedio=calcular_promedio(notas_ana)
# print(round(promedio,2))


# def calcular():
#     resultado=0
#     print(resultado) 

# calcular()
# print(resultado)


# nombre="laura"

# def saludar():    
#    print(nombre)
# saludar()   


# def aumentar(numero):
#     return numero+1

# contador=10
# contador=aumentar(contador)
# print(contador )

#EJERCICIO

# def calcular_total(precio,cantidad):
#     return precio * cantidad

# producto={
#   "nombre":"teclado",
#   "precio":80000,
#    "cantidad":3
# }

# producto["total"]=calcular_total(   
#    producto["precio"],
#    producto["cantidad"]
# )

# print(producto)



# def sumar_puntos(puntos):
#  return puntos + 10

# puntos=5
# puntos=sumar_puntos(puntos)
# print(puntos)

#taller de clase 


def calcular_promedio(notas):
    suma=0
    for nota in notas :
        suma += nota
        return suma / len(notas)
estudiantes = [ 
 {"nombre":"ana" , " notas " : [4.0,3.5,5.0]},
 { "nombre":"luis" , "notas " : [2.5,3.0,2.8]},
 { "nombre":"carlos" , "notas ": [4.5,4.0,4.8]}
 ]
for estudiante in estudiantes:
 if estudiante["notas"]>= 3:
        print (estudiante [ "nombre"], "aprobo" )
else :
     print( estudiante[ "nombre"], " no aprobo" )
print(estudiante[ "nombre"], round(calcular_promedio, 2))