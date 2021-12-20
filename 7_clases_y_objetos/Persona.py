class Persona:
    # inicializador como en smalltalk
    def __init__(self, nombre, apellido, edad, **notas):
        self._nombre = nombre
        self._apellido = apellido
        self._edad = edad
        self._notas = notas
        # con el guion bajo indicamos que esta restringido su uso publico
        # (solo permitido dentro de la clase, encapsulamiento) doble guion bajo es mas restrictivo

    # metodo get() para notas
    @property
    def notas(self):
        return self._notas

    # metodo set()
    @notas.setter
    def notas(self, notas):
        self._notas = notas

    @property
    def nombre(self):
        return self._nombre

    @nombre.setter
    def nombre(self, nombre):
        self._nombre = nombre

    @property
    def apellido(self):
        return self._apellido

    @apellido.setter
    def apellido(self, apellido):
        self._apellido = apellido

    @property
    def edad(self):
        return self._edad

    @edad.setter
    def edad(self, edad):
        self._edad = edad

    # metodos o comportamientos de la clase
    def mostrarDetalle(self):
        print(f'Datos: {self._nombre} - {self._apellido} - {self._edad}')

    def mostrarNotas(self):
        for materia, nota in self._notas.items():
            print(f'{materia} -> {nota}')

    def __del__(self):
        print(f'Objeto {self._nombre} {self._apellido} eliminado')


