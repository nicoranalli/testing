# Crear una función para sumar los valores recibidos de tipo numérico,
# utilizando argumentos variables *args como parámetro de la función y
# regresar como resultado la suma de todos los valores pasados como argumentos.

def sumar(*nums):
    suma = 0
    for num in nums:
        suma += num
    return suma


print(sumar(2, 3, 4, 1))
