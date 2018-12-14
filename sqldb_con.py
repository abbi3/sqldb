import pymysql

conn = pymysql.connect(host='localhost', port=3306, user='root', passwd='', db='mysql')

cur = conn.cursor()
cur.execute("""Create table students(uname varchar(5), password varchar(10),id varchar2(20));""")
print(cur.description)

for row in cur:
    print(row)
cur.close()
conn.close()


