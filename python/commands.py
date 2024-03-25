import mysql.connector

connection = mysql.connector.connect(
    user='root', password='', host='mysql', port="3300" , database='abschlussarbeit')
print("Connected to abschlussarbeit")

cursor = connection.cursor()
cursor.execute("SELECT * FROM members")
members = cursor.fetchall()
connection.close()

print(members)
