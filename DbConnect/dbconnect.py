#!/usr/bin/env python

import pyodbc
import pandas

# SQL server authentication

DRIVER = "ODBC Driver 17 for SQL Server"
SERVER = "mssql-2017.labs.wmi.amu.edu.pl"
USER = ""
PASSWORD = ""
DATABASE = ""

if __name__ == "__main__":
    connection_string = "DRIVER={0};SERVER={1};UID={2};PWD={3};DATABASE={4}"

    # connect to database

    conn = pyodbc.connect(
        connection_string.format(DRIVER, SERVER, USER, PASSWORD, DATABASE)
    )

    cursor = conn.cursor()

    # show names of tables

    print("")

    tables = [row.table_name for row in cursor.tables(tableType='TABLE')]
    print(len(tables))
    print(pandas.DataFrame(tables, range(1, len(tables) + 1), ["Table name"]))

    # show first table

    print("")
    print(tables[0] + ":")

    columns = [row.column_name for row in cursor.columns(table=tables[0])]

    cursor.execute("SELECT * FROM " + tables[0])

    rows = [list(row) for row in cursor.fetchall()]

    print(pandas.DataFrame(rows, range(1, len(rows) + 1), columns))

    # close connection

    conn.close()