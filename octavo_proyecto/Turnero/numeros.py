
def turnero_perfumeria():
    for n in range(1, 10000):
        yield f"P - {n}"


def turnero_farmacia():
    for n in range(1, 10000):
        yield f"F - {n}"


def turnero_cosmetica():
    for n in range(1, 10000):
        yield f"C - {n}"


P = turnero_perfumeria()

F = turnero_farmacia()

C = turnero_cosmetica()


def decorar_turnero(funcion):
    print('''Su turno es: 
        ''')
    if funcion == 'P':
        print(next(P))
    elif funcion =='F':
        print(next(F))
    else:
        print(next(C))
        print('Aguarde y será atendido')










