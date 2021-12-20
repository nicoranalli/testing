class Persona:
    def __init__(self, nombre, edad):
        self._nombre = nombre
        self._edad = edad

    def __str__(self):
        return f'Persona {self._nombre} - {self._edad}'

    @property
    def nombre(self):
        return self._nombre

    @nombre.setter
    def nombre(self, nombre):
        self._nombre = nombre

    @property
    def edad(self):
        return self._edad

    @edad.setter
    def edad(self, edad):
        self._edad = edad


class Empleado(Persona):
    def __init__(self, sueldo, nombre, edad):
        super().__init__(nombre, edad)
        self._sueldo = sueldo

    def __str__(self):
        return f'{super().__str__()} - Sueldo {self._sueldo}'


empleado1 = Empleado(5000, 'Jorge', 58)
print(empleado1.nombre)
