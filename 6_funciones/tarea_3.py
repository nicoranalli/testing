#Imprimir numeros de 5 a 1 de manera descendente usando funciones recursivas.
# Puede ser cualquier valor positivo, ejemplo, si pasamos el valor de 5, debe imprimir: 5 4 3 2 1 Si
# se pasa el valor de 3, debe imprimir: 3 2 1 Si se pasan valores negativos no imprime nada

def imprimir(num):
    if num >=1:
        print(num, end=' ')
        imprimir(num-1)

imprimir(55)