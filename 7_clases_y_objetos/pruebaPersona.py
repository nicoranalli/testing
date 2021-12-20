from Persona import Persona

print('Creacion de objetos'.center(50, '-'))
persona1 = Persona('Nicolas', 'Ranalli', 19, PPR=8, ASI=7, AM2=7, FISICA2=10)

persona1.mostrarDetalle()
# Persona.mostrarDetalle(persona1)
persona1.mostrarNotas()

persona2 = Persona('Daniela', 'Ranalli', 53)

persona2.mostrarDetalle()

# modificar atributos

persona2.nombre = 'Daniela Juana'

print()
print('Eliminación de objetos'.center(50, '-'))
del persona2
