from random import *

nombre = input("Nombre: ")
print(f"Hola {nombre}, a partir de este momento tienes 8 intentos para adivinar un número del 1 al 100")
numero_ganador = randint(1, 100)
print(numero_ganador)

intentos = 8

while intentos > 0:

    numero_elegido = int(input("¿Cuál es el número? "))

    if numero_elegido < 1 or numero_elegido > 100:
        print("Ha elegido un número que no está permitido")
    elif numero_elegido < numero_ganador:
        print("Respuesta incorrecta y ha elegido un número menor al número secreto")
    elif numero_elegido > numero_ganador:
        print("Respuesta incorrecta y ha elegido un número mayor al número secreto")
    elif numero_elegido == numero_ganador:
        print(f"¡GANASTE! Número de intentos restantes: {intentos}")
        break

    intentos -= 1

if intentos == 0:
    print(f"Perdiste. El número secreto era {numero_ganador}.")




