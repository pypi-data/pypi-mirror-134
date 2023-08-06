import os
from mysql.connector import connect
from column import Column
from database import get_db


class Table(object):

    def __init__(self, table_name, columns):
        self.table_name = table_name
        self.columns = columns

    def get_table_sql_string(self):
        ''' Returns the SQL string for the table '''

        sql = "CREATE TABLE IF NOT EXISTS {table_name} (".format(
            table_name=self.table_name)

        for column in self.columns:
            if self.columns.index(column) == len(self.columns) - 1:
                sql += "{column})".format(column=column)
            else:
                sql += "{column}, ".format(column=column)

        return sql

    def create_table(self):
        ''' Creates a new table in the database '''

        sql = self.get_table_sql_string()

        db = get_db(db_name='dbtools_db')

        cursor = db.cursor()
        cursor.execute(sql)
