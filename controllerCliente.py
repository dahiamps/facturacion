from dbconnection import getConnection


def insert_client(ccnit,nombre,telefono,direccion,estado):
    cnx = getConnection()
    with cnx.cursor() as cursor:
        cursor.execute("INSERT INTO cliente (ccnit,nombre,telefono,direccion,estado) VALUES (%s,%s,%s,%s,%s)",(ccnit,nombre,telefono,direccion,estado))
    cnx.commit()
    cnx.close()


def get_clientes():
    cnx = getConnection()
    Clientes = []
    with cnx.cursor() as cursor:
        cursor.execute("SELECT id,ccnit,nombre,telefono,direccion,estado FROM cliente")
        Clientes = cursor.fetchall()
    cnx.close()
    return Clientes
