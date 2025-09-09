import pymysql

# 1) db connection
connection = pymysql.connect(
    host = '127.0.0.1',
    user = 'root',
    password = 'l3yl3yp0rt@$',
    db = 'classicmodels',
    charset = 'utf8mb4',
    cursorclass = pymysql.cursors.DictCursor
)

def get_customers():
    cursor = connection.cursor()
    sql = "SELECT * FROM customers"
    cursor.execute(sql)
    customers = cursor.fetchone()
    print("customers: ", customers['country'])
    print("customers: ", customers['customerName'])
    print("customers: ", customers)


# CRUD
# INSERT INTO
def add_customers():
    cursor = connection.cursor()
    name = 'hochizzle'
    family_name = 'solen'
    phone = '00555'
    addressLine1 = 'daegu'
    sql = f"INSERT INTO customers(customerNumber, customerName, contactLastName, phone, addressLine1) Values({10000}, '{name}', '{family_name}' '{phone}','{addressLine1}')"
    cursor.execute(sql)
    connection.commit()  # commit해야함! 실제로 우리가 한 걸 데이터 베이스에 반영해라 라는 뜻.
# 나는 지금 not null 표시 몇 개 빼먹었는데...흠;

# 3. update set
def update_customer():
    cursor = connection.cursor()
    update_name = 'update_hochizzle'
    contactLastName = 'update_solen'
    sql = f"UPDATE customers SET customerName = '{update_name}', contactLastName = '{contactLastName}' WHERE customerNumer = 1000"
    cursor.execute(sql)
    connection.commit()
    cursor.close()

add_customers()

# 4. ddelete from
def delete_customer():
    cursor = connection.cursor()
    sql = "DELETE FROM customers WHERE customerNumber = 1000"
    cursor.execute(sql)
    connection.commit()
