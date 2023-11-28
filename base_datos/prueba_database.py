import psycopg2


conexion = psycopg2.connect(
    user="jakepys",
    password="123chopin",
    host="127.0.0.1",
    port="5432",
    database="test_db"
)


try:
    with conexion:
        with conexion.cursor() as cursor:
            sentencia = "SELECT * FROM persona WHERE id_persona = %s"
            id_persona = input("Ingresa el id de persona: ")
            cursor.execute(sentencia, (id_persona,))
            registro = cursor.fetchone()
            if registro is None:
                print("No existe el usuario con id: %s" % id_persona)
                exit(1)
            print(registro)
except Exception as e:
    print("%s" % e)

finally:
    conexion.close()
