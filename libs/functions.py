import os
import sys

from libs.conn import connection, conn


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


def delete_function(table, data):
    try:
        conn.execute(f'delete from {table} where id = {data}')
        connection.commit()
        connection.close()

        python = sys.executable
        os.execl(python, python, *sys.argv)

    except Exception as erro:
        print(erro)


def insert_function(table, data):
    columns = []
    items = []

    for column, item in data.items():
        columns.append(column)
        items.append(item)

    columns = ",".join(columns)
    items = "','".join(items)

    try:
        conn.execute(f"insert into {table} ({columns}) values ('{items}')")
        connection.commit()
        connection.close()

        python = sys.executable
        os.execl(python, python, *sys.argv)

        return 'ok'
    except Exception as error:
        print(error)
