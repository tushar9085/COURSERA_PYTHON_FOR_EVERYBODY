import sqlite3

conn = sqlite3.connect("emaildb.sqlite")
cur = conn.cursor()

cur.execute('DROP TABLE IF EXISTS counts')

cur.execute('CREATE TABLE counts(email VARCHAR(128),count INTEGER)')

fh = open('mbox-short.txt')

for line in fh:
    if line.startswith('From') and not line.startswith('From:'):
        words = line.split()
        email = words[1]

        cur.execute('SELECT count FROM counts WHERE email = ?', (email,))
        row = cur.fetchone()

        if row is None:
            cur.execute('INSERT INTO counts (email,count) VALUES (?,1)', (email,))

        else:
            cur.execute('UPDATE counts SET count = count +1 WHERE email = ?', (email,))



conn.commit()
sqlstr = 'SELECT * FROM counts ORDER BY count DESC'

for row in cur.execute(sqlstr):
    print(str(row[0]), row[1])
