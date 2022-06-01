#String: Cadena de texto
from __future__ import print_function


nombre = "Pedro 😎"

print(nombre)

#Enteros: Numeros sin punto decimal
edad = 19

edads = "19"

#Ejemplos de diferencia
print(edad + edad)
print(edads + edads)

#Flotante: Numeros con punto decimal
pi = 3.14159264

#Para convertir una variable de un tipo a otro

edad = float(edad)  #Casteo: Transformar un tipo de variable a otra

print(edad) #Ahora saldra con un punto decimal

edad = 26 #Aqui se volvio a cambiar el tipo de variable y e incluso le cambio el valor

print(edad)

#Bool: Booleano que solo puede tener como respuesta SI o NO
legustas = False

if legustas == True :
    print("Si")
else :
    print("No")

legustas = True

print(legustas)
