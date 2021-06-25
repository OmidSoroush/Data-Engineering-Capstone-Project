import psycopg2
from sql_queries import create_table_queries, drop_table_queries
conn = psycopg2.connect("dbname=capstone user=postgres password=password")

def create_database():
    """
    - Creates and connects to the sparkifydb
    @return: cursor and connection to sparkifydb
    """

    # connect to default database (add database name)
    conn = psycopg2.connect("dbname=database_name user=postgres password=password")
    conn.set_session(autocommit=True)
    cur = conn.cursor()

    # create database with UTF8 encoding
    cur.execute("DROP DATABASE IF EXISTS sparkifydb")
    cur.execute("CREATE DATABASE sparkifydb WITH ENCODING 'utf8' TEMPLATE template0")

    # close connection to default database
    conn.close()

    # connect to database (add database name)
    conn = psycopg2.connect("dbname=database_name user=postgres password=password")
    cur = conn.cursor()

    return cur, conn


def drop_tables(cur, conn):
    """
    Drops each table using the queries in `drop_table_queries` list.
    @param cur:
    @param conn:
    """
    for query in drop_table_queries:
        cur.execute(query)
        conn.commit()


def create_tables(cur, conn):
    """
    Creates each table using the queries in `create_table_queries` list.
    @param cur:
    @param conn:
    """
    for query in create_table_queries:
        cur.execute(query)
        conn.commit()


def main():
    """
    - Drops (if exists) and Creates the sparkify database.

    - Establishes connection with the sparkify database and gets
    cursor to it.

    - Drops all the tables.

    - Creates all tables needed.

    - Finally, closes the connection.
    """
    cur, conn = create_database()

    drop_tables(cur, conn)
    create_tables(cur, conn)

    conn.close()


if __name__ == "__main__":
    main()
