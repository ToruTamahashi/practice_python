"""
実行前に...
コンテナ起動
docker run --name mysql -e MYSQL_ROOT_PASSWORD=mysql -d -p 3306:3306 mysql
コンテナに接続
docker exec -it [CONTAINER ID] bash
MYSQLに接続
mysql -u root -p
データベース作成
  mysql> CREATE DATABASE python_test;
  mysql> SHOW DATABASES;
"""
import mysql.connector

conn = mysql.connector.connect(
      host='localhost',
      port='3333',
      user='root',
      password='root',
      database='mydb'
  )

cursor = conn.cursor()

# cursor.execute(    'CREATE DATABASE test_mysql_databases')

# テーブル作成
cursor.execute(
    'CREATE TABLE person('
    'id int NOT NULL AUTO_INCREMENT,'
    'name varchar(14) NOT NULL,'
    'PRIMARY KEY(id))'
)
# データ挿入
cursor.execute('INSERT INTO person(name) values("Jun")')

# アップデート
#cursor.execute('UPDATE person set name = "Michel" WHERE name = "Mike"')

# データ検索
'''
cursor.execute('SELECT * FROM person')
for row in cursor:
    print(row)
'''
conn.commit()
cursor.close()
conn.close()