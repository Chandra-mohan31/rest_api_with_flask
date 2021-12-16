import sqlite3

connection = sqlite3.connect('data.db')

cursor = connection.cursor()

create_table = "CREATE TABLE users (id int, username test, password text)"

cursor.execute(create_table)


user = (0, 'mose', 'ami')

insert_query = "INSERT INTO users VALUES(?,?,?)"

cursor.execute(insert_query, user)

users = [
    (1, 'jose', 'ami'),
    (2, 'rose', 'ami'),
    (3, 'pose', 'ami')
]

cursor.executemany(insert_query, users)

select_query = "SELECT * FROM users"

for row in cursor.execute(select_query):
    print(row)

connection.commit()

connection.close()
