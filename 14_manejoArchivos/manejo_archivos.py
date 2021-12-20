try:
    archivo = open('test.txt', 'w', encoding='utf8')
    archivo.write('Hola\n')
    archivo.write('Chau')
except:
    print('No se pudo crear el archivo')
finally:
    archivo.close()