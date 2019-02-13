import os
import sys
import psycopg2
import psycopg2.extras
from werkzeug.security import generate_password_hash
from config import app_config


def init_db(DB_URL=None):
    
    try:
        conn, cursor = connect_to_db()
        create_db_query = drop_table_if_exists() + set_up_tables()
        i = 0
        while i != len(create_db_query):
            query = create_db_query[i]
            cursor.execute(query)
            conn.commit()
            i += 1
        print("--"*50)
        conn.close()

    except Exception as error:
        print("\nQuery not executed : {} \n".format(error))


def set_up_tables():
    """
        Queries run to set up and create tables
    """
    table_users = """
    CREATE TABLE users (
        id SERIAL PRIMARY KEY,
        username VARCHAR (24) NOT NULL UNIQUE,
        firstname VARCHAR (24) NOT NULL,
        lastname VARCHAR (24) NOT NULL,
        othername VARCHAR (24),
        phone VARCHAR (24) NOT NULL,
        email VARCHAR (30) NOT NULL UNIQUE,
        password VARCHAR (128) NOT NULL,
        passportUrl VARCHAR (200),
        isPolitician BOOLEAN,
        isAdmin BOOLEAN
    )"""



    # I'm the admin of this system.
    password = generate_password_hash('@ndel@')
    create_admin_query = """
    INSERT INTO users(username, firstname, lastname, othername ,phone, email, password, passportUrl , isPolitician ,isAdmin) VALUES(
        '{}', '{}', '{}', '{}', '{}', '{}', '{}', '{}', '{}', '{}'
    )""".format('John', 'John', 'Doe', 'Brims' ,'0705324u4','johndoe@gmail.com', password, "", False ,True)

    return [table_users,create_admin_query]


def drop_table_if_exists():
    """
        Removes all tables on app restart
    """
    drop_users_table = """
    DROP TABLE IF EXISTS users CASCADE"""

    return [drop_users_table]


def connect_to_db(query=None, DB_URL=None):
    """
        Initiates a connection to the db and executes a query
    """
    conn = None
    cursor = None
    if DB_URL is None:
        DB_URL = os.getenv('DATABASE_URL') #get the DATABASE_URL
        print(DB_URL)

    try:
        # connect to db
        conn = psycopg2.connect(DB_URL)
        print("\n\nConnected {}\n".format(conn.get_dsn_parameters()))
        cursor = conn.cursor(cursor_factory=psycopg2.extras.DictCursor)

        if query:
            # Execute query
            cursor.execute(query)
            # Commit changes
            conn.commit()

    except(Exception,
           psycopg2.DatabaseError,
           psycopg2.ProgrammingError) as error:
        print("DB ERROR: {}".format(error))

    return conn, cursor


def query_data_from_db(query):
    """
        Handles INSERT queries
    """
    try:
        conn = connect_to_db(query)[0]
        # After successful INSERT query
        conn.close()
    except psycopg2.Error as _error:
        sys.exit(1)


def select_data_from_db(query):
    """
        Handles SELECT queries
    """
    rows = None
    conn, cursor = connect_to_db(query)
    if conn:
        # Retrieve SELECT query results from db
        rows = cursor.fetchall()
        conn.close()

    return rows

# initialize the db operations
if __name__ == '__main__':
    init_db()
    connect_to_db()