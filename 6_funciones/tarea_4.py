#Crear una función para calcular el total de un pago
# incluyendo un impuesto aplicado.

def total(valor, impuesto):
    return valor + (valor*impuesto)/100

valor=5500
impuesto=25
print(f'Valor total con 25% de impuesto: {total(valor, impuesto)}')