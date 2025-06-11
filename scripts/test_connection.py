import cx_Oracle

# Update with your actual username, password, and service name
dsn = cx_Oracle.makedsn('localhost', 1521, service_name='XE')
connection = cx_Oracle.connect(user='SYSTEM', password='Password', dsn=dsn)

print("Successfully connected to the database!")
connection.close()