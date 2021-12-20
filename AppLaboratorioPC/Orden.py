class Orden:
    contadorOrdenes = 0

    @classmethod
    def contarOrden(cls):
        cls.contadorOrdenes += 1
        return cls.contadorOrdenes

    def __init__(self, computadoras):
        self._idOrden = Orden.contarOrden()
        self._computadoras = list(computadoras)

    @property
    def idOrden(self):
        return self._idOrden

    @idOrden.setter
    def idOrden(self, idOrden):
        self._idOrden = idOrden

    @property
    def computadoras(self):
        return self._computadoras

    @computadoras.setter
    def computadoras(self, computadoras):
        self._computadoras = computadoras

    def __str__(self):
        computadoras_str = ''
        for computadora in self._computadoras:
            computadoras_str += computadora.__str__()

    def agregarComputadoras(self, computadora):
        self._computadoras.append((computadora))
