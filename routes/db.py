import pymysql
from routes.passwords import host, username, password, db
def insert(programming_laungage,idea,by):
    connection = pymysql.connect(host,username,password,db)
    cursor = connection.cursor()
    sql = "INSERT INTO ideas(programming_laungage,idea,by_person) VALUES(%s,%s,%s)"
    try:
        cursor.execute(sql,(programming_laungage,idea,by))
        connection.commit()
        connection.close()
        return "Done"
    except Exception as e:
        print(e)
        return "Problame"


def get_data():
    connection = pymysql.connect("localhost","phpmyadmin","gitik","idealab")
    cursor = connection.cursor()
    sql = "SELECT * FROM ideas"
    
    try:
        cursor.execute(sql)
        ar = cursor.fetchall()
        connection.close()
        return ar
    except Exception as e:
        print(e)
        return "Problame"