import pymysql
import requests
conn = pymysql.connect(host='wangdongxu.top', port=13306, user='root', passwd='123456', db='springstudy', charset='utf8')
cursor = conn.cursor()
sql = "select * from user"
cursor.execute(sql)
datas = cursor.fetchall()
for data in datas:
    print(data[4])
    response = requests.get(data[4])
    with open("E://"+str(data[1])+".txt","wb") as f:
        f.write(response.content)
