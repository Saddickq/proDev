import mysql.connector
from dotenv import load_dotenv
import os
import logging
import csv
import uuid

load_dotenv()

def connect_db():
    """connect to the database"""
    
    try:
        conn = mysql.connector.connect(
            user=os.getenv("DB_USER"), 
            host=os.getenv("DB_HOST"), 
            port=os.getenv("DB_PORT"), 
            password=os.getenv("DB_PASSWORD")
        )
        if conn.is_connected():
            return conn
    except mysql.connector.Error as error:
        logging.error(f"MySql connection failed {error}")


def connect_to_prodev():
    """connect to the ALX_prodev database"""
    
    try:
        db = connect_db()
        cursor = db.cursor()
        cursor.execute("USE ALX_prodev")
        return db
    except mysql.connector.Error as error:
        logging.error(f"Connection to the ALX_prodev database failed: {error}")
    finally:
        cursor.close()


def create_table(connection):
    """create the user_data table"""
    
    try:
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
    except mysql.connector.Error as error:
        logging.error(f"Create database table failed: {error}")
    finally:
        connection.commit()
        cursor.close()
    
    
def create_database(connection):
    """create the ALX_prodev database"""
    
    cursor = connection.cursor()
    cursor.execute("CREATE DATABASE IF NOT EXISTS ALX_prodev")
    cursor.close()


def insert_data(connection, data):
    """insert data into the user_data table"""
    
    try:
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
                
    except mysql.connector.Error as error:
        logging.error(f"Database Insertion failed: {error}")
    finally:
        connection.commit()
        cursor.close()

