from libs.conn import connection, conn


def _list():
    query = conn.execute("SELECT * FROM department")
    query = conn.fetchall()

    return query
