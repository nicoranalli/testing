class Persona:
    contador_personas = 0

    @classmethod
    def _generarValor(cls):
        cls.contador_personas +=1
        return cls.contador_personas

    def __init__(self, nombre, edad):
        self.idPersona = Persona._generarValor()
        self.nombre = nombre
        self.edad = edad

    def __str__(self):
        return f'Persona-> ID: {self.idPersona}  Nombre: {self.nombre}  Edad: {self.edad}'


print('Valor del contador de personas:', Persona.contador_personas)
persona1 = Persona('Nico', 19)
print(persona1)
print('Valor del contador de personas:', Persona.contador_personas)
persona2 = Persona('Juan', 20)
print(persona2)
print('Valor del contador de personas:', Persona.contador_personas)
persona3 = Persona('Alexis', 31)
print(persona3)
print('Valor del contador de personas:', Persona.contador_personas)