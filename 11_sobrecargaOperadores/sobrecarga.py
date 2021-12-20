# operador +

a = 2
b = 3
print(a + b)

a = 'Hola'
b = ' Mundo'
print(a + b)


class Persona:
    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad

    def __add__(self, otro):
        return self.edad + otro.edad


ob1 = Persona('Juan', 20)
ob2 = Persona('Alex', 16)
print(' Suma de objeto 1 y objeto 2 '.center(50, '-'))
print(ob1 + ob2)
