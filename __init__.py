import sqlite3

connection = sqlite3.connect('Concerts.db')
cursor = connection.cursor()

# print(connection.total_changes)


rows = cursor.execute("SELECT band_name FROM bands").fetchall()
print(rows)

rows = cursor.execute("SELECT venue_title FROM venues").fetchall()
print(rows)

rows = cursor.execute("SELECT venue_id FROM concerts").fetchall()
print(rows)

rows = cursor.execute("SELECT band_id FROM concerts").fetchall()
print(rows)


