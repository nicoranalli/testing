def listarTermino(**terminos):
    for llave, valor in terminos.items():
        print(llave, valor)


listarTermino(Uno='1', Dos='2', PK='Primary Key')
