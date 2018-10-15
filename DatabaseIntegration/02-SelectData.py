# pip install pymysql
import pymysql

connection = pymysql.connect(host='localhost',
                port=3306,
                user='root',
                db='hmr_testEngine',
                autocommit=True)

cursor = connection.cursor()

s_id = 101

query = 'SELECT * FROM students WHERE s_id = %s'
cursor.execute(query, (s_id))
data = cursor.fetchall()
print(data)