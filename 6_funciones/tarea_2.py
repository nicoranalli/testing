#Crear una función para multiplicar los valores recibidos de tipo numérico,
# utilizando argumentos variables *args como parámetro de la función y
# regresar como resultado la multiplicación de todos los valores pasados como argumentos.

def mult(*nums):
    mul = 1
    for num in nums:
        mul *= num
    return mul


print(mult(2, 3, 4, 1))