from dbconnection import getConnection

def get_clientes():
    cnx = getConnection()
    Clientes = []
    with cnx.cursor() as cursor:
        cursor.execute("SELECT id,ccnit,nombre,telefono,direccion,estado FROM cliente")
        Clientes = cursor.fetchall()
    cnx.close()
    return Clientes
