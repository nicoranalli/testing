nombres = ['Nico','Alexis','Guty','Bianca']
print(nombres)

print(nombres[0])
print(nombres[1])
ultimoElemento = len(nombres) - 1
print(nombres[ultimoElemento])

print(nombres[0:2])

print(nombres[2:])

nombres[1] = 'Ricardo'

print(nombres)

for nom in nombres:
    print(nom)

#agregar un elemento
nombres.append('Lorenzo')
print(nombres)

#insertar elemento
nombres.insert(1, 'Octavio')
print(nombres)

#remover elemnto
nombres.remove('Octavio')
print(nombres)

#remover el ultimo elemento
nombres.pop()
print(nombres)

#remover con indice
del nombres[0]
print(nombres)

#limpiar lista
nombres.clear()
print(nombres)
