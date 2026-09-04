# 1punto

# edad=int(input("ingrese su edad : "))
# if edad >= 18:
#    print(" mayor de edad ")
# else:
#    print ("menor de edad")

# faltaba poner el int y () en la primera linea para que nos leyera la variable edad correctamente 

# parte b

# nota=float(input("ingrese la nota: ")) 
# if nota >= 4.5 :
#     print ("desempeño superior")
# elif nota >= 3.0 :
#     print ("aprobado")  
# else :
#     print("no aprobado")    

# 2 punto

# nota=float(input("ingrese la nota: ")) 
# if nota >= 4.6 and nota <= 5.0 :
#     print ("desempeño superior")
# elif nota >= 3.0 and nota < 4.0 :
#       print ("desempeño basico ")  
# elif nota < 3.0 :
#    print ("no aprobado")
# elif nota >= 4.0 and nota <= 4.6 :
#  print ("desempeño alto")
# else :
#  print("nota invalida")   

# 3 punto

total_ventas = 0
cantidad_ventas = 0
opcion = 0

while opcion <=3 :
    opcion= int(input("seleccione una opcion del menu"))
    print ("ingrese una opcion 1.registrar venta , 2.consultar resumen ,3.finalizar :  "  )
    if opcion == 1 :
        print ("registar venta ")
        total_ventas = total_ventas + 1 
        cantidad_ventas=cantidad_ventas + 1
        print (" venta registrada ")
    elif opcion ==2 :
        print (" consultar resumen ")
        cantidad_ventas=cantidad_ventas
        total_vendido=total_ventas    
    elif opcion==3 :
        print ("registro finalizado")
        cantidad_ventastotales=cantidad_ventas
        total_vendido=total_ventas
    else :
        print("opcion invalida")