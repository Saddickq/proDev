import seed
from mysql.connector import Error
import logging

def stream_users_in_batches(batch_size):
    try:
        db = seed.connect_db()
        cursor = db.cursor(dictionary=True)
        cursor.execute("USE ALX_prodev")
        cursor.execute("SELECT * FROM user_data")
        while True:
            batch = cursor.fetchmany(size=batch_size)
            if not batch:
                break
            yield batch
    except Error as error:
        logging.error(f"ERROR: {error}")

def batch_processing(batch_size):
    for batch in stream_users_in_batches(batch_size):
        for user in batch:
            if user["age"] > 25:
                print(user)