print("\n Bluces de listas \n")

contador = 0
while contador < 100:
    print("Contador:", contador)
    contador += 1
    if contador == 10:
        print("Se alcanzó el valor de 10, saliendo del bucle.")
        break
print("\n Bucle con continue... \n")

contador = 0
while contador < 10:
    contador += 1
    if contador % 2 == 0:
        continue
    print("Número impar:", contador)

print("\n Bucle for con range... \n")
while contador <= 100:
    print("Contador:", contador)
    contador += 1
    if contador == 10:
        print("se incrementa")
    else:
        print("No se ha alcanzado el valor limite de 100...")

numero = -1
while numero < 0:
    try:
        numero = int(input("Ingresa un número positivo: "))
        if numero < 0:
            print(f"El número ingresado es: {numero}... Intente nuevamente.")
        else:
            print("¡Gracias! Has ingresado el número positivo:", numero)
    except:
        print("Entrada inválida. Por favor, ingresa un número entero.")
