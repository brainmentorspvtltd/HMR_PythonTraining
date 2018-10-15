# pip install pymysql
import pymysql

connection = pymysql.connect(host='localhost',
                port=3306,
                user='root',
                db='hmr_testEngine',
                autocommit=True)

cursor = connection.cursor()

s_id = 102
s_name = 'Shyam'
s_pwd = '1234'
s_branch = 'IT'

# query = "INSERT INTO students VALUES (101, 'Ram', 1234, 'CS')"
query = "INSERT INTO students VALUES (%s, %s, %s, %s)"
cursor.execute(query, (s_id, s_name, s_pwd, s_branch))
print("Data Inserted Successfully...")