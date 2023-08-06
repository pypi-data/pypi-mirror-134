# DBTools

DBTools is a simple package that eases the creation of databases and their tables. Currently under early development and this will be updated as new features are added.

## Environment Variables

Make sure that the root of your project has an environment variables file name `.env`. The key values for the database include the following environment variables:

* **DB_HOST**: currently it is `localhost` as the default host.
* **DB_USER**: the default username is `dbtools_users`.
* **DB_PASS**: the current default password is `rDP)Otntq(f0r7AD`, this should be changed for security reasons.
* **DB_NAME**: the default database name is `dbtools_db`. Change as needed.

## Connection Module

The connection module provides access to a connection to MySQL or/and the actual database.

The imports required by the connection module are:

* **`import os`**: used for fetching and manipulating environment variables.
* **`from mysql.connector import connect, Error`**: for creating MySQL connections and returning potential errors.
* **`from dotenv import load_dotenv`**: loads the environment variables for the `os` import via `os.getenv('VAR)`.

Currently has the following methods:

* **get_connection()**: returns a connection to MySQL, without the database specified in case the database is not created yet.
* **get_db(db_name=None)**: returns a connection to the MySQL database specified in the environment variables unless specified as the methods `db_name` parameter.
* **get_cursor(db_name=None)**: returns a cursor to the MySQL database specified in the environment variables unless specified as the methods `cursor` parameter.
* **set_env_db_name(db_name)**: edits the environment variable `DB_NAME` to a newly specified database name using the methods `db_name` parameter.

## Column Module

The column module is a class that helps create column objects that can return the SQL string for a given column.

To create a column object, use the following example:

```python
id_column = Column('id', 'int', 11, primary_key=True)
```

To return the SQL string for a given column, use the following method:

```python
id_col_sql = id_column.get_column_sql_string()
```

The column class has the following attributes:

* **column_name**: the name of the column.
* **field_type**: the datatype of the column.
* **field_length**: the length of the field, especially for numeric types, otherwise defaults to `None`.
* **nullable**: lets the column know if the value can be null or not. By default, it is set to `False`, therefore `NOT NULL`.
* **default**: sets a default value to the column if none was given. By default, it is set to `None` meaning no default value.
* **primary_key**: defines this particular column as the primary key which cannot be null and auto increments. Generally used for a row's `id` value.
