from util import get_connection


def build_insert_query(table_name, column_names):
    # 1. Join columns with "," so it looks like: col1","col2","col3
    joined_columns = '","'.join(column_names)

    # 2. Add the outer quotes: "col1","col2","col3"
    column_names_string = f'"{joined_columns}"'

    # 3. Create placeholders: %s, %s, %s
    placeholders = ', '.join(['%s'] * len(column_names))

    # 4. Construct the final query
    query = f'INSERT INTO "{table_name}" ({column_names_string}) VALUES ({placeholders})'

    return query


def insert_data(connection, cursor, query, data, batch_size=100):
    recs = []
    for i, rec in enumerate(data, 1):
        recs.append(rec)
        if i % batch_size == 0:
            cursor.executemany(query, recs)
            connection.commit()
            print(f"Batch of {batch_size} committed...")
            recs = []

    # CRITICAL: Handle the remaining records (the last batch)
    if len(recs) > 0:
        cursor.executemany(query, recs)
        connection.commit()
        print(f"Final batch of {len(recs)} committed.")


def load_table(db_details, data, column_names, table_name):
    TARGET_DB = db_details['TARGET_DB']

    connection = get_connection(
        db_type=TARGET_DB['DB_TYPE'],
        db_host=TARGET_DB['DB_HOST'],
        db_name=TARGET_DB['DB_NAME'],
        db_user=TARGET_DB['DB_USER'],
        db_pass=TARGET_DB['DB_PASS']
    )

    if connection is None:
        print(f"Error: Could not establish connection to Target DB for {table_name}")
        return

    try:
        cursor = connection.cursor()
        query = build_insert_query(table_name, column_names)
        insert_data(connection, cursor, query, data)
        print(f"Successfully loaded {table_name}")
    except Exception as e:
        print(f"!!! Error loading table {table_name}: {e}")
        connection.rollback()
    finally:
        connection.close()