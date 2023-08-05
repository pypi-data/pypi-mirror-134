from sqlite3 import *

conn = sqlite3.connect(db_file) #.db 

cursor = conn.cursor()

cursor.execute(query_string)