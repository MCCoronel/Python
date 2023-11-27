def suma():
    n1 = int(input('num1: '))
    n2 = int(input('num2: '))
    print(n1+n1)
    print('thanks' + n1)

#suma()

try:
    #Codigo a probar
    suma()
except TypeError:
    print('Estas intentando concatenar str e int')
except ValueError:
    print('Ese no es un numero')
else:
    print('lito')
finally:
    print('ok')