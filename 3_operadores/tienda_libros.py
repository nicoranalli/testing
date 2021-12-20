nombre = input('Nombre del libro: ')
numID = int(input('Id del libro: '))
precio = float(input('Precio del libro: '))
envio = bool(input('El envio es gratuito? (True/False): '))

print(f'Nombre: {nombre}')
print(f'ID: {numID}')
print(f'Precio: ${precio}')
print(f'Envio gratis: {envio}')
