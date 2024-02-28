import sqlite3

conn = sqlite3.connect("calendar.db")
cursor = conn.cursor()

cursor.execute('''CREATE TABLE IF NOT EXISTS family(
                familyId INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
                sirName varchar(50),
                numMembers int
            )''')

print("hello")
cursor.execute("INSERT INTO family (sirName, numMembers) VALUES (?, ?)", ('Pope', 3))
# Inserting data into the family table

# Committing the transaction and closing the connection
conn.commit()
conn.close()



# res = cursor.execute("SELECT * FROM family WHERE sirName='spam'")
# res.fetchone() is None
# print(res)