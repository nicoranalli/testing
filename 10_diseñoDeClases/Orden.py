from Producto import Producto


class Orden:
    contadorOrdenes = 0

    @classmethod
    def contarOrdenes(cls):
        cls.contadorOrdenes += 1
        return cls.contadorOrdenes

    def __init__(self, productos):
        self._idOrder = Orden.contarOrdenes()
        self._productos = list(productos)

    def agregarProducto(self, producto):
        self._productos.append(producto)

    def calcularPrecio(self):
        total = 0
        for producto in self._productos:
            total += producto.precio

        return total

    def __str__(self):
        productosStr = ''
        for producto in self._productos:
            productosStr += producto.__str__() + ' | '

        return f'Orden: {self._idOrder} - \nProductos: {productosStr}'


if __name__ == '__main__':
    producto1 = Producto('Pantalon', 2500)
    producto2 = Producto('Zapatillas', 6250)
    productos = [producto1, producto2]

    orden = Orden(productos)
    print(orden)