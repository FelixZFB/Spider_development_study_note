import sqlite3

# 此处本来是要创建test.db的，但是python中\t是制表符，这里用t会出现错误
# 因此，创建的是jest.db
# 连接到数据库，如果没有该数据库，就创建一个数据库

con = sqlite3.connect('D:\jest.db')

# 创建一个游标对象
cur = con.cursor()

# 使用游标对象创建一个表格
cur.execute(' CREATE TABLE person (id integer primary key,name varchar(20),age integer)')