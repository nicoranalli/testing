from DispositivoES import DispositivoES


class Teclado(DispositivoES):
    contadorTeclados = 0

    @classmethod
    def contarTeclados(cls):
        cls.contadorTeclados += 1
        return cls.contadorTeclados

    def __init__(self, tipo, marca):
        super().__init__(tipo, marca)
        self._idTeclado = Teclado.contarTeclados()

    @property
    def idTeclado(self):
        return self._idTeclado

    @idTeclado.setter
    def idTeclado(self, idTeclado):
        self._idTeclado = idTeclado

    def __str__(self):
        return f'{super().__str__()} - Teclado: [ID: {self._idTeclado}]'


if __name__ == '__main__':
    tec1 = Teclado('Gamer', 'Razer')
    print(tec1)