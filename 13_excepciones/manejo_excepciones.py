from numIdenticosException import numIdenticosException

resultado = None
a = int(input('Ingresa el primer numero: '))
b = int(input('Ingresa el segundo numero: '))
try:
    if a == b:
        raise numIdenticosException('Números identicos')
    resultado = a/b
    print(a/b)
except Exception as e:
    print(f'Error: {e}')