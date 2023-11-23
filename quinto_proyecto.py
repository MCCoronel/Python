
'''El programa va a elegir una palabra secreta y le va a mostrar al jugador solamente una serie
de guiones que representa la cantidad de letras que tiene la palabra. El jugador en cada turno
deberá elegir una letra y si la letra se encuentra en la palabra oculta, el sistema le va a
mostrar en qué lugares se encuentra. Pero si el jugador dice una letra que no se encuentra en
la palabra oculta, pierde una vida.
En el juego real del ahorcado, cada vez que perdemos una vida, se va completando el dibujo
del ahorcado miembro por miembro. Pero en nuestro caso, como aún no tenemos elementos
gráficos, simplemente le vamos a decir que tiene seis vidas y se las iremos descontando de una
en una, cada vez que el jugador elija una letra incorrecta.
Si se agotan las vidas antes de adivinar la palabra, el jugador pierde. Pero si adivina la palabra
completa antes de perder todas las vidas, el jugador gana.
Parece sencillo, pero ¿cómo diseñamos todo este código? Bueno, aquí van algunas ayudas:
 Primero vas a crear un código que importe el método choice, ya que lo vas a necesitar
para que el sistema pueda elegir una palabra al azar dentro de una lista de palabras que
también vas a crear al comienzo.
 Luego de eso, vas a crear tantas funciones como creas necesarias para que el programa
haga cosas como pedirle al usuario que elija una letra, para corroborar si lo que el
usuario ha ingresado es una letra válida, para chequear si la letra ingresada se
encuentra en la palabra o no, para verificar si ha ganado o no, etc.
 Recuerda escribir primero las funciones y luego el código que las implementa
ordenadamente.'''

import random
def palabras_al_azar():
    palabras=["estrella","perro","gato","mercado","computadora"]
    palabra_elegida= random.choice(palabras)
    return palabra_elegida

def desglose_palabra(palabra):

    lista = list(palabra)
    return lista

def juego(lista):
    largolista = len(lista)
    letras_adivinadas = ['_'] * largolista
    vidas = 6

    while vidas > 0:
        letra = input(f'la palabra tiene {largolista} palabras,elije una letra: ')

        if letra in lista:
            print(f"Correcto! La letra {letra} se encuentra en la palabra secreta")

            for i in range(largolista):
                if lista[i] == letra:
                    letras_adivinadas[i] = letra
            print("Avance de palabra: " + " ".join(letras_adivinadas))

            if "_" not in letras_adivinadas:
                print("¡Felicidades! Has adivinado la palabra.")
                break

        else:
                vidas -= 1
                print(f"Incorrecto. Te quedan {vidas} vidas.")

        if vidas == 0:
            print(f"Perdiste. La palabra era: {palabra}")



palabra = palabras_al_azar()
print(palabra)
lista = desglose_palabra(palabra)
print(lista)
ahorcado = juego(lista)
print(ahorcado)



