from sqlite3 import *

conn = connect(db_file) #.db 

cursor = conn.cursor()

cursor.execute(query_string)

cursor.execute('update user set name = ? where id = ?', [name, user_id])

rows = cursor.fetchall()