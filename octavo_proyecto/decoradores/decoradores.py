
def decorar_saludo(funcion):
    def otra_funcion(palabra):
        print('Hola')
        funcion(palabra)
        print('adios')
    return otra_funcion


@decorar_saludo
def mayus(texto):
        print(texto.upper())
@decorar_saludo
def minus(texto):
        print(texto.lower())

#OTRA FORMA ES:

def mayus(texto):
        print(texto.upper())

def minus(texto):
        print(texto.lower())

mayuscula_decorada = decorar_saludo(mayus('Cele'))
mayuscula_decorada('ceLe')

mayus('Cele')


