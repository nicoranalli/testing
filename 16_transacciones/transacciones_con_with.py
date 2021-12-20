import psycopg2 as bd

conexion = bd.connect(user='postgres', password='admin', host='127.0.0.1', port='5432', database='test')

try:
    with conexion:
        with conexion.cursor() as cursor:
            sentencia1 = "INSERT INTO persona(nombre, apellido, email) VALUES(%s,%s,%s)"
            valores = ('Gael', 'Kuchen', 'gkuchen@gmail.com')
            cursor.execute(sentencia1, valores)
            sentencia2 = "UPDATE persona SET id_persona=6 WHERE id_persona=11"

except Exception as e:
    print(f'Error, se hizo un rollback')
finally:
    conexion.close()
print('Termina la transaccion')