##### PRINT E INPUT #####

print("Tipos de datos en Python")
print('Hola como te llamas?')


"""
age = input("¿Cuántos años tienes? ")
print("Tienes " + age + " años.")

pais, departamento = input("¿De qué país y departamento eres? ").split()
print("Eres de " + departamento + ", " + pais + ".")

print("ingrese su edad:")
edad = input()
edad = int(edad)

if edad >= 18:
    print("Eres mayor de edad.")
    print("Puedes votar!!!")
else:
    print("Eres menor de edad.")
    print("No puedes votar!!!")

edad = 17
mensaje ="Eres mayor de edad." if edad >= 18 else "Eres menor de edad"


###listas
print("\nCrear Listas")
lista1 = [1, 2, 3, 4, 5]
lista2 = ["manzanas", "bananas", "cerezas"]
lista3 = [1, "hola", 3.14, True]
lista_de_listas = [lista1, lista2, lista3]
print("Lista 1:", lista1, "\nLista 2:", lista2, "\nLista 3:", lista3)
lista1 = [1, 2, 3, 4, 5]
print(lista1[1:4])
import os
os.system("clear")

###### metodos
lista1 = ['a', 'b', 'c', 'd', 'e']
lista1.append('f')
print("Después de append(6):", lista1)

lista1.insert(0, 0)
print("Después de insert(0, 0):", lista1)

lista1.remove('b')
print("Después de remove(3):", lista1)

lista1.pop()
print("Después de pop():", lista1)

numeros = [1, 202, 30, 400, 5, 6, 7]
numeros.sort()
print("Después de sort():", numeros)

lista1.sort(reverse=True)
print("Después de sort(reverse=True):", lista1)

frutas = ['manzana', 'banana', 'cereza', 'Durazno', 'Platano']
print(frutas.count('banana'))
print(frutas)
print('banana' in frutas)
frutas.sort(key=str.lower)
print("Después de sort(key=str.lower):", frutas)

"""