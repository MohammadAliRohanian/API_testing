import pymysql
import config

host = config.DB_HOST
user = config.DB_USER
password = config.DB_PASS
database = config.DB_NAME

# Insert to db and save started_at
def init_run(started_at):
    connection = pymysql.connect(
        host=host, user=user, passwd=password, database=database
    )
    cursor = connection.cursor()

    query = "insert into runs (started_at) values(%s)"

    val = started_at

    cursor.execute(query, val)
    connection.commit()
    connection.close()

    # Print stared run
    print("------ Run Started at " + str(started_at) + " ------")

    return cursor.lastrowid

# Upadte runs
def finalize_run(run_model):
    connection = pymysql.connect(
        host=host, user=user, passwd=password, database=database
    )
    cursor = connection.cursor()

    # query = "insert into runs (module_count, status, started_at, ended_at, duration) values(%s, %s, %s, %s, %s)"
    query = "update runs set status = %s, ended_at = %s, duration = %s where id = %s"

    val = run_model.get_csv_array()

    cursor.executemany(query, val)
    connection.commit()
    connection.close()

    # print ended_at & duration
    print(
        "------ Run Ended at "
        + str(val[0][1])
        + ". Duration: "
        + str(val[0][2])
        + " ------"
    )

    return cursor.lastrowid

# Select the last 10 rows
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
