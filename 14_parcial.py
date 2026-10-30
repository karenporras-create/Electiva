# parte c
class Dispositivo:
 Dispositivo=("Dispositivo.txt", "w") as archivo :
    def __init__(self, nombre, marca, precio):
        self.nombre = nombre
        self.marca = marca
        self.precio = precio

    def mostrar_informacion(self):
        print("Nombre:", self.nombre)
        print("Marca:", self.marca)
        print("Precio: $", self.precio)

    def calcular_descuento(self, porcentaje):
        if 0 <= porcentaje <= 1:
            return self.precio * (1 - porcentaje)
        else:
            print("Porcentaje de descuento no válido")
            return None
        
 class Sensor(Dispositivo):

    def __init__(self, tipo,unidad, estado):

        super().__init__(nombre, precio)

        self.tipo = tipo
        self.unidad= unidad
        self.__estado = "Disponible"
        self.cambiar_estado(estado)

    # Modificar el estado
    def cambiar_estado(self, nuevo_estado):

        if nuevo_estado == "Disponible" or nuevo_estado == "Prestado":
            self.__estado = nuevo_estado
            print("Estado actualizado correctamente_activo")

        else:
            print("Error: estado no permitido_inactivo")

    # Consultar estado
    def consultar_estado(self):
        return self.__estado

    def mostrar_informacion(self):

        super().mostrar_informacion()

        print("nombre", self.nombre)
        print("Estado:", self.__estado)


# parte 3

sensor1 = Sensor(
    "rubiano",
    "rojo",
    500000,
    "Disponible"
)

sensor2 = Sensor(
    "faro_electrico",
    "verde",
    180000,
    "Disponible"
)

# Mostrar información
print("\n===== SENSOR 1 =====")
sensor1.mostrar_informacion()

print("\n===== SENSOR 2 =====")
sensor2.mostrar_informacion()

# Cambiar estado
print("\n===== CAMBIO DE ESTADO =====")

sensor1.cambiar_estado("Prestado")

print("Estado actual:", sensor1.consultar_estado())

# Intentar estado incorrecto
print("\n===== ESTADO INCORRECTO =====")

sensor1.cambiar_estado("Dañado")

print("Estado actual:", sensor1.consultar_estado())

# Aplicar descuento
print("\n===== DESCUENTO =====")

precio_final = sensor1.calcular_descuento(0.10)






#    parte b
Productos = []
with open("productos.txt" , "w") as archivo:
#registrar los 4 equipos
    for i in range(4):
        print(f"\nRegistro del producto{i+1}")

nombre=input("ingrese el nombre del producto: ")
cantidad=int(input("ingrese la cantidad disponible: "))
precio=float(input("ingrese el valor unitario: "))
Productos.append([nombre, cantidad,precio])

with open("Productos.txt", "r" ) as archivo:
    for linea in archivo:

        datos = linea.strip().split(",")

        nombre = datos[0]
        cantidad = int(datos[1])
        valor_unitario = float(datos[2])

    def __init__(self, nombre, marca, precio):

        super().__init__(nombre, marca, precio)
print("\nproductos superiore a $2.000.000 ")

with open("productos.txt", "r") as archivo:
    for linea in archivo:

        nombre, cantidad, valor = linea.strip().split(",")

        cantidad = int(cantidad)
        valor = float(valor)

        total = cantidad * valor

        if total > 2000000:
            print(nombre, "- Valor total: $", total)

# Mostrar valor total general
total_general=0
print("\n")
print(" valor total de los productos: $",total_general)



