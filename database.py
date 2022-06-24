import sqlite3

database = sqlite3.connect('compliment.db')

cursor = database.cursor()

cursor.execute('''
    CREATE TABLE IF NOT EXISTS compliment(
    compliment_id INTEGER PRIMARY KEY AUTOINCREMENT,
    compliment_description TEXT
    )
''')

database.commit()

database.close()
