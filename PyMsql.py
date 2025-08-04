import pymysql
test= pymysql.connect(
    host="localhost",
    user="root",
    password="123456789",
    charset="utf8",
    database="yygl"
)
cursor = test.cursor()
# 展示数据库
sql="show databases"
cursor.execute(sql)
result=cursor.fetchall()
for row in result:
        print(row)
create_sql="create table grades(id int,name varchar(10))"
cursor.execute(create_sql)
# 插入数据
insert_sql="insert into grades(id,name) values(%s,%s)"
insert=[
    (1000,"zhangsan"),
    (1002,"LISI"),
    (1003,"WANGWU")
]
result = cursor.executemany(insert_sql,insert)
print(result)
# 更新数据
update_sql="update grades set name=%s where id = %s"
update1 ="javk"
update2=1003
result = cursor.execute(update_sql,(update1,update2))
print(result)
test.commit()
cursor.close()
test.close()