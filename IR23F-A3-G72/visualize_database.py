import sqlite3

conn = sqlite3.connect("WordsDatabase.db")
cursor = conn.cursor()
# cursor.execute("""
#     select *
#     from words
# """)

cursor.execute("""
    select *
    from ImportantWords
    where word = 'cristina'
""")


result = cursor.fetchall()
print(result)
# print()
# cursor.execute("""SELECT COUNT(*) FROM words""")
# print(cursor.fetchone()[0])