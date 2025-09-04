import mysql.connector
from faker import Faker
import random

# 1. MYSQL 연결 설정
db_connection = mysql.connector.connect(
    host = 'localhost',
    user = 'root',
    password = 'l3yl3yp0rt@$',
    database = "db0904learning01"
)

# 2. MYSQL 연결
cursor = db_connection.cursor()
faker = Faker()    # 제너레이터를 위해서

# 3. users 데이터 생성

for _ in range (100):   # 값 굳이 사용 안 하고 100번을 할거야
    username = faker.user_name()  # 유저이름 생성
    email = faker.email()

    sql = "INSERT INTO users(usernname, email) VALUES(%s, %s)"
    values = (username, email)
    cursor.execute(sql, values)
    # 이메일 값을 넣을거다. (sql 문법 같은데?)
    # print(sql) sql 어떻게 나온느지 확인

# 오더스 테이블 만들어볼께요~
# 일단 user_id 불러오죠?
cursor.execute("SELECT user_id FROM users")
valid_user_id = [row[0] for row in cursor.fetchall()]

for _ in range(10):  #난 10개만 해도 충분해
    user_id = random.choice(valid_user_id)
    product_name = faker.word()
    quantity = random.randint(1, 10)

    try:
        sql = "INSERT INTO orders(user_id, product_name, quantity) VALUES(%s, %s, %s)"
        values = (user_id, product_name, quantity)

        cursor.execute(sql, values)
    except:
        print("오류 발생")
        pass

db_connection.commit()
cursor.close()
db_connection.close()