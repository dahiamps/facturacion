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


def delete_clientes():
    cnx = getConnection()
    with cnx.cursor() as cursor:
        cursor.execute("DELETE FROM cliente WHERE estado = '0' or NOT EXISTS(SELECT * FROM factura WHERE ccnit = cliente.ccnit)")
    cnx.commit()
    cnx.close()


def get_cliente_id(id):
    cnx = getConnection()
    cliente = None
    with cnx.cursor() as cursor:
        cursor.execute("SELECT id, ccnit, nombre, telefono, direccion, estado FROM cliente WHERE id = %s",(id))
        cliente = cursor.fetchone()
    cnx.close()
    return cliente


def update_cliente(ccnit, nombre, telefono, direccion, estado, id):
    cnx = getConnection()
    with cnx.cursor() as cursor:
        cursor.execute("UPDATE cliente SET ccnit = %s, nombre = %s, telefono = %s, direccion = %s , estado = %s WHERE id = %s",(ccnit, nombre, telefono, direccion, estado, id))
    cnx.commit()
    cnx.close()
