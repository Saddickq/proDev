import sqlite3 
import functools

def with_db_connection(func):
    @functools.wraps(func)
    def wrapper_with_db_connection(*args, **kwargs):
        with sqlite3.connect('users.db') as conn:
            return func(conn, *args, **kwargs)
            
    return wrapper_with_db_connection


def transactional(func):
    @functools.wraps(func)
    def wrapper_transactional(*args, **kwargs):
        conn = args[0]
        try:
            func(*args, **kwargs)
            conn.commit()
        except Exception as e:
            conn.rollback()
    return wrapper_transactional


@with_db_connection 
@transactional 
def update_user_email(conn, user_id, new_email): 
    cursor = conn.cursor() 
    cursor.execute("UPDATE users SET email = ? WHERE id = ?", (new_email, user_id)) 
#### Update user's email with automatic transaction handling 

update_user_email(user_id=1, new_email='Crawford_Cartwright@hotmail.com')