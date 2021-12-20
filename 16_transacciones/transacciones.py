import psycopg2 as bd

conexion = bd.connect(user='postgres', password='admin', host='localhost', port='5432', database='test')

try:
    cursor = conexion.cursor()
    sentencia1 = "UPDATE persona SET id_persona = 5 WHERE id_persona = 10"
    valores = ('Benjamin', 'Carrizo', 'benjacarrizo@gmail.com')
    cursor.execute(sentencia1, valores)
    conexion.commit()
    print('Termina la transaccion')
except Exception as e:
    conexion.rollback()
    print(f'Ocurrió un error: Se hizo rollback de la transaccion')
finally:
    conexion.close()
