import sqlite3

f = "discobandit.db"
db = sqlite3.connect(f)
c = db.cursor()

q = "SELECT name, students.id, mark FROM students, courses WHERE students.id = courses.id"
sel = c.execute(q)
d = {}

for rec in sel:
        name = rec[0]
        d[name] = [0,0,0]

# print d["tiesto"]

q = "SELECT name, students.id, mark FROM students, courses WHERE students.id = courses.id"
sel = c.execute(q)

for rec in sel:
        name = rec[0]
        # print name
        ids = rec[1]
        # print ids
        grade = rec[2]
        # print grade
        d[name][0] += grade
        d[name][1] = ids
        d[name][2] += 1

for student in d:
        ids = d[student][1]
        avg = (d[student][0])/(d[student][2])
        print "Name: %s ID: %d Average: %d"%(student, ids, avg) # 
        
db.commit()
db.close()
