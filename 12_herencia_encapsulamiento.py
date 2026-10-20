# class Persona:
#      def__init__(self,nombre):
#       self.nombre = nombre

#      def saludar(self):
#         returnf"Hola,soy{self.nombre}"

# class Estudiante(Persona):   
# Estudiante1=Estudiante("karen")
# print(estudiante.saludar())

# class Persona:
#      def__init__(self,nombre,edad):
#         self.nombre = nombre
#         self.edad = edad

# class Estudiante(Persona):  
#      def__init__(self,nombre,edad,carrera):
#          super().__init__(nombre,edad)
#          self.carrera = carrera


     
# class Estudiante(Persona):  
#      def__init__(self , nombre , edad, carrera, nota):
#          super().__init__(nombre,edad)
#          self.carrera = carrera
#          self.__nota = nota 
# estudiante1=Estudiante("karen",22,"Lic.Tecnologia", 4.5)

# estudiante1.presentarse()
# # METODO HEREDADO DE PERSONA 

# estudiante1.mostar_nota()
# # METODO PROPIO DE ESTUDIANTE 

# estudiante1.obtener_estado()
# # METODO PROPIO DE ESTUDIANTE 

# class Persona:
#    def presentarse(self):
#         return "soy una persona"
   
# class Estudiante (Persona):
#     def presentarse (self):
#         return "soy un estudiante "

# class Estudiante :
#     def __init__(self,nota):
#         self.__nota = nota

#     def mostrar_nota(self):
#         return self.__nota

# class Sensor:
#     def __init__(self):
#         self._ubicacion = "sala"
#         self._temperatura = 25

# #_ubicacion es interno por conveccion    
# # __temperatura se controla desde metodos      

# class Estudiante:
#    def __init__(self,nota):
#        self.__nota = nota

#     def mostrar_nota(self):
#         return self.__nota

#     def cambiar_nota(self, nueva_nota):
#         if 0 <= nueva_nota <=5:
#         self.__nota=nueva_nota

# def obtener_estado(self):
#     if self.__nota >= 3:
#          return f"Aprobado con: {self.__nota}"
#     else:
#          return f"Reprobado con: {self.__nota}"

# estudiante1 =Estudiante("Luis", 34, "Lic en Tecnologia", 4.5)
# estudiante2 =Estudiante("Pedro", 25, "Lic en Tecnologia", 2.8)

# print(estudiante1.obtener_estado())
# print(estudiante2.obtener_estado())

# class Cuenta:
#     def __init__(self, titular, saldo):
#        self.titular = titular
#        self.__saldo = saldo

#     def consultar_saldo(self):
#         return self.__saldo
    
#     def depositar(self, cantidad):
#         if cantidad > 0:
#             self.__saldo += cantidad

#actividad

class Persona:
    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad

    def presentarse(self):
        return f"Hola,soy karen {self.nombre}"   

class Estudiante(Persona ):
     def __init__(self, nota, carrera):
         self.__nota = nota
         self.carrera = carrera

     def mostrar_nota(self):
         return self.__nota
     
     def cambiar_nota(self, nueva_nota):
         if 0 <= nueva_nota <=5:
          self.__nota=nueva_nota

     def obtener_estado(self):
        if self.__nota >= 3:
          return f"Aprobado con: {self.__nota}"
        else:
         return f"Reprobado con: {self.__nota}"

estudiante1 =Estudiante("Karen", 22, "Lic en Tecnologia", 4.8)
estudiante2 =Estudiante("Melisa", 22, "Lic en Tecnologia" , 4.7)
print(estudiante1.obtener_estado())
print(estudiante2.obtener_estado())