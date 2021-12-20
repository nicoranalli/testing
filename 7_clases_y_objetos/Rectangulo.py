class Rectangulo:
    def __init__(self, altura, ancho):
        self.altura = altura
        self.ancho = ancho

    def calcularArea(self):
        return self.altura * self.ancho


altura = int(input('Altura: '))
base = int(input('Base: '))

rectangulo1 = Rectangulo(altura, base)
print(f'Rectángulo 1 -> altura: {rectangulo1.altura}'
      f' ancho: {rectangulo1.ancho}'
      f' área: {rectangulo1.calcularArea()}')
