#%%
# Importiert den MYSQL Python Connector
import mysql.connector 

#%%
# Verbindet sich mit der Datenbank 'abschlussarbeit' auf dem port 3306 mit dem User 'root' und dem Passwort 'root'. Gibt aus sobald die Verbindung hergestellt wurde.
connection = mysql.connector.connect(
    user='root', password='root', host='mysql', port="3366" , database='abschlussarbeit')
print("Connected to abschlussarbeit")

#%%
# Entfehrne die '''  am Anfang und Ende um den Code zu aktivieren. Dies ist ein beispiel Eintrag in die Tabelle. Dieser Eintrag verwendet den python Mysql connector.
'''
# Erstellt einen Cursor um SQL Befehle auszuführen
cursor = connection.cursor()

# SQL querry für neuen Eintrag in der Tabelle 'members'
sql = "INSERT INTO members (nachname, vorname, spitzname, age) VALUES (%s, %s, %s, %s)"

# Definiert die Variablen für die Spalten in der Tabelle 'members'
nachname = "Arlt"
vorname = "Johnatan"
spitzname = "Jonny"
age = 18

# Führt den SQL Befehl aus und fügt die Variablen in die Tabelle 'members' ein
cursor.execute(sql, (vorname, nachname, spitzname, age))
connection.commit()

'''