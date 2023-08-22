import pymysql
import config

host = config.DB_HOST
port = config.DB_PORT
user = config.DB_USER
password = config.DB_PASS
database = config.DB_NAME


# Insert to db
def save_case(case_model):
    connection = pymysql.connect(
        host=host, port=port, user=user, passwd=password, database=database
    )
    cursor = connection.cursor()

    query = "insert into cases (run_id, status, module, name, description, route, http_code, started_at, ended_at, duration) values(%s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"

    val = case_model.get_csv_array()

    cursor.executemany(query, val)
    connection.commit()
    connection.close()

    # Print cases that in executing
    print("       Case Executed.")

    return cursor.lastrowid


# Select the last 10 rows
def get_case():
    connection = pymysql.connect(
        host=host, port=port, user=user, passwd=password, database=database
    )
    cursor = connection.cursor()

    query = "select * from cases order by id desc limit 10"

    cursor.execute(query)
    rows = cursor.fetchall()

    for i in rows:
        print(i)

    connection.commit()
    connection.close()
