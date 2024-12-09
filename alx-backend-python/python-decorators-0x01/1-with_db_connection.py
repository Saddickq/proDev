import sqlite3 
import functools

def with_db_connection(func):
    @functools.wraps(func)
    def wrapper_with_db_connection(*args, **kwargs):
        with sqlite3.connect('users.db') as conn:
            return func(conn, *args, **kwargs)
            
    return wrapper_with_db_connection


@with_db_connection 
def get_user_by_id(conn, user_id): 
    cursor = conn.cursor() 
    cursor.execute("SELECT * FROM users WHERE id = ?", (user_id,)) 
    return cursor.fetchone() 
#### Fetch user by ID with automatic connection handling 

user = get_user_by_id(user_id=1)
print(user)