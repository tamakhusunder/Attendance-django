import mysql.connector
from datetime import datetime

mydb = mysql.connector.connect(
                host="localhost",
                user="root",
                password="admin",
                database="project"
                )
cur = mydb.cursor()

sql = """SELECT MAX(time) FROM faceapp_attendancetb WHERE t_id='730320'"""

cur.execute(sql)

time=cur.fetchall()
print(time)
t=time[0][0]
print(t)
t1 = datetime.strptime(t, '%H:%M:%S.%f').time()

print(type(t1))

t2 = datetime.now().time()
print(t2)
print(type(t2))


interval=datetime.combine(datetime.today(), t2) - datetime.combine(datetime.today(), t1)
print(interval)
minutes = interval.total_seconds() / 60
print(minutes)
print(type(minutes))
# print(t2-t1)