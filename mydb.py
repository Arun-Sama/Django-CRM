import mysql.connector

database = mysql.connector.connect(
    host='localhost',
    user='root',
    passwd='Passwordweak'
)
# preparing cursor object[to fetch the details from the database]
cursorObject = database.cursor()
# create a database
cursorObject.execute("CREATE DATABASE company")
print("All Done!")
