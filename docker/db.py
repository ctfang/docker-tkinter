import sqlite3


def create():
    create_tables = "CREATE TABLE docker (task text, finished integer, date text)"
    query(create_tables)


def query(sql, data=None, receive=False):
    conn = sqlite3.connect("docker.db")
    cursor = conn.cursor()
    if data:
        cursor.execute(sql, data)
    else:
        cursor.execute(sql)

    if receive:
        return cursor.fetchall()
    else:
        conn.commit()

    conn.close()
