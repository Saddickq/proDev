import time
import sqlite3 
import functools


query_cache = {}


def with_db_connection(func):
    @functools.wraps(func)
    def wrapper_with_db_connection(*args, **kwargs):
        with sqlite3.connect('users.db') as conn:
            return func(conn, *args, **kwargs)
            
    return wrapper_with_db_connection


def cache_query(func):
    @functools.wraps(func)
    def wrapper_cache_query(*args, **kwargs):
        query = kwargs['query']
        if query in query_cache:
            print("This is the Cache")
            return query_cache[query]
        else:
            result = func(*args, **kwargs)
            query_cache[query] = result
            print("No Cache here")
            return result
    return wrapper_cache_query


@with_db_connection
@cache_query
def fetch_users_with_cache(conn, query):
    cursor = conn.cursor()
    cursor.execute(query)
    return cursor.fetchall()

#### First call will cache the result
users = fetch_users_with_cache(query="SELECT * FROM users")
print(users)

#### Second call will use the cached result
users_again = fetch_users_with_cache(query="SELECT * FROM users")
print(users_again)