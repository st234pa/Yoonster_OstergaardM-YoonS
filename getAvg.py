import sqlite3

f = "discobandit.db"
db = sqlite3.connect(f)
c = db.cursor()

q = "CREATE TABLE averages (name TEXT, id INTEGER, average INTEGER)"
c.execute(q)

select = "SELECT name, mark FROM students, courses WHERE students.id == courses.id"
s = "INSERT INTO averages VALUES ( %s, "%name

db.commit()
db.close()
