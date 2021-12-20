num = int(input('Ingresa un número del 1 al 3: '))

while num> 3 or num <1:
    num = int(input('Ingresa un número DEL 1 AL 3: '))

if num == 1:
    print('Número uno')
elif num == 2:
    print('Número dos')
else:
    print('Número tres')