#!/usr/bin/env python3
import mysql.connector
from mysql.connector import Error
 
#Database config
DB_CONFIG = {
    'host': 'localhost',
    'user': 'root',
    'password': '',
    'database': 'ALX_prodev',   
}

def stream_users_in_batches(batch_size):
    """Generator that fetches rows from the user_data table in batches."""
    conn = None
    cursor = None
    try:
        conn = mysql.connector.connect(**DB_CONFIG)
        cursor = conn.cursor(dictionary=True)
        cursor.execute("SELECT * FROM user_data")

        #fetchmany*() pulls many a few rows at a time 
        while True:
            rows = cursor.fetchmany(batch_size)
            if not rows:
                break #stop when no more rows 
            yield rows #yield one batch at a time

    except Error as e:
        print (f"Error:{e}")
    
    finally:
        if cursor:
            cursor.close()
        if conn:
            conn.close()

def batch_processing(batch_size):
    """Processes user batches by filtering users older than 25 Prints them one by one"""
    for batch in stream_users_in_batches(batch_sizes):
        for user in batch:
            if user['age']>25:
                print(user)
