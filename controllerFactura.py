from dbconnection import getConnection


def insert_factura(ccnit,fecha	,valor,saldo):
    cnx = getConnection()
    with cnx.cursor() as cursor:
        cursor.execute("INSERT INTO factura (ccnit,fecha,valor,saldo) VALUES (%s,%s,%s,%s) ",(ccnit,fecha,valor,saldo))
    cnx.commit()
    cnx.close()


def get_factura():
    cnx = getConnection()
    Factura = []
    with cnx.cursor() as cursor:
        cursor.execute("SELECT * FROM factura")
        Factura = cursor.fetchall()
    cnx.close()
    return Factura


def delete_factura(nrofact):
    cnx = getConnection()
    with cnx.cursor() as cursor:
        cursor.execute("DELETE FROM factura WHERE nrofact = %s",(nrofact))
    cnx.commit()
    cnx.close()


def get_factura_id(nrofact):
    cnx = getConnection()
    factura = None
    with cnx.cursor() as cursor:
        cursor.execute("SELECT * FROM factura WHERE nrofact = %s",(nrofact))
        factura = cursor.fetchone()
    cnx.close()
    return factura


def update_factura(fecha,valor,saldo, nrofact):
    cnx = getConnection()
    with cnx.cursor() as cursor:
        cursor.execute("UPDATE factura SET fecha = %s, valor = %s, saldo = %s WHERE nrofact = %s",(fecha,valor,saldo, nrofact))
    cnx.commit()
    cnx.close()
