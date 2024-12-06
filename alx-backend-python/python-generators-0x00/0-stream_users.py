import seed
    
def stream_users():
    try:
        connection = seed.connect_db()
        cursor = connection.cursor()
        cursor.execute("USE ALX_prodev")
        cursor.execute("SELECT * FROM user_data LIMIT 20;")
        rows = cursor.fetchall()
        for row in rows:
            yield row
    except Exception as e:
        raise e
    finally:
        cursor.close()
        connection.close()