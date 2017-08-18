import sqlite3

conn = sqlite3.connect('test.db')
cursor = conn.cursor()
# cursor.execute('create table user (id varchar(20) primary key, name varchar(20))')
# cursor.execute('insert into user (id, name) values (\'2\', \'LiuNian\')')
# cursor.execute('insert into user (id, name) values (\'3\', \'WangMiao\')')
# cursor.execute('select * from user where id=?', ('1',))
cursor.execute('select * from user')
values = cursor.fetchall()
print values

cursor.close()
conn.commit()
conn.close()