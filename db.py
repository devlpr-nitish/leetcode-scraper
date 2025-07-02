
import os

import psycopg2 
from scraper import get_profile_info
from dotenv import load_dotenv


load_dotenv()


def store_data(data):

    db_url = os.getenv('DATABASE_URL')

    if not db_url :
        raise ValueError("Data base url is not available")


    pg_connect = psycopg2.connect(db_url)

    cur = pg_connect.cursor()

    cur.execute("""
        CREATE TABLE IF NOT EXISTS user_info (
            id SERIAL PRIMARY KEY,
            username TEXT,
            ranking INTEGER,
            easy INTEGER,
            medium INTEGER,
            hard INTEGER,
            total INTEGER
        )
    """)

    if data:
        cur.execute("""
            INSERT INTO user_info (username, ranking, easy, medium, hard, total)
            VALUES (%s, %s, %s, %s, %s, %s)
        """, (
            data['username'], data['ranking'], data['easy'],
            data['medium'], data['hard'], data['total']
    ))
    
    pg_connect.commit()
    cur.close()
    pg_connect.close()





