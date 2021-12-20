class DispositivoES:
    def __init__(self, tipo, marca):
        self._tipo = tipo
        self._marca = marca

    @property
    def tipo(self):
        return self._tipo

    @tipo.setter
    def tipo(self,tipo):
        self._tipo = tipo

    @property
    def marca(self):
        return self._marca

    @marca.setter
    def marca(self, marca):
        self._marca = marca

    def __str__(self):
        return f'Dispositivo: [Tipo: {self._tipo} - Marca: {self._marca}]'


