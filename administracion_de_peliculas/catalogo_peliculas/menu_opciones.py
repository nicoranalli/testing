from servicio.catalogo_peliculas import CatalogoPeliculas
from dominio.Pelicula import Pelicula

def menu():
    print('Menú de opciones'.center(50, '-'))
    print('1-Agregar Pelicula')
    print('2-Listar Peliculas')
    print('3-Eliminar catalogo')
    print('4-Salir')
    opt = int(input('Ingrese una opción ---> '))
    return opt


def agregarPelicula(pelicula):
    CatalogoPeliculas.agregarPelicula(pelicula)


def listarPelicula():
    CatalogoPeliculas.listarPeliculas()


def eliminarCatalogo():
    CatalogoPeliculas.eliminarPelicula()


opt = 1
while opt != 4:
    opt = menu()
    if opt == 1:
        nombre = input('Ingrese el nombre de la pelicula a agregar: ')
        pel = Pelicula(nombre)
        agregarPelicula(pel)
        print('Pelicula agregada!')

    elif opt == 2:
        try:
            listarPelicula()
        except:
            print('Archivo no encontrado o eliminado!')
    else:
        try:
            eliminarCatalogo()
            print('Archivo de catalogo eliminado!')
        except:
            print('Archivo no encontrado!')


