class Monitor:
    contadorMOnitores = 0

    @classmethod
    def contarMonitores(cls):
        cls.contadorMOnitores += 1
        return cls.contadorMOnitores

    def __init__(self, marca, tamanio):
        self._idMonitor = Monitor.contarMonitores()
        self._marca = marca
        self._tamanio = tamanio

    def __str__(self):
        return f'Monitor: [ID: {self._idMonitor} - Marca: {self._marca} - Tamaño: {self._tamanio}]'


if __name__ == '__main__':
    mon1 = Monitor('Philco', 48)
    mon2 = Monitor('Philco', 21)
    print(mon1)
    print(mon2)
