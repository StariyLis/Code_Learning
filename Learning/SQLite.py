import sqlite3
from pprint import pprint as pp

conn = sqlite3.connect('exemple.db')
cur = conn.cursor()

cur.execute('CREATE TABLE IF NOT EXISTS test(Дата TEXT, Курс FLOAT)')
data = [('20.03.2019', 65.2), ('21.03.2019', 65.25), ('22.03.2019', 65.15), ('23.03.2019', 65.03)]
cur.executemany('INSERT INTO test VALUES(?,?)', data)
conn.commit()
cur.execute('SELECT * FROM test')
d = cur.fetchall()
cur.close()
conn.close()
pp(d)
