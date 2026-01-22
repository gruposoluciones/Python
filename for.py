### ITERACION todo lo que sea iterable

print("\n Bucle for con lista... \n")  
frutas = ['manzana', 'banana', 'cereza', 'Durazno', 'Platano']
for fruta in frutas:
    print(fruta)

cadena = "percybeltran"
for caracter in cadena:
    print(caracter) 

###recuperar el indice
enumerate()

frutas = ['manzana', 'banana', 'cereza', 'Durazno', 'Platano']
for indice, fruta in enumerate(frutas):
    print(f"Índice: {indice}, Fruta: {fruta}")  


###bucles anidados

letras = ["A", "B", "C"]
numeros = [1, 2, 3] 

for letra in letras:
    for numero in numeros:
        print(f"{letra}-{numero}")

animales = ["perro", "gato", "conejo", "zorro", "loro"]
for indice, animal in enumerate(animales):
    print(animal)
    if animal == "zorro":        
        break
    print(f"se bloqueo el for...");

print("\nContinue:")  
print("...........")
animales = ["perro", "gato", "conejo", "zorro", "loro"]
for indice, animal in enumerate(animales):
    if animal == "conejo":
        continue
    print(animal)
    print(f"El animal: {animal} está en la posición {indice}")

print("\nContinue:")  
print("...........")

pares = [num for num in [1,2,3,4,5,5,6] if num % 2 == 0]
print(pares)

for num in range(5,150,8):
    print(num)

for num in range(10,0,-1):
    print(num)

for num in range(0, 32, 5):
    print(num)

contador = 0
while contador <5:
    print("hacer algo 5 veces")
    contador +=1

for _ in range(5):
    print("hacer algo 5 veces")
