# edad = 50.0

# print(type(edad))

# precio = 5000
# cantidad = 3

# total = precio * cantidad
# print(total) 

# nombre = input ("nombre: ")
# semestre = input ("semestre: ")
# carrera =input ("carrera:  ")

# hace_semestres = (int(semestre)-5)
# print("buenos dias", nombre ,"estas en el ", semestre ,"semestres y estudias ",carrera,"hace",hace_semestres,"semestres")

# nombre = input ("nombre_del_cliente: ")
# producto = input (" producto: ")
# precio_unitario = float(input (" precio_unitorio: "))
# cantidad = int(input ("cantidad : "))
# total = precio_unitario * cantidad
# print ("el valor de la compras es ", total)

usuario = input ("usuario: ")
nombre = input ("nombre: ")
edad = int(input("edad: "))
temperatura=float(input("temperatura_corporal: "))
nota=float(input("Nota de 0.0 a 5.0       "))
carnet=input("¿tienes carnet? responde si o no ")
mayor_edad = edad>=18
temp_adecuada =  temperatura== 37.5
not_capacitacion= nota>=0.0 and nota<=5.0
confirmacion_carnet = carnet== "si"
cumple_requisitos= mayor_edad and temp_adecuada and not_capacitacion  and confirmacion_carnet 
print("CUMPLE REQUISO DE INGRESO ",     cumple_requisitos)
print("___________________________________")
print("ES MAYOR DE EDAD: ",             mayor_edad)
print("TIENE TEMPERATURA NORMAL: ",     temp_adecuada)
print("TIENE NOTA ACEPTABLE: ",            not_capacitacion)
print("TIENE CARNET: ",                 confirmacion_carnet)


print ()
