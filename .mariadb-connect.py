import pymysql.cursors
 
# Connect to the database
connection = pymysql.connect(
        host='localhost',
        user='root',
        password='hoge',
        db='DB',
        port = 3307,
        charset='utf8mb4'
        )


# id int, name varchar(20), loginID varchar(20) unique, password varchar(20), createDate date, updateDate date, deleteDate date
with connection.cursor() as cursor:
        sql = "INSERT INTO user (id, name, loginID, password, createDate, updateDate, deleteDate) VALUES (%s, %s, %s, %s, %s, %s, %s)"
        r = cursor.execute(sql, (0, 'pengin', 'pengin0', 'pengin0', '2023-03-09','2023-03-09','2023-03-09'))
        print(r) # -> 1
        # autocommitではないので、明示的にコミットする
        connection.commit()

connection.commit()



connection.close()
print("PythonからMariaDBに接続できました。")