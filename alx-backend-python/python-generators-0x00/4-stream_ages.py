import seed
import logging
from mysql.connector import Error


def stream_user_ages():
    try:
        conn = seed.connect_to_prodev()
        cursor = conn.cursor()
        cursor.execute("SELECT age FROM user_data")
        
        for (age,) in cursor:
            yield age
            
    except Error as error:
        logging.error(f"Fetching data failed: {error}")


def calculate_avg_age():
    total_age = 0
    num_of_ages = 0

    for age in stream_user_ages():
        total_age += age
        num_of_ages += 1

    age_avg = total_age / num_of_ages
    print(f"Average age of users: {age_avg}")


if __name__ == "__main__":
    calculate_avg_age()