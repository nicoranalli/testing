class Pelicula:
    def __init__(self, nombre):
        self._nombre = nombre

    def __str__(self):
        return f'Pelicula: {self._nombre}'

    @property
    def nombre(self):
        return self._nombre

    @nombre.setter
    def nombre(self, nombre):
        self._nombre = nombre




if __name__ == '__main__':
    pel1 = Pelicula('Rapidos y Furiosos')
    print(pel1)
    pel1.nombre = 5
    print(pel1)
