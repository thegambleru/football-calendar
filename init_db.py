import sqlite3

connection = sqlite3.connect('database.db')



with open('schema.sql') as f:
    connection.executescript(f.read())

cur = connection.cursor()


cur.execute("INSERT INTO users (name, day, interval) VALUES (?, ?, ?)",
            ('Silviu Hotoi', '17/02/2023', '12:00 - 14:00')
            )

cur.execute("INSERT INTO users (name, day, interval) VALUES (?, ?, ?)",
            ('Silviu Hotoi', '17/02/2023', '14:00 - 16:00')
            )

cur.execute("INSERT INTO users (name, day, interval) VALUES (?, ?, ?)",
            ('Silviu Hotoi', '17/02/2023', '16:00 - 18:00')
            )

connection.commit()
connection.close()