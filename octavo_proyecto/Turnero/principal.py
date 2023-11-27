import numeros

'''. Y el desafío de hoy, es que crees un software que funcione como el turnero
 de una farmacia (en mi país le llamamos así a esa máquina que se encuentra en
  la entrada de muchos comercios o bancos inclusive, que te pregunta qué trámite
   vienes a realizar y te asigna un número de turno según el área a la que
    deseas dirigirte).
En nuestro caso, vas a crear el tunero para una farmacia que tiene tres áreas 
de atención: perfumería, farmacia (que es donde venden los medicamentos), y
 cosméticos. Tu programa le tiene que preguntar al cliente a cuál de las áreas desea dirigirse, y le va a dar un número de
turno según a qué área se dirija. Por ejemplo, si elige cosmética le va a dar el número C-54
(“C” de cosmética). Luego de eso, nos va a preguntar si queremos sacar otro turno. Esto, en
realidad, es para simular si viene un nuevo cliente. Y repetirá todo el proceso.
Algunas cosas a tener en cuenta:
Los diferentes clientes van a ir sacando turnos para diferentes áreas (perfumería, farmacia,
cosmética), en diferentes órdenes, por lo que el sistema debe llevar la cuenta de cuántos turnos
ha dado para cada una de esas áreas, y producir el siguiente número de cada área a medida
que se lo pida. ¿No te parece genial aprovechar la eficiencia de los generadores para poder
hacer esto?
Por otro lado, el mensaje donde le comunicamos el número de espera al cliente, debería tener
algo de texto adicional antes y después del número. Por ejemplo, “su turno es (-el número de
turno con el del comienzo-)”, y luego algo así como “aguarde y será atendido”. Para que
nuestro código no se repita, en vez de poner ese texto en cada una de las funciones que calculen
los números, podemos aprovechar la flexibilidad de los decoradores para crear ese texto
adicional una sola vez, y luego envolver a cualquiera de nuestras funciones con ese texto único.
Finalmente, deberías aprovechar que ahora ya sabes dividir tu programa en diferentes módulos,
y entonces separar el código en dos partes: por un lado, un módulo que se puede llamar
números.py, en el que vas a escribir todos los generadores y el decorador, y un segundo módulo
que podemos llamar principal.py, donde vas a escribir las funciones que administran el
funcionamiento del programa (como las instrucciones para elegir un área y para decidir si
seguirá tomando nuevos turnos o si va a finalizar el programa). Recuerda que vas a necesitar
importar el contenido de numeros.py dentro de principal.py para poder disponer de sus
funciones. '''

import numeros


def inicio():

    while True:

        try:
            turnero = input(''' Bienvenido a Farmacie:
                    Seleccione el area donde desea su turno:
                    [C] Cosmetica
                    [P] Perfumeria
                    [F] Farmacia 
                    ==>
                     ''').upper()
            print(turnero)
            print(['P','F','C'].index(turnero))
            ['P','F','C'].index(turnero)
        except ValueError:
            print('Esa no es una opcion valida')
        else:
            break

    numeros.decorar_turnero(turnero)


def preguntar():

    while True:
        inicio()
        try:
            otro_turno = input("Deseas sacar un turno? S/N: ").upper()
            ['S','N'].index(otro_turno)
        except ValueError:
            print('Opcion invalida')
        else:
            if otro_turno == 'N':
                print('Gracias por visitar Farmacie')
                break


preguntar()


