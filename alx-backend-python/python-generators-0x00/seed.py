import mysql.connector
import csv
import uuid

def connect_db():
    """connect to the database"""
    
    try:
        conn = mysql.connector.connect(user='root', host="localhost", port=3306, password="password")
        return conn
    except mysql.connector.Error as error:
        raise error


def connect_to_prodev():
    """connect to the ALX_prodev database"""
    
    db = connect_db()
    
    cursor = db.cursor()
    cursor.execute("USE ALX_prodev")
    cursor.close()
    return db


def create_table(connection):
    """create the user_data table"""
    
    cursor = connection.cursor()
    create_table = """
        CREATE TABLE IF NOT EXISTS user_data (
            user_id CHAR(36) NOT NULL PRIMARY KEY,
            name VARCHAR(255) NOT NULL,
            email VARCHAR(255) NOT NULL,
            age DECIMAL(3, 0) NOT NULL,
            INDEX(user_id)
        )"""
    cursor.execute(create_table)
    connection.commit()
    cursor.close()
    
    
def create_database(connection):
    """create the ALX_prodev database"""
    
    cursor = connection.cursor()
    cursor.execute("CREATE DATABASE IF NOT EXISTS ALX_prodev")
    cursor.close()


def insert_data(connection, data):
    """insert data into the user_data table"""
    
    cursor = connection.cursor()
    
    with open(data, "r") as file:
        csv_reader = csv.DictReader(file)
        for row in csv_reader:
            user_id = str(uuid.uuid4())
            email = row['email']
            name = row['name']
            age = row['age']

            insert_query = """INSERT INTO user_data (user_id, email, name, age)
                VALUES (%s, %s, %s, %s)
                """
            
            cursor.execute(insert_query, (user_id, email, name, age))
    
    connection.commit()
    cursor.close()

