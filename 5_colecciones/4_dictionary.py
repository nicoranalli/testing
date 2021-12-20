dic = {
    'IDE': 'Integrated Development Environment',
    'OOB': 'Oriented Objects Programming', 
    'DBMS': 'Database Management System'
}

print(dic['IDE'])
print(dic.get('OOB'))

#RECORRER UN DICT
for llave,valor in dic.items():
    print(llave, valor)

for llave in dic.keys():
    print(llave)
    
for valor in dic.values():
    print(valor)