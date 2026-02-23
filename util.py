from mysql import connector as mc
from mysql.connector import errorcode as ec
import psycopg2
import pandas as pd
from config import DB_DETAILS

def load_db_details(env):
    return DB_DETAILS[env]


def get_mysql_connection(db_host, db_name, db_user, db_pass):
    connection = None  # <--- CRITICAL: Initialize this first!
    try:
        connection = mc.connect(
            host=db_host,  # Ensure this matches the argument name
            user=db_user,
            password=db_pass,
            database=db_name
        )
    except mc.Error as error:
        print(f"Connection Error: {error}")

    return connection

def get_pg_connection(db_host, db_name, db_user, db_pass):
    """Establishes a connection to the Target PostgreSQL database."""
    try:
        connection = psycopg2.connect(
            host=db_host,
            database=db_name,
            user=db_user,
            password=db_pass
        )
        return connection
    except Exception as error:
        print(f"PostgreSQL Error: {error}")
    return None


def get_connection(db_type, db_host, db_name, db_user, db_pass):
    connection = None
    if db_type == 'mysql':
        connection = get_mysql_connection(db_host=db_host,
                                          db_name=db_name,
                                          db_user=db_user,
                                          db_pass=db_pass)
    if db_type == 'postgres':
        connection = get_pg_connection(db_host=db_host,
                                       db_name=db_name,
                                       db_user=db_user,
                                       db_pass=db_pass
                                       )
    return connection


def get_tables(path, table_list):
    tables = pd.read_csv(path, sep=':')

    if table_list == 'all':
        return tables.query('to_be_loaded == "yes"')
    else:
        # Create a DataFrame from the split list of table names
        table_list_df = pd.DataFrame(table_list.split('.'), columns=['table_name'])

        # Join and query. Note: backslash allows multi-line chaining
        return tables.join(table_list_df.set_index('table_name'), on='table_name', how='inner') \
            .query('to_be_loaded == "yes"')


