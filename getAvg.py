import sqlite3

f = "discobandit.db"
db = sqlite3.connect(f)
c = db.cursor()

q = "SELECT name, students.id, mark FROM students, courses WHERE students.id = courses.id"
t = c.execute(q)
d = {}

for r in t:
        name = r[0]
        dict[name] = [0,0,0]

for r in t:
        name = r[0]
        sid = r[1]
        grade = [2]
        d[name][0] += grade
        d[name][1] = sid
        d[name][2] += 1

for key in d:
        sid = d[key][1]
        avg = d[key][0]/d[key][2]
        print "Name: %s ID: %d Avg: %d"%(key, sid, avg)
        
db.commit()
db.close()
