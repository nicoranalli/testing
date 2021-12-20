class Producto:
    contadorProductos = 0

    @classmethod
    def aumentarProductos(cls):
        cls.contadorProductos += 1
        return cls.contadorProductos

    def __init__(self, nombre, precio):
        self._idProducto = Producto.aumentarProductos()
        self._nombre = nombre
        self._precio = precio

    def __str__(self):
        return f'ID:{self._idProducto} - {self._nombre} - ${self._precio}'

    # metodos get y set
    @property
    def idProducto(self):
        return self._idProducto

    @idProducto.setter
    def idProducto(self, idProducto):
        self._idProducto = idProducto

    @property
    def nombre(self):
        return self._nombre

    @nombre.setter
    def nombre(self, nombre):
        self._nombre = nombre

    @property
    def precio(self):
        return self._precio

    @precio.setter
    def precio(self, precio):
        self._precio = precio


if __name__ == '__main__':
    producto1 = Producto('Pantalon', 2500)
    producto2 = Producto('Zapatillas', 6250)

    print(producto1)
    print(producto2)
