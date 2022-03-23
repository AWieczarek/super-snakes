import pyodbc
server = 'mysql.wmi.amu.edu.pl'
database = ''
username = ''
password = ''
driver = '{MySQL ODBC 8.0 ANSI Driver}'

with pyodbc.connect('DRIVER='+driver+';SERVER='+server+';PORT=1433;DATABASE='+database+';UID='+username+';PWD='+ password) as conn:
    with conn.cursor() as cursor:
        cursor.execute("SELECT * FROM `Tabela_test`")
        for row in cursor.fetchall():
            print(row)