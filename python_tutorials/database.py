import sqlite3

db = sqlite3.connect('Company.db')

db.execute('create table Employeess(name text,salary int)')

db.execute('insert into Employeess(name,salary) values(?,?)',('rajesh',6000))
db.execute('insert into Employeess(name,salary) values(?,?)',('kamlesh',700))
db.execute('insert into Employeess(name,salary) values(?,?)',('hitesh',200))
db.commit()

data_base = db.execute('select * from Employeess order by name')

for emp_details in data_base:
    print(emp_details)