import sqlite3

f = "discobandit.db"
db = sqlite3.connect(f)
c = db.cursor()

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ Create new "averages" table ~~~~~~~~~~~~~~~~~~~~~~~~~~~~
q = "CREATE TABLE averages (name TEXT, id INTEGER, average INTEGER)"
c.execute(q)

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ Populate table ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

# select = "SELECT name, mark FROM students, courses WHERE students.id = courses.id;"

# Insert names, id
select = "SELECT name, id FROM students;"
names = c.execute(select)
for record in names:
	"INSERT INTO averages VALUES ('%s')"%(record) 





db.commit()
db.close()
