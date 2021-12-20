#conjunto:  no tienen indice, no podemos modificar los elementos y no permiten repetidos

conjunto = {'Marte', 'Jupiter', 'Venus'}

print(conjunto)

#agregar elemento
conjunto.add('Mercurio')
print(conjunto)

#eliminar elemento
conjunto.remove('Mercurio')
print(conjunto)

#eliminar elemento sin arrojar error si no lo encuentra
conjunto.discard('Mercurios')