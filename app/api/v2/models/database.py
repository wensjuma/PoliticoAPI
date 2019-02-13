import os
import sys
import psycopg2
import psycopg2.extras
from werkzeug.security import generate_password_hash
from config import app_config


db_url= "dbname='politico' host='127.0.0.1' port='5432' user='postgres' password='root'",
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
    Create tables if not existing
    """
    users_table_query = """
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
    parties_table_query=""" 
    CREATE TABLE IF NOT EXISTS parties (
        id SERIAL PRIMARY KEY,
        party_name VARCHAR(32) NOT NULL,
        hqAddress VARCHAR(32) NOT NULL,
        logoUrl VARCHAR(200) NOT NULL

    ) """

    offices_table_query=""" 
    CREATE TABLE IF NOT EXISTS office (
        id SERIAL PRIMARY KEY,
        office_name VARCHAR(32) NOT NULL,
        type VARCHAR(32) NOT NULL
        
    ) """
    return [users_table_query,parties_table_query,
    offices_table_query ]


def drop_table_if_exists():
    """
        Removes all tables on app restart
    """
    drop_users_table = """ 
    DROP TABLE IF EXISTS users CASCADE """

    drop_parties_table = """ 
    DROP TABLE IF EXISTS parties CASCADE """

    drop_offices_table = """ 
    DROP TABLE IF EXISTS offices CASCADE """

    return [drop_users_table, drop_offices_table, drop_parties_table]


def connect_to_db(query=None, DB_URL=None):
    """
        Connection to the database
    """
    conn = None
    cursor = None
    if DB_URL is None:
        DB_URL = os.getenv('DATABASE_URL') 
        print(DB_URL)

    try:
        # connect to db
        conn = psycopg2.connect(DB_URL)
        print("\n\nConnected {}\n".format(conn.get_dsn_parameters()))
        cursor = conn.cursor(cursor_factory=psycopg2.extras.DictCursor)

        if query:
            
            cursor.execute(query)
            conn.commit()

    except(Exception,
           psycopg2.DatabaseError,
           psycopg2.ProgrammingError) as error:
        print("DB ERROR: {}".format(error))

    return conn, cursor


def query_parties_data(query):
    """
        Handles INSERT queries
    """
    try:
        conn = connect_to_db(query)[0]
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
        
        rows = cursor.fetchall()
        conn.close()

    return rows


if __name__ == '__main__':
    init_db()
    connect_to_db()