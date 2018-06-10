import pymysql
conn = pymysql.connect(host='wangdongxu.top', port=13306, user='root', passwd='123456', db='springstudy', charset='utf8')
cursor = conn.cursor()
sql = "select * from user"
cursor.execute(sql)
data = cursor.fetchone()
print(data)