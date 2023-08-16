import pymysql

host = "localhost"
user = "test"
password = "test"
database = "test"


def save_module(module_model):
    connection = pymysql.connect(
        host=host, user=user, passwd=password, database=database
    )
    cursor = connection.cursor()

    query = "insert into modules (run_id, route, case_count, status, started_at, ended_at, duration) values(%s, %s, %s, %s, %s, %s, %s)"

    val = module_model.get_csv_array()

    cursor.executemany(query, val)
    connection.commit()
    connection.close()

    return cursor.lastrowid


def get_module():
    connection = pymysql.connect(
        host=host, user=user, passwd=password, database=database
    )
    cursor = connection.cursor()

    query = "select * from modules order by id desc"

    cursor.execute(query)
    rows = cursor.fetchall()

    for i in rows:
        print(i)

    connection.commit()
    connection.close()
