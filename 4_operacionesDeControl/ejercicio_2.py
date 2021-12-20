verano = ['Enero', 'Febrero', 'Marzo']
otonio = ['Abril','Mayo', 'Junio']
invierno = ['Julio', 'Agosto','Septiembre']
primaveria = ['Octubre', 'Noviembre','Diciembre']

mes = input('Ingresa un mes: ')

if mes in verano:
    print('Estás en verano')
elif mes in otonio:
    print('Estás en otoño')
elif mes in invierno:
    print('Estás en invierno')
else:
    print('Estás en primavera')
