import os

DB_DETAILS = {
    'dev': {
        'SOURCE_DB': {
            'DB_TYPE': 'mysql',
            # If SOURCE_DB_HOST is not found, it defaults to 'mysql_container'
            'DB_HOST': os.environ.get('SOURCE_DB_HOST', 'mysql_container'),
            'DB_NAME': os.environ.get('SOURCE_DB_NAME', 'retail_db'),
            'DB_USER': os.environ.get('SOURCE_DB_USER', 'root'),
            'DB_PASS': os.environ.get('SOURCE_DB_PASS', 'Password@123456')
        },
        'TARGET_DB': {
            'DB_TYPE': 'postgres',
            # If TARGET_DB_HOST is not found, it defaults to 'postgres_container'
            'DB_HOST': os.environ.get('TARGET_DB_HOST', 'postgres_container'),
            'DB_NAME': os.environ.get('TARGET_DB_NAME', 'retail_db'),
            'DB_USER': os.environ.get('TARGET_DB_USER', 'postgres'),
            'DB_PASS': os.environ.get('TARGET_DB_PASS', 'Post@123456')
        }
    }
}