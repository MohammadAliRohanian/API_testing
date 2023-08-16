import pymysql

host = "localhost"
user = "test"
password = "test"
database = "test"


def save_run(run_model):
    connection = pymysql.connect(
        host=host, user=user, passwd=password, database=database
    )
    cursor = connection.cursor()

    query = "insert into runs (module_count, status, started_at, ended_at, duration) values(%s, %s, %s, %s, %s)"

    val = run_model.get_csv_array()

    cursor.executemany(query, val)
    connection.commit()
    connection.close()

    return cursor.lastrowid


def get_run():
    connection = pymysql.connect(
        host=host, user=user, passwd=password, database=database
    )
    cursor = connection.cursor()

    query = "select * from runs order by id desc limit 10"

    cursor.execute(query)
    rows = cursor.fetchall()

    for i in rows:
        print(i)

    connection.commit()
    connection.close()
