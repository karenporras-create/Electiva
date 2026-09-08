# total = 0
# for vueltas in range(4):
#      numero = int(nput("numero: "))
#      total = total + numero
# print ("Numero:", numero)     

# contador = 0
# suma = 0 
# for numero in range (1,11):
#     if numero % 2 == 0:
#         contador += 1
#         suma += numero
# print("cantidad de pares :", contador)    
# print("suma de pares :" , suma )    

# for numero in range (1,8):
#     if numero ==4 :
#         break
#     print (numero )

# texto = "hola"
# for letra in texto :
#     print ("letra :", letra )


# texto = "  AREA TECNICA "
# texto = texto.lower()

# if letra in "aeiou" :
#      .....

# texto = "python "
# len(texto)    #6
# texto [0]     #p
# texto[-1]     #n
# texto [0:3]   #Pyt
# texto [::-1]  #nohtyp
# texto = print (texto ) 

# notas = [4.5,3.8,5.0,2.9] 
# print (notas[0])
# print (notas [-1])
# print (len(notas))

# notas = [4.5,3.0,5.0] 
# for nota in notas : 
#     print ("Nota:" , nota )

# suma = 0
# for nota in notas : 
#     suma += nota
# promedio = suma / len(notas )     

# notas = []
# for vuelta in range (3):
#     nota = float(input("ingrese una nota: "))
#     notas.append(nota)
# print (notas )

# frutas = [" manzana" , "pera", "uva "]
# frutas [1] = "mango"
# # ["manzana , "mango " ,"uva "]

# frutas.remove("uva")
# # elimina por valor 

# eliminada  = frutas.pop(0)
# #elimina por indice y devuelve el valor 

# numeros = [30, 10, 40, 20]
# numeros.sort ()  # modifica la lista
# ordenada = sorted(numeros)   # crea otra lista 
# numeros.reverse()       # invierte el orden actual
# numeros.count(20)      # cuenta coincidencias 
# numeros.index(40)      # primera posicion donde aparece  

# nombres = ["ana " , "luis", "carlos"]
# for i in range(len(nombres)):
#      print ("estudiante ", i + 1 , ":" , nombres[i] )

# notas = [2.5 , 3.0 , 4.0]
# for i in range (len(notas )):
#     if notas[i] < 3.0 :
#         notas[i] = 3.0
# print(notas )        

# estudiante = [
#   ["ana ",4.5],
#   ["luis ",3.8 ],
#   ["carlos" ,4.2]     
#   ]
  

# for estudiante in estudiantes:
#     print (estudiante[0], estudiante[1])


estudiantes = [
    ["ana ", [4.0 ,3.5,5.0]]
    ["luis" , [2.8, 3.0, 4,2]]
]

for estudiante in estudiantes :
    suma=0

    for nota in estudiante[1]:
        suma += nota
        
    promedio= suma / len (estudiante[1])
    print(estudiante[0], round(promedio , 2))