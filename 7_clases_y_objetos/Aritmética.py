# ejercicio aritemtica
class Aritmetica:
    """
    Clase aritmetica para realizar operacion de suma, resta, etc...
    """

    def __init__(self, a, b):
        self.a = a
        self.b = b

    def sumar(self):
        return self.a + self.b

    def restar(self):
        return self.a - self.b

    def multiplicar(self):
        return self.a * self.b

    def dividir(self):
        return self.a / self.b


arit1 = Aritmetica(1, 3)

print(f'Suma: {arit1.sumar()}')
print(f'Resta: {arit1.restar()}')
print(f'Multiplicacion: {arit1.multiplicar()}')
print(f'Division: {round(arit1.dividir(), 2)}')
