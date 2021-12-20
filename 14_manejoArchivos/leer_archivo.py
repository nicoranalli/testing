archivo = open('test.txt', 'r')

print(archivo.read())

# leer lineas
archivo.seek(0)
print(archivo.readline())

# leer caracteres
archivo.seek(0)
print(archivo.read(2))

archivo.seek(0)
for linea in archivo:
    print(linea)

archivo.close()