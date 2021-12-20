# variables de clases se asocia con la clase en si misma
class MiClase:
    variableClase = 'valor de variable de clase'

    def __init__(self, variableInstanica):
        self.variableInstancia = variableInstanica
        # variables de instancia se asocia con los objetos

    # metodo estatico (que se asocia a la clase y no al objeto)
    @staticmethod
    def metodoEstatico():
        print(MiClase.variableClase)

    @classmethod
    def metodoClase(cls):
        print(cls.variableClase)


print(MiClase.variableClase)

obj1 = MiClase('valorinstancia')
print(obj1.variableInstancia)
print(obj1.variableClase)

MiClase.variableClase2 = 'valo2'
print(MiClase.variableClase2)



print('Metodo estático'.center(35, '-'))
MiClase.metodoEstatico()

print('Metodo de clase'.center(35, '-'))
MiClase.metodoClase()

print('Metodo de clase accedido por un objeto'.center(50, '-'))
obj1.metodoClase()

