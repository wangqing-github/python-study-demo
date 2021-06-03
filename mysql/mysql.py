import pymysql


def main():
    conn = pymysql.connect(
        host='localhost',
        user='root',
        password='12345',
        db='test',
        port=3306,
        autocommit=True,  # 如果插入数据，， 是否自动提交? 和conn.commit()功能一致。
    )
    # ****python, 必须有一个游标对象， 用来给数据库发送sql语句， 并执行的.
    # 2. 创建游标对象，
    cur = conn.cursor()
    create_sqli = "select roleid from user_info"
    cur.execute(create_sqli)
    values = cur.fetchall()
    for row in values:
        sql = "insert into user_battle_skin values (%s,%s,%s)"
        cur.execute(sql, [row[0], 60001,1])


if __name__ == '__main__':
    main()
