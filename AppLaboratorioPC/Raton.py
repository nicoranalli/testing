from DispositivoES import DispositivoES


class Raton(DispositivoES):
    contadorRatones = 0

    @classmethod
    def contarRatones(cls):
        cls.contadorRatones += 1
        return cls.contadorRatones

    def __init__(self, tipo, marca):
        super().__init__(tipo, marca)
        self._idRaton = Raton.contarRatones()

    @property
    def idRaton(self):
        return self._idRaton

    @idRaton.setter
    def idRaton(self, idRaton):
        self._idRaton = idRaton

    def __str__(self):
        return f'{super().__str__()} - Ratón: [ID: {self._idRaton}]'


if __name__ == '__main__':
    raton1 = Raton('usb', 'hp')
    print(raton1)
    raton2 = Raton('bluetooth', 'acer')
    print(raton2)
