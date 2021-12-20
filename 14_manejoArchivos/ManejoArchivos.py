class ManejoArchivos:
    def __init__(self,archivo):
        self.archivo = archivo

    def __enter__(self):
        print('Entrando al recurso'.center(50,'-'))
        self.archivo = open(self.archivo, 'r')
        return self.archivo

    def __exit__(self, exc_type, exc_val, exc_tb):
        print('Cerrando archivo...')
        if self.archivo:
            self.archivo.close()


