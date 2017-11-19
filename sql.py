
import sqlite3

con =sqlite3.connect('db.sqlite3')

cursor = con.cursor()

# get row count of database
res = cursor.execute("SELECT COUNT(*) FROM blog_blog").fetchone()[0]


print(res)

# cursor.execute("INSERT INTO blog_blog VALUES('이병세', 85)")
#
# con.commit()
#
# con.close()
