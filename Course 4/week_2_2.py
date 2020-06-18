import sqlite3

conn = sqlite3.connect("emaildb_1.sqlite")
cur = conn.cursor()

cur.execute('DROP TABLE IF EXISTS counts')

cur.execute('CREATE TABLE counts(org TEXT,count INTEGER)')

fh = open('mbox.txt')

for line in fh:
    if line.startswith('From') and not line.startswith('From:'):
        words = line.split()
        email = words[1]
        pos1 = email.find('@')
        org = email[pos1+1:]

        cur.execute('SELECT count FROM counts WHERE org = ?', (org,))
        row = cur.fetchone()

        if row is None:
            cur.execute('INSERT INTO counts (org,count) VALUES (?,1)', (org,))

        else:
            cur.execute('UPDATE counts SET count = count +1 WHERE org = ?', (org,))


conn.commit()
sqlstr = 'SELECT * FROM counts ORDER BY count DESC'

sql = cur.execute(sqlstr)

for row in sql:
    print(str(row[0]), row[1])