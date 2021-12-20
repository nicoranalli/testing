vacaciones = False
diaDescanso = False

res = vacaciones or diaDescanso

if res:
    print('Puede asistir')
else:
    print('No puede asistir')