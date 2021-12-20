import os


class CatalogoPeliculas:
    ruta_archivo = 'peliculas.txt'

    @classmethod
    def agregarPelicula(cls, pelicula):
        with open(cls.ruta_archivo, 'a') as catalogo:
            catalogo.write(f'{pelicula.nombre}\n')

    @classmethod
    def listarPeliculas(cls):
        with open(cls.ruta_archivo, 'r', encoding='utf8') as catalogo:
            print(catalogo.read())

    @classmethod
    def eliminarPelicula(cls):
        os.remove(cls.ruta_archivo)
