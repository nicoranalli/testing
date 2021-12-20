import psycopg2

conexion = psycopg2.connect(user='postgres',
                            password='admin',
                            host='localhost',
                            port='5432',
                            database='test')

"""print(conexion)
cursor = conexion.cursor()
sentence = 'SELECT * FROM persona WHERE id_persona in (1,2)'
cursor.execute(sentence)
registros = cursor.fetchall()
print(registros)
"""
try:
    with conexion:
        with conexion.cursor() as cursor:
            sentence = 'INSERT INTO persona(nombre, apellido, email) VALUES(%s, %s, %s)'
            valores = ('Daniela', 'Ranalli', 'daniguaty@gmail.com')
            cursor.execute(sentence, valores)
            registros_insertados = cursor.rowcount
            print(registros_insertados)
except Exception as e:
    print(f'Ocurrió un error: {e}')
finally:
    conexion.close()