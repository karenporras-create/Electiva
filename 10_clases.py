
# productos = [
#     {"nombre":"Mouse","precio":50000,"cantidad":5},
#     {"nombre":"Teclado","precio":80000,"cantidad":3},
#     {"nombre":"Monitor","precio":700000,"cantidad":2}   
# ]
# with open("productos.txt","w") as archivo:
#     for producto in productos:
#         archivo.write(producto["nombre"]+","+
#                       str(producto["precio"])+","+
#                       str(producto["cantidad"])+"\n")


# archivos 2 parte 

# with open ("productos.txt", "r") as archivo:
#     for linea in archivo:
#         datos = linea.strip().split(",")

#         producto ={
#              "nombre": datos[0],
#              "precio": int(datos[1])
#              "cantidad": int(datos[2])
#         }
#         productos.append(producto)
# print(productos)        

# with open ("estudiantes.txt", "w") as archivo :
#      for i in range (3) :
#          nombre = input("ingrese el nombre: ") 
#          edad= int(input("ingrese la edad: " ))
#          archivo.write(nombre + ", " + str(edad) + "\n")


# estudiantes = []

# with open ("estudiantes.txt", "r") as archivo :
#     for linea in archivo :
#         datos=linea.strip().split(",")
#     estudiante={
#         "nombre":datos[0],
#         "edad": int(datos[1])
#     }
#     estudiantes.append(estudiante)
        
# print(estudiantes)

# programacion orientada  a objetos 

# class Producto:
#     pass
# mouse = Producto()
# teclado = Producto()

# print(type(mouse))

# #_init_se ejecuta automaticamente cuando creamos un objeto

# class Producto:
#     def _init_(self,nombre,precio):
#         self.nombre = nombre
#         self.precio = precio
# mouse = Producto("Mouse", 50000)        

# class Producto:
#      def _init_(self,nombre,precio,cantidad):
#          self.nombre = nombre
#          self.precio = precio
#          self.cantidad = cantidad    
# teclado= Producto("teclado",80000,3)
# print("Producto:teclado.nombre , precio:teclado.precio , cantidad:teclado.cantidad")

class Producto:
    def _init_(self , nombre, precio):
        self.nombre = nombre
        self.precio = precio

    def mostrar_precio(self):
        print (self.nombre , self.precio)
mouse=Producto("Mouse ", 70000)
mouse.demostrar_precio()
        
