#!/usr/bin/python3
seed = __import__('seed')


def stream_users():
    """
    Generator that fetches rows one by one from the user_data table.
    """
    connection = seed.connect_to_prodev()
    cursor = connection.cursor(dictionary=True)
    cursor.execute("SELECT * FROM user_data")

    # Use one loop only
    for row in cursor:
        yield row

    connection.close()
