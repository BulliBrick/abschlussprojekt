
# Importiert den MYSQL Python Connector
import mysql.connector


# Verbindet sich mit der Datenbank 'abschlussarbeit' auf dem port 3306 mit dem User 'root' und dem Passwort 'root'. Gibt aus sobald die Verbindung hergestellt wurde.
connection = mysql.connector.connect(
    user='root', password='root', host='mysql', port="3306" , database='abschlussarbeit')
print("Connected to abschlussarbeit")