"""La consigna es esta: el programa le va a preguntar al usuario su nombre, y luego le va a decir
algo así como “Bueno, Juan, he pensado un número entre 1 y 100, y tienes solo ocho intentos
para adivinar cuál crees que es el número”. Entonces, en cada intento el jugador dirá un
número y el programa puede responder cuatro cosas distintas:
 Si el número que dijo el usuario es menor a 1 o superior a 100, le va a decir que ha elegido
un número que no está permitido.
 Si el número que ha elegido el usuario es menor al que ha pensado el programa, le va a
decir que su respuesta es incorrecta y que ha elegido un número menor al número secreto.
 Si el usuario eligió un número mayor al número secreto, también se lo hará saber de la
misma manera.
 Y si el usuario acertó el número secreto, se le va a informar que ha ganado y cuántos
intentos le ha tomado.
Si el usuario no ha acertado en este primer intento, se le va a volver a pedir que elija otro
número. Y así hasta que gane o hasta que se agoten los ocho intentos.
"""

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




