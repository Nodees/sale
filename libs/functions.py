from libs.conn import connection, conn
#
#
# def select_all(table=None):
#     values = conn.execute(f"SELECT * FROM {table}")
#     values = conn.fetchall()
#
#     return values


def select_all(table=None):
    aux = {}
    obj_list = []

    values = conn.execute(f"SELECT * FROM {table}")
    values = conn.fetchall()

    column_names = conn.execute(f"SELECT column_name, ordinal_position "
                                f"FROM INFORMATION_SCHEMA.COLUMNS "
                                f"WHERE TABLE_NAME = '{table}' ORDER BY ordinal_position")
    column_names = conn.fetchall()

    for column in column_names:
        aux.update({column[0]: ''})

    for value in values:
        for index, column in enumerate(aux):
            aux.update({column: value[index]})
        copy = aux.copy()
        obj_list.append(copy)

    return obj_list

