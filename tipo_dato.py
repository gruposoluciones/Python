#tipos de datos en python

"""
a = 5 #numerico
b = "Hola" #cadena de texto
c = 3.14 #decimal
d = True #booleano
e = [1, 2, 3] #lista
f = (4, 5, 6) #tupla
g = { "clave": "valor" } #diccionario
h = {1, 2, 3} #conjunto
print("\n")
print(type(a))
print(type(b))  
print(type(c))
print(type(e))
print(type(f))
print(type(g))
print(type(h))  

#concadenacion datos
print(b + " Mundo")  # Concatenación de cadenas
print(a + 10)        # Suma de números
print(c * 2)        # Multiplicación de números decimales
print(e + [4, 5])   # Concatenación de listas
print(f + (7, 8))   # Concatenación de tuplas
print(g["clave"])    # Acceso a valor en diccionario
print(h.union({4, 5})) # Unión de conjuntos

#como concatedamos un dato boleano, 6 ejemplos tomando en cuenta operaciones booleanas
print('\n')
print(d + False)  # Suma de booleanos (True se considera 1 y False se considera 0)
print(d and False)  # Operación lógica AND entre booleanos
print(d or False)   # Operación lógica OR entre booleanos
print(not d)        # Operación lógica NOT
print(d == True)   # Comparación de igualdad
print(d != False)  # Comparación de desigualdad
print()

#declaracion de variables
#otras formas de concatenar vqariables
primer_nombre = "Percy"
apellido = "Quispe"
nombre_completo = primer_nombre + " " + apellido
print("Nombre completo:", nombre_completo)
print()

años_de_servicio = 33
print("Años de servicio =", años_de_servicio)
print()

sueldo = 5000
impuesto = 0.18
sueldo_final = sueldo - (sueldo * impuesto)
print("Mi sueldo COMPLETO es:", sueldo,", Menos el impuesto a la RENTA =", sueldo_final)
print()

#ahora declaramos variable en una sola linea
x, y, z = 10, 20.5, "Hola"
print("x =", x)
print("y =", y)
print("z =", z)
print()

#ahora cambiado el valor de las variables
x = "Nuevo valor"
y = 30.75
z = "Mundo"
print("x =", x)
print("y =", y)
print("z =", z)
print()

#creando listas, ojo si se puede modificar
lista_numeros = [1, 2, 3, 4, 5]
lista_cadenas = ["manzana", "banana", "cereza"]
print("Lista de números:", lista_numeros)
print("Lista de cadenas:", lista_cadenas)
#esto es valido
lista_numeros[2] = 667674
print("Lista de números modificada:", lista_numeros)

#creando tuplas, NO se puede modificar
tupla_numeros = (10, 20, 30)
tupla_cadenas = ("rojo", "verde", "azul")
#tupla_numeros[1] = 999  # Esto generará un error
print("Tupla de números:", tupla_numeros, "Tupla_cadenas:", tupla_cadenas) 

#creando conjunto set
conjunto_numeros = {1, 2, 3, 4, 5, 5, 5, 1, 5,}
conjunto_cadenas = {"perro", "gato", "pez"}
print("Conjunto de números:", conjunto_numeros)
print("Conjunto de cadenas:", conjunto_cadenas)

#creando un diccionario (dict)
diccionario_persona = {
    "nombre": "Ana",
    "edad": 28,
    "ciudad": "Madrid"
} 
print("Diccionario persona:", diccionario_persona)
print("Nombre:", diccionario_persona["nombre"])
print("Edad:", diccionario_persona["edad"])
print("Ciudad:", diccionario_persona["ciudad"])

print(diccionario_persona['edad'])

#----Listas----
#Estructura de datos, si se puede modificar

lista_numeros = [1, 2, 3, 4, 5]
lista_nombres = ["Ana", "Luis", "Carlos", "Marta"]
lista_cadenas = ["manzana", "banana", "cereza"]
print("Lista de números:", lista_numeros)
print("Lista de cadenas:", lista_cadenas)
print("Lista de nombres:", lista_nombres)
print("...............................")
print()
lista_numeros.append("6")
lista_numeros[5] = 7897
print("Lista de números modificada:", lista_numeros)
lista_nombres.append("Sofía")  # Agregar un elemento al final de la lista
print("Lista de nombres modificada:", lista_nombres)

#que otras operaciones pueden hacer con las listas
print("Longitud de la lista de números:", len(lista_numeros))  # Longitud de la lista
print("Elemento en el índice 2 de la lista de nombres:", lista_nombres[2])
print("Índice del elemento 'Marta' en la lista de nombres:", lista_nombres.index("Marta"))
print("Eliminar el elemento 'Luis' de la lista de nombres.")
lista_nombres.remove("Luis")
print("Lista de nombres después de eliminar 'Luis':", lista_nombres)
"""
#para devolver indices
import os
os.system('cls' if os.name == 'nt' else 'clear')

lista1 = [10, 11, 14, 20, 30, 31, 40, 50]
print(lista1[::6])  # Devuelve [10, 30, 50]
print(lista1[1:7:2])  # Devuelve [20, 15, 50]

lista1 += [1, 2, 3, 4, 5, 7] 
print("nueva lista:", lista1)
print("Longitud de la nueva lista:", len(lista1))
print(lista1[-1])

