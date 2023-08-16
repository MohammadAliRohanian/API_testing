import pymysql

host = "localhost"
user = "test"
password = "test"
database = "test"


def save_case(case_model):
    connection = pymysql.connect(
        host=host, user=user, passwd=password, database=database
    )
    cursor = connection.cursor()

    query = "insert into cases (module_id, name, status, http_code, started_at, ended_at, duration) values(%s, %s, %s, %s, %s, %s, %s)"

    val = case_model.get_csv_array()

    cursor.executemany(query, val)
    connection.commit()
    connection.close()

    return cursor.lastrowid


def get_case():
    connection = pymysql.connect(
        host=host, user=user, passwd=password, database=database
    )
    cursor = connection.cursor()

    query = "select * from cases order by id desc limit 10"

    cursor.execute(query)
    rows = cursor.fetchall()

    for i in rows:
        print(i)

    connection.commit()
    connection.close()
