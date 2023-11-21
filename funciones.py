from random import shuffle
'''Lista inicial'''
palitos = ['-','--','---']
print(type(palitos.index('-')))

'''Mezclar palitos'''
def mezclar(lista):
    shuffle(lista)
    return lista

print(mezclar(palitos))

'''Pedir elegir'''
def probar_suerte():
    intento = ''
    while intento not in ['1','2','3']:
        intento = input("elige un nro del 1 al 3 : ")
    return int(intento)

intento1 = probar_suerte()

'''Comprobar el elegido'''

def elegido(lista,intento):

        if lista[intento-1] == '-' or lista[intento -1] == '--':
            print("perdiste")
        else:
            print("Ganaste")



palitos_mezclados = mezclar(palitos)
print(palitos_mezclados)
seleccion = probar_suerte()
elegido(palitos_mezclados,seleccion)

