from .Empleado import Empleado
from .Gerente import Gerente


def imprimirDetalles(objeto):
    print(objeto)
    print(type(objeto))
    if isinstance(objeto, Gerente):
        print(objeto.departamento)


gerente1 = Gerente('Nicolas', 19, 4)
empleado1 = Empleado('Juan', 30)

imprimirDetalles(gerente1)
imprimirDetalles(empleado1)