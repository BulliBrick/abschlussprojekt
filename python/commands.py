import mysql.connector

connection = mysql.connector.connect(
    user='root', password='', host='mysql', port="3300" , database='abschlussprojekt')
print("Connected to abschlussprojekt")

cursor = connection.cursor()
cursor.execute("SELECT * FROM members")
members = cursor.fetchcall()
connection.close()

print(members)