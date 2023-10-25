''' Source: https://www.sqlitetutorial.net/sqlite-python/sqlite-python-select/'''

import sqlite3
from sqlite3 import Error


def create_connection(db_file):
    """ create a database connection to the SQLite database
        specified by the db_file
    :param db_file: database file
    :return: Connection object or None
    """
    conn = None
    try:
        conn = sqlite3.connect(db_file)
    except Error as e:
        print(e)

    return conn


def select_all_tasks(conn):
    """
    Query all rows in the tasks table
    :param conn: the Connection object
    :return:
    """
    cur = conn.cursor()
    cur.execute("SELECT * FROM students")

    rows = cur.fetchall()

    for row in rows:
        print("- [ ] " + row[1] + " " + row[3])



def main():
    database = r"D:\Coding\Python\sqlliteTest\Students."

    # create a database connection
    conn = create_connection(database)
    with conn:

        print("Markdown Checklist of all Students")
        select_all_tasks(conn)


#if __name__ == '__main__':
main()
