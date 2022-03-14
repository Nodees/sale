# import os
# import sys
from PyQt5.QtWidgets import QMessageBox

from libs.conn import connection, conn


def select_all(table=None):
    with connection:
        sql = f'SELECT * FROM {table} ORDER BY id DESC'

        conn.execute(sql)
        result = conn.fetchall()

        columns = [column[0] for column in conn.description]
        rows = [dict(zip(columns, row)) for row in result]
        return rows


def delete_function(table, data):
    try:
        with connection:
            sql = f'delete from {table} where id = {data}'
            conn.execute(sql)
            connection.commit()

    except Exception as error:
        alert_dialog(str(error), 'Error')


def logical_delete_function(table, data, value):
    try:
        with connection:
            sql = f'update {table} set active = {value} where id = {data}'
            conn.execute(sql)
            connection.commit()

    except Exception as error:
        alert_dialog(str(error), 'Error')


def insert_function(table, data):
    columns = []
    items = []

    for column, item in data.items():
        columns.append(column)
        items.append(item)

    columns = ",".join(columns)
    items = "','".join(items)

    try:
        with connection:
            sql = f"insert into {table} ({columns}) values ('{items}')"
            conn.execute(sql)
            connection.commit()

            alert_dialog('successfully added', 'success')

            return 'ok'
    except Exception as error:
        alert_dialog(str(error), 'Error')


def update_function(table, data):
    set_list = []

    for column, item in data.items():
        set_list.append(f"{column} = '{item}'")

    sets = ','.join(set_list)

    try:
        with connection:
            sql = f"update {table} set {sets} where id = {data.get('id')}"
            conn.execute(sql)
            connection.commit()

            return 'ok'
    except Exception as error:
        alert_dialog(str(error), 'Error')


def alert_dialog( msg: str, title: str):

    msgBox = QMessageBox()

    if title == 'success':
        type_dialog = QMessageBox.Information
        type_button = QMessageBox.Ok
    else:
        type_dialog = QMessageBox.Warning
        type_button = QMessageBox.Close

    msgBox.setIcon(type_dialog)
    msgBox.setText(msg)
    msgBox.setWindowTitle(title)
    msgBox.setStandardButtons(type_button)
    msgBox.exec()