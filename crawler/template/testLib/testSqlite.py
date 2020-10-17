# -*- coding = utf-8 -*-
# @Time: 2020/10/16 9:33 AM
# @Author: haotianmichael
# @File: testSqlite.py
# @Software: PyCharm


import sqlite3
# 1. 打开/创建数据库文件
con = sqlite3.connect("./DB/test.db")


# 2. 创建数据表
c = con.cursor()   # 获取游标

# sql = '''
#     create table company
#         (id int primary key not null,
#         name text not null,
#         age int not null,
#         address char(50),
#         salary real);
# '''
# print("Open databse successfully")

# 3. 插入数据

# sql = '''
#     insert into company(id, nam, age, address, salary)
#     values (1, "haotian", 32, "Beijing", 89000);
# '''

# print("Insert Data successfully")


# 4. 查询数据

sql = "select id, nam, address, salary from company"

cursor = c.execute(sql)   # 执行sql语句

for row in cursor:
    print("id = ", row[0])
    print("name = ", row[1])
    print("address = ", row[2])
    print("salary = ", row[3])

con.commit()   # 提交数据库操作
con.close()   # 关闭连接


