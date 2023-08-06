import os
from mysql.connector import connect
from dotenv import load_dotenv


class Column(object):

    def __init__(self, column_name, field_type, field_length=None, nullable=False, default=None, primary_key=False):
        self.column_name = column_name
        self.field_type = field_type
        self.field_length = field_length
        self.nullable = nullable
        self.default = default
        self.primary_key = primary_key

    def get_column_sql_string(self):
        ''' Returns the SQL string representation of the column '''

        sql = "{column_name} {field_type}".format(
            column_name=self.column_name, field_type=self.field_type)

        if self.field_length is not None:
            sql += "({field_length}) ".format(field_length=self.field_length)
        else:
            sql += " "

        if self.nullable is False:
            sql += "NOT NULL"
        else:
            sql += "NULL "

        if self.default is not None:
            sql += "DEFAULT {default} ".format(default=self.default)

        if self.primary_key is True:
            sql += " PRIMARY KEY AUTO_INCREMENT"

        return sql
