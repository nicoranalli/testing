from Cuadrado import Cuadrado
from Rectangulo import Rectangulo

print('Creación objeto cuadrado'.center(50, '-'))
cuad1 = Cuadrado(5, 'Rojo')

print(cuad1.ancho)
print(cuad1.alto)
print(cuad1.color)
area = cuad1.calcularArea()
print(area)

print(Cuadrado.mro())

print(cuad1)

print('Creación objeto rectangulo'.center(50, '-'))

rect1 = Rectangulo(5, 4, 'Azul')

print(f'Área del rectángulo: {rect1.calcularArea()}')
print(rect1)

